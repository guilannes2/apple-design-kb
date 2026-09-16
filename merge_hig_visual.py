# Insere, no fim de cada artigo de kb/hig, a síntese visual verificada da página (idempotente, entre marcadores).
import os, re, glob
K=os.path.expanduser("~/Downloads/apple-design-kb")
def clean(s):
    s=re.sub(r"\s+[—–]\s+",", ",s); return re.sub(r"(?<=\w)—(?=\w)",", ",s)
ins=pend=semvis=0
for f in sorted(glob.glob(f"{K}/kb/hig/*.md")):
    s=open(f).read()
    s=re.sub(r"\n*<!-- visual:[a-z0-9-]+ -->.*?<!-- /visual:[a-z0-9-]+ -->\n*","\n\n",s,flags=re.S)
    heads=list(re.finditer(r"^## .*\(slug: ([a-z0-9-]+)\)\s*$",s,flags=re.M))
    for m in reversed(heads):
        slug=m.group(1)
        nxt=re.search(r"^## ",s[m.end():],flags=re.M)
        end=m.end()+nxt.start() if nxt else len(s)
        syn=f"{K}/kb/visual_sintese_hig/{slug}.md"
        if os.path.exists(syn):
            body=clean(open(syn).read()).strip(); ins+=1
        elif os.path.exists(f"{K}/kb/visual_hig/{slug}.md"):
            body="### O que as ilustrações mostram\n\nSíntese visual pendente."; pend+=1
        else:
            body="### O que as ilustrações mostram\n\nA página não tem ilustrações nem vídeos no próprio conteúdo."; semvis+=1
        block=f"\n\n<!-- visual:{slug} -->\n{body}\n<!-- /visual:{slug} -->\n\n"
        s=s[:end].rstrip()+block+s[end:].lstrip("\n")
    open(f,"w").write(s)
print(f"sínteses inseridas {ins} | pendentes {pend} | páginas sem visual {semvis}")
