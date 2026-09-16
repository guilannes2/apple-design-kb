# Confere folha por folha se o código que o agente anotou (lido na imagem) bate com o carimbado.
# Lê kb/visual_logs/parts/*.json escritos pelos agentes. Uso: python verify_codes.py <dir_segredo>
import json, os, sys, glob, re
K=os.path.expanduser("~/Downloads/apple-design-kb")
import hashlib
SALT=open(os.path.join(sys.argv[1],"salt")).read().strip()
class _Codes:
    # código esperado recalculado da chave secreta, sem depender de codes.json
    def get(self,vid,default=None):
        return {"__getn__":vid}
codes=None
def expected(vid,n): return hashlib.sha1(f"{SALT}|{vid}|{n}".encode()).hexdigest()[:5].upper()
infos={json.load(open(p))["id"]:json.load(open(p)) for p in glob.glob(f"{K}/frames/*/DONE.json")}
if os.path.exists(f"{K}/sheets_hig/manifest.json"):
    for u in json.load(open(f"{K}/sheets_hig/manifest.json")): infos[u["id"]]={"id":u["id"],"sheets":u["sheets"],"kind":u["kind"]}
ok=set(); wrong=[]; unreadable_logs=[]
for p in sorted(glob.glob(f"{K}/kb/visual_logs/parts/*.json")):
    try: log=json.load(open(p))
    except Exception as e: unreadable_logs.append(os.path.basename(p)); continue
    for s in log.get("sheets_viewed",[]):
        vid=s.get("video_id"); n=int(s.get("sheet",0)); c=str(s.get("code","")).strip().upper()
        exp=expected(vid,n) if vid else None
        if exp and c==exp: ok.add((vid,n))
        else: wrong.append({"log":os.path.basename(p),"video_id":vid,"sheet":n,"declared":c})
# segunda fonte de evidência: códigos escritos nos cabeçalhos das notas (lidos na imagem pelo agente)
header_ok=0
for f in glob.glob(f"{K}/kb/visual/*/folhas_*.md")+glob.glob(f"{K}/kb/visual_hig/*/*_folhas_*.md"):
    for vid,n,c in re.findall(r"### (\S+) · folha (\d{4}) · .*?código ([A-Z0-9]+)",open(f).read()):
        n=int(n)
        if (vid,n) not in ok and c.upper()==expected(vid,n): ok.add((vid,n)); header_ok+=1
wrong=[w for w in wrong if (w["video_id"],w["sheet"]) not in ok]
per={}
for vid,i in infos.items():
    seen=sum(1 for n in range(1,i["sheets"]+1) if (vid,n) in ok)
    per[vid]={"sheets":i["sheets"],"verified":seen,"missing":[n for n in range(1,i["sheets"]+1) if (vid,n) not in ok]}
full=sorted(v for v,x in per.items() if x["verified"]==x["sheets"])
rep={"videos_processed":len(infos),"sheets_total":sum(i["sheets"] for i in infos.values()),"sheets_verified":len(ok),
     "codes_wrong":len(wrong),"videos_fully_watched":len(full),"fully_watched":full,"wrong":wrong,"unreadable_logs":unreadable_logs,"per_video":per}
json.dump(rep,open(f"{K}/kb/visual_logs/verificacao_codigos.json","w"),indent=1,ensure_ascii=False)
hig=[v for v in per if v.startswith("hig-")]; vid=[v for v in per if not v.startswith("hig-")]
def summ(keys): return {"unidades":len(keys),"folhas":sum(per[k]["sheets"] for k in keys),"verificadas":sum(per[k]["verified"] for k in keys),"completas":sum(1 for k in keys if per[k]["verified"]==per[k]["sheets"])}
print("folhas conferidas só pelo cabeçalho das notas:",header_ok); print("vídeos Apple:",summ(vid),"| HIG:",summ(hig),"| códigos errados:",len(wrong),"| logs ilegíveis:",len(unreadable_logs))
