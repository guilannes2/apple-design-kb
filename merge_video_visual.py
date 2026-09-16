# Insere nos cartões de kb/videos a síntese visual verificada de cada vídeo e troca a linha Base pelo status real.
# Uso: python merge_video_visual.py [--dry]
import os, re, glob, json, sys
K=os.path.expanduser("~/Downloads/apple-design-kb"); DRY="--dry" in sys.argv
per=json.load(open(f"{K}/kb/visual_logs/verificacao_codigos.json"))["per_video"]
has_media={v["id"]:bool(v.get("sd") or v.get("m3u8")) for v in json.load(open(f"{K}/raw/video_manifest.json"))}
def clean(s):
    s=re.sub(r"\s+[—–]\s+",", ",s); return re.sub(r"(?<=\w)—(?=\w)",", ",s)
stats={"sintese":0,"pendente":0,"sem_midia":0,"base_trocada":0}
for f in sorted(glob.glob(f"{K}/kb/videos/*.md")):
    s=open(f).read()
    s=re.sub(r"\n*<!-- visual:[A-Za-z0-9_-]+ -->.*?<!-- /visual:[A-Za-z0-9_-]+ -->\n*","\n\n",s,flags=re.S)
    heads=list(re.finditer(r"^## .*\(id: ([A-Za-z0-9_-]+)[,)].*$",s,flags=re.M))
    for m in reversed(heads):
        vid=m.group(1); nxt=re.search(r"^## ",s[m.end():],flags=re.M)
        end=m.end()+nxt.start() if nxt else len(s)
        sec=s[m.end():end]; x=per.get(vid)
        if x:
            st=(f"transcrição e {x['sheets']} de {x['sheets']} folhas de quadros vistas, códigos conferidos" if x["verified"]==x["sheets"]
                else f"transcrição e {x['verified']} de {x['sheets']} folhas de quadros com código conferido (visualização parcial)")
            new=re.sub(r"Base: transcrição \(quadros ainda não vistos\)",f"Base: {st}",sec,count=1)
            if new!=sec: stats["base_trocada"]+=1
            sec=new
        syn=f"{K}/kb/visual_sintese_videos/{vid}.md"
        if os.path.exists(syn): body=clean(open(syn).read()).strip(); stats["sintese"]+=1
        elif x or has_media.get(vid): body="### O que as imagens mostram\n\nSíntese visual pendente."; stats["pendente"]+=1
        else: body="### O que as imagens mostram\n\nVídeo sem mídia disponível no site; nenhum quadro visto."; stats["sem_midia"]+=1
        block=f"\n\n<!-- visual:{vid} -->\n{body}\n<!-- /visual:{vid} -->\n\n"
        s=s[:m.end()]+sec.rstrip()+block+s[end:].lstrip("\n")
    if not DRY: open(f,"w").write(s)
print(("SIMULAÇÃO " if DRY else "")+str(stats))
