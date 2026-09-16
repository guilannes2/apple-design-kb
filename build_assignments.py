# Monta lotes para os agentes: no máximo 25 folhas por agente; vídeo longo é dividido, vídeos curtos são agrupados.
import json, os, glob, sys
K=os.path.expanduser("~/Downloads/apple-design-kb"); CAP=25
wave=sys.argv[1]
done_path=f"{K}/kb/visual_logs/assigned.json"
assigned=set(json.load(open(done_path))) if os.path.exists(done_path) else set()
infos=sorted([json.load(open(p)) for p in glob.glob(f"{K}/frames/*/DONE.json")],key=lambda x:x["id"])
new=[i for i in infos if i["id"] not in assigned]
pieces=[]
for i in new:
    S=i["sheets"]; parts=-(-S//CAP); size=-(-S//parts)
    for p in range(parts):
        a=p*size+1; b=min(S,(p+1)*size)
        pieces.append({"video_id":i["id"],"title":i["title"],"from":a,"to":b,"total":S,"transcript":i["transcript"]})
bins=[]; cur=[]; n=0
for pc in pieces:
    k=pc["to"]-pc["from"]+1
    if cur and n+k>CAP: bins.append(cur); cur=[]; n=0
    cur.append(pc); n+=k
if cur: bins.append(cur)
out=[{"label":f"{wave}-{j+1:03d}","items":b} for j,b in enumerate(bins)]
json.dump(out,open(f"{K}/kb/visual_logs/{wave}_assignments.json","w"),ensure_ascii=False,indent=1)
json.dump(sorted(assigned|{i["id"] for i in new}),open(done_path,"w"))
print(f"{wave}: vídeos novos {len(new)} | folhas {sum(i['sheets'] for i in new)} | agentes {len(out)}")
print(json.dumps(out,ensure_ascii=False,separators=(",",":")))
