import json, os, re, html
K=os.path.expanduser("~/Downloads/apple-design-kb")
def inline(items, refs):
    out=[]
    for it in items or []:
        t=it.get("type")
        if t=="text": out.append(it.get("text",""))
        elif t=="codeVoice": out.append("`"+it.get("code","")+"`")
        elif t in("emphasis","strong"): out.append(inline(it.get("inlineContent"),refs))
        elif t=="reference":
            r=refs.get(it.get("identifier"),{}); out.append(r.get("title") or it.get("identifier","").split("/")[-1])
        elif t=="link": out.append(it.get("title") or it.get("destination",""))
        elif t=="image":
            r=refs.get(it.get("identifier"),{}); out.append(f"[imagem: {r.get('alt') or it.get('identifier')}]")
        else: out.append(inline(it.get("inlineContent"),refs))
    return "".join(out)
def blocks(items, refs, depth=0):
    md=[]
    for b in items or []:
        t=b.get("type")
        if t=="heading": md.append("\n"+"#"*min(6,b.get("level",2)+1)+" "+b.get("text",""))
        elif t=="paragraph": md.append(inline(b.get("inlineContent"),refs))
        elif t in("unorderedList","orderedList"):
            for i,li in enumerate(b.get("items",[]),1):
                txt=" ".join(blocks(li.get("content"),refs,depth+1)).strip()
                md.append(("  "*depth)+("- " if t=="unorderedList" else f"{i}. ")+txt)
        elif t=="aside": md.append("> "+(b.get("name") or b.get("style","note")).upper()+": "+" ".join(blocks(b.get("content"),refs,depth+1)))
        elif t=="table":
            for row in b.get("rows",[]):
                md.append("| "+" | ".join(" ".join(blocks(c,refs,depth+1)).replace("\n"," ") for c in row)+" |")
        elif t=="links":
            md.append("Links: "+", ".join((refs.get(i,{}).get("title") or i) for i in b.get("items",[])))
        elif t in("row","tabNavigator","small"):
            for c in b.get("columns",[]) or b.get("tabs",[]) or []:
                md.extend(blocks(c.get("content"),refs,depth+1))
            if t=="small": md.append(inline(b.get("inlineContent"),refs))
        elif t=="codeListing": md.append("```\n"+"\n".join(b.get("code",[]))+"\n```")
        else:
            if b.get("content"): md.extend(blocks(b.get("content"),refs,depth+1))
            elif b.get("inlineContent"): md.append(inline(b.get("inlineContent"),refs))
    return md
idx=[]
for f in sorted(os.listdir(f"{K}/raw/hig")):
    j=json.load(open(f"{K}/raw/hig/{f}")); refs=j.get("references",{})
    title=j.get("metadata",{}).get("title",f); url="https://developer.apple.com"+(j.get("identifier",{}).get("url","").replace("doc://com.apple.HIG","") or "")
    md=[f"# {title}", f"Fonte: https://developer.apple.com/design/human-interface-guidelines/{f[:-5]}", "", inline(j.get("abstract"),refs), ""]
    for s in j.get("primaryContentSections",[]): md.extend(blocks(s.get("content"),refs))
    for tsec in j.get("topicSections",[]) or []:
        md.append("\n## "+tsec.get("title","Topics")); md.extend("- "+(refs.get(i,{}).get("title") or i) for i in tsec.get("identifiers",[]))
    text="\n".join(md); open(f"{K}/text/hig/{f[:-5]}.md","w").write(text)
    idx.append({"slug":f[:-5],"title":title,"chars":len(text),"images":sum(1 for r in refs.values() if r.get("type")=="image")})
json.dump(idx,open(f"{K}/text/hig_index.json","w"),indent=1)
man=json.load(open(f"{K}/raw/video_manifest.json")); vidx=[]
for v in man:
    h=open(f"{K}/raw/videos/{v['id']}.html",encoding="utf-8",errors="ignore").read()
    m=re.search(r'<section[^>]*id="transcript-content"[^>]*>(.*?)</section>',h,re.S)
    paras=[]
    if m:
        for p in re.findall(r'<p[^>]*>(.*?)</p>',m.group(1),re.S):
            t=re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",p))).strip()
            if t: paras.append(t)
    desc=re.search(r'<meta name="description" content="([^"]*)"',h)
    head=[f"# {v.get('title')}", f"Fonte: {v['url']}", f"Duração: {round((v.get('seconds') or 0)/60,1)} min", "Descrição: "+html.unescape(desc.group(1)) if desc else "", ""]
    open(f"{K}/text/transcripts/{v['id']}.md","w").write("\n".join(head+paras))
    vidx.append({"id":v["id"],"title":v.get("title"),"seconds":v.get("seconds"),"media":"sd_mp4" if v.get("sd") else ("hls" if v.get("m3u8") else "none"),"sd_bytes":v.get("sd_bytes"),"transcript_chars":sum(map(len,paras))})
json.dump(vidx,open(f"{K}/text/video_index.json","w"),indent=1)
print("HIG md:",len(idx),"chars:",sum(i["chars"] for i in idx),"imagens:",sum(i["images"] for i in idx))
print("transcrições:",len(vidx),"com texto:",sum(1 for v in vidx if v["transcript_chars"]>500),"chars:",sum(v["transcript_chars"] for v in vidx))
print("sem transcrição e com mídia:",[v["id"] for v in vidx if v["transcript_chars"]<=500 and v["media"]!="none"])
print("sem mídia:",[(v["id"],v["title"]) for v in vidx if v["media"]=="none"])
hls=[v for v in vidx if v["media"]=="hls"]; print("HLS:",len(hls),"horas:",round(sum(v["seconds"] or 0 for v in hls)/3600,1))
