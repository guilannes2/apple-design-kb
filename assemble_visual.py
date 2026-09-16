# Junta as notas por vídeo e por página do HIG, marca o status pela verificação de códigos e limpa travessões.
import json, os, glob, re
K=os.path.expanduser("~/Downloads/apple-design-kb")
rep=json.load(open(f"{K}/kb/visual_logs/verificacao_codigos.json"))
per=rep["per_video"]
titles={v["id"]:v["title"] for v in json.load(open(f"{K}/raw/video_manifest.json"))}
def clean(s):
    s=re.sub(r"\s+[—–]\s+",", ",s)
    s=re.sub(r"(?<=\w)—(?=\w)",", ",s)
    return s
def order(p):
    m=re.search(r"folhas_(\d{4})-(\d{4})",p); return int(m.group(1)) if m else 0
def status(uid):
    x=per.get(uid)
    if not x: return "não processado"
    if x["verified"]==x["sheets"]: return f"assistido: {x['sheets']} de {x['sheets']} folhas abertas, todos os códigos conferidos"
    return f"parcial: {x['verified']} de {x['sheets']} folhas com código conferido; faltam as folhas {x['missing'][:40]}"
rows=[]
for d in sorted(glob.glob(f"{K}/kb/visual/*/")):
    vid=os.path.basename(d.rstrip("/")); parts=sorted(glob.glob(f"{d}folhas_*.md"),key=order)
    if not parts: continue
    body="\n\n".join(clean(open(p).read()).strip() for p in parts)
    st=status(vid)
    open(f"{K}/kb/visual/{vid}.md","w").write(f"# {vid}: {titles.get(vid,'')}\n\nStatus visual: {st}.\n\n{body}\n")
    rows.append((vid,titles.get(vid,""),st))
hrows=[]
for d in sorted(glob.glob(f"{K}/kb/visual_hig/*/")):
    page=os.path.basename(d.rstrip("/")); parts=sorted(glob.glob(f"{d}*_folhas_*.md"),key=lambda p:(("vid" in os.path.basename(p)),os.path.basename(p)))
    if not parts: continue
    units=sorted({re.sub(r"_folhas_.*","",os.path.basename(p)) for p in parts})
    sts=[f"{u}: {status(u)}" for u in units]
    body="\n\n".join(clean(open(p).read()).strip() for p in parts)
    open(f"{K}/kb/visual_hig/{page}.md","w").write(f"# HIG, página {page}: o que as ilustrações e vídeos mostram\n\nStatus visual:\n"+"\n".join(f"- {s}" for s in sts)+f"\n\n{body}\n")
    hrows.append((page,sts))
idx=["# Índice visual","",f"Vídeos com notas: {len(rows)}. Assistidos por inteiro: {sum(1 for r in rows if r[2].startswith('assistido'))}.",""]
idx+=[f"- {v} ({t}): {s}" for v,t,s in rows]
idx+=["",f"Páginas do HIG com notas: {len(hrows)}.",""]
for p,sts in hrows: idx.append(f"- {p}: "+"; ".join(sts))
open(f"{K}/kb/INDICE_VISUAL.md","w").write("\n".join(idx)+"\n")
print(f"vídeos montados {len(rows)} (assistidos {sum(1 for r in rows if r[2].startswith('assistido'))}) | páginas HIG montadas {len(hrows)}")
