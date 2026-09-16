# Baixa as ilustrações do HIG com o contexto de onde aparecem (página, título da seção, legenda, alt).
import json, glob, os, re, time, urllib.request, concurrent.futures as cf
K=os.path.expanduser("~/Downloads/apple-design-kb")
DARK_PAGES=re.compile(r"color|dark-mode|material|liquid-glass|app-icons|icons$")
def text(inl):
    out=[]
    for x in inl or []:
        if isinstance(x,dict):
            if x.get("type")=="text": out.append(x.get("text",""))
            elif "inlineContent" in x: out.append(text(x["inlineContent"]))
            elif x.get("type")=="codeVoice": out.append(x.get("code",""))
    return " ".join(s for s in out if s).strip()
occ=[]; seen=set()
for f in sorted(glob.glob(f"{K}/raw/hig/*.json")):
    d=json.load(open(f)); slug=os.path.basename(f)[:-5]; refs=d.get("references",{})
    title=(d.get("metadata") or {}).get("title",slug)
    state={"h":title,"last_par":""}
    def walk(node):
        if isinstance(node,list):
            for n in node: walk(n)
            return
        if not isinstance(node,dict): return
        t=node.get("type")
        if t=="heading": state["h"]=node.get("text",state["h"])
        if t is None and "title" in node and "content" in node: state["tab"]=node.get("title")
        if t=="video" and node.get("identifier"):
            rid=node["identifier"]; r=refs.get(rid,{})
            cap=text(((node.get("metadata") or {}).get("abstract")))
            h=state["h"]+(f" (aba {state['tab']})" if state.get("tab") else "")
            occ.append({"page":slug,"page_title":title,"heading":h,"before":state["last_par"],"caption":cap,"alt":r.get("alt"),"id":rid,"type":"video","variants":r.get("variants",[]),"poster":r.get("poster")})
        if t=="paragraph":
            imgs=[x for x in node.get("inlineContent",[]) if isinstance(x,dict) and x.get("type") in ("image","video")]
            if not imgs: state["last_par"]=text(node.get("inlineContent"))[:300]
            for im in imgs:
                rid=im.get("identifier"); r=refs.get(rid,{})
                cap=text(((im.get("metadata") or {}).get("abstract")))
                occ.append({"page":slug,"page_title":title,"heading":state["h"],"before":state["last_par"],"caption":cap,"alt":r.get("alt"),"id":rid,"type":r.get("type"),"variants":r.get("variants",[]),"poster":r.get("poster")})
        for k,v in node.items():
            if k in ("inlineContent",) : continue
            if isinstance(v,(list,dict)): walk(v)
    walk(d.get("primaryContentSections",[])); walk(d.get("sections",[]))
imgs=[]; vids=[]; thumbs=0
for o in occ:
    if o["type"]=="video": vids.append(o); continue
    tr=[tuple(v.get("traits",[])) for v in o["variants"]]
    if not any("light" in t or "dark" in t for t in tr) and any("_wide_" in v.get("url","") for v in o["variants"]): thumbs+=1; continue
    key=(o["page"],o["id"])
    if key in seen: continue
    seen.add(key)
    def pick(app):
        for want in (("2x",app),("1x",app)):
            for v in o["variants"]:
                if set(want)<=set(v.get("traits",[])): return v["url"]
        return None
    o["url_light"]=pick("light") or next((v["url"] for v in o["variants"] if "2x" in v.get("traits",[])),o["variants"][0]["url"] if o["variants"] else None)
    o["url_dark"]=pick("dark") if DARK_PAGES.search(o["page"]) else None
    imgs.append(o)
def get(url,dest):
    if url.startswith("/"): url="https://developer.apple.com/tutorials"+url
    if os.path.exists(dest) and os.path.getsize(dest)>0: return 0
    for a in range(4):
        try:
            b=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read()
            open(dest,"wb").write(b); time.sleep(0.15); return len(b)
        except Exception as e: err=e; time.sleep(2*(a+1))
    raise RuntimeError(f"{url} {err}")
jobs=[]
for i,o in enumerate(imgs):
    for kind in ("light","dark"):
        u=o.get(f"url_{kind}")
        if u:
            ext=os.path.splitext(u.split("?")[0])[1] or ".png"
            o[f"file_{kind}"]=f"media_hig/img/{o['page']}__{i:04d}_{kind}{ext}"; jobs.append((u,f"{K}/{o[f'file_{kind}']}"))
fails=[]; tot=0
os.makedirs(f"{K}/media_hig/video",exist_ok=True); vseen=set(); vids_u=[]
for j,o in enumerate(vids):
    if (o["page"],o["id"]) in vseen: continue
    vseen.add((o["page"],o["id"]))
    v=next((v for v in o["variants"] if "light" in v.get("traits",[])), o["variants"][0] if o["variants"] else None)
    if v: o["file"]=f"media_hig/video/{o['page']}__{j:03d}.mp4"; jobs.append((v["url"],f"{K}/{o['file']}")); vids_u.append(o)
vids=vids_u
with cf.ThreadPoolExecutor(4) as ex:
    futs={ex.submit(get,u,d):(u,d) for u,d in jobs}
    for fu in cf.as_completed(futs):
        try: tot+=fu.result()
        except Exception as e: fails.append(str(e)[:200])
json.dump({"images":imgs,"videos":vids,"skipped_related_session_thumbnails":thumbs,"failures":fails},open(f"{K}/raw/hig_media_manifest.json","w"),ensure_ascii=False,indent=1)
print(f"ocorrências de imagem únicas por página: {len(imgs)} | com versão escura baixada: {sum(1 for o in imgs if o.get('url_dark'))} | miniaturas de sessões puladas: {thumbs} | vídeos no conteúdo: {len(vids)} | arquivos: {len(jobs)} | MB novos: {tot/1e6:.1f} | falhas: {len(fails)}")
print("páginas:",len({o['page'] for o in imgs}))
