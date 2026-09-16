# Encaixa cartões novos de vídeo (kb/cartoes_novos/<id>.md) no arquivo do grupo: substitui o cartão existente
# ou insere antes de "## O que este grupo revela", e atualiza a menção na seção "## Sem transcrição".
# Uso: python merge_new_cards.py [--dry]
import os, re, glob, json, sys
K=os.path.expanduser("~/Downloads/apple-design-kb"); DRY="--dry" in sys.argv
g=json.load(open(f"{K}/groups.json"))
where={vid:i for i,grp in enumerate(g["videos"]) for vid in grp["ids"]}
def clean(s):
    s=re.sub(r"\s+[—–]\s+",", ",s); return re.sub(r"(?<=\w)—(?=\w)",", ",s)
done=[]
for card in sorted(glob.glob(f"{K}/kb/cartoes_novos/*.md")):
    vid=os.path.basename(card)[:-3]; body=clean(open(card).read()).strip()
    if not re.match(rf"^## .*\(id: {re.escape(vid)}[,)]",body): print("formato inválido, pulei:",vid); continue
    files=glob.glob(f"{K}/kb/videos/{where[vid]:02d}_*.md")
    if len(files)!=1: print("arquivo do grupo não encontrado:",vid); continue
    f=files[0]; s=open(f).read()
    m=re.search(rf"^## .*\(id: {re.escape(vid)}[,)].*$",s,flags=re.M)
    if m:
        nxt=re.search(r"^## ",s[m.end():],flags=re.M); end=m.end()+nxt.start() if nxt else len(s)
        s=s[:m.start()]+body+"\n\n"+s[end:]; acao="substituído"
    else:
        anchor=re.search(r"^## O que este grupo revela",s,flags=re.M) or re.search(r"^## Sem transcrição",s,flags=re.M)
        pos=anchor.start() if anchor else len(s)
        s=s[:pos]+body+"\n\n"+s[pos:]; acao="inserido"
    sec=re.search(r"^## Sem transcrição.*?(?=^## |\Z)",s,flags=re.M|re.S)
    if sec:
        new=re.sub(rf"^.*{re.escape(vid)}.*$",f"- {vid}: agora tem cartão próprio neste arquivo, com a base indicada no cartão.",sec.group(0),flags=re.M)
        s=s[:sec.start()]+new+s[sec.end():]
    if not DRY: open(f,"w").write(s)
    done.append((vid,os.path.basename(f),acao))
print(("SIMULAÇÃO " if DRY else ""),done)
