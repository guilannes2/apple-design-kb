# Lotes do HIG: até 25 folhas por agente, na ordem das páginas; ilustrações e vídeos da mesma página ficam juntos quando cabem.
import json, os
K=os.path.expanduser("~/Downloads/apple-design-kb"); CAP=25
units=json.load(open(f"{K}/sheets_hig/manifest.json"))
order=sorted(units,key=lambda u:(u["page"],0 if u["kind"]=="hig-imagens" else 1,u["id"]))
pieces=[]
for u in order:
    S=u["sheets"]; parts=-(-S//CAP); size=-(-S//parts)
    for p in range(parts):
        pieces.append({"unit_id":u["id"],"kind":u["kind"],"page":u["page"],"title":u["title"],"from":p*size+1,"to":min(S,(p+1)*size),"total":S})
bins=[]; cur=[]; n=0
for pc in pieces:
    k=pc["to"]-pc["from"]+1
    if cur and n+k>CAP: bins.append(cur); cur=[]; n=0
    cur.append(pc); n+=k
if cur: bins.append(cur)
out=[{"label":f"hig-{j+1:03d}","items":b} for j,b in enumerate(bins)]
json.dump(out,open(f"{K}/kb/visual_logs/hig_assignments.json","w"),ensure_ascii=False,indent=1)
print(f"unidades {len(units)} | folhas {sum(u['sheets'] for u in units)} | agentes {len(out)}")
