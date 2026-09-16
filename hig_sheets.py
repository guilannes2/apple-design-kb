# Folhas das ilustrações e vídeos do HIG, com código carimbado e contexto por folha. Códigos em codes_hig.json (arquivo próprio).
import json, os, glob, hashlib, subprocess, re, sys
from PIL import Image, ImageDraw, ImageFont
K=os.path.expanduser("~/Downloads/apple-design-kb"); SEC=sys.argv[1]; SALT=open(f"{SEC}/salt").read().strip()
man=json.load(open(f"{K}/raw/hig_media_manifest.json"))
OUT=f"{K}/sheets_hig"; os.makedirs(OUT,exist_ok=True)
F=lambda s: ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf",s)
font,big=F(20),F(30)
codes={}; units=[]; skipped=[]
def code(unit,n): return hashlib.sha1(f"{SALT}|{unit}|{n}".encode()).hexdigest()[:5].upper()
def short(s,n): s=re.sub(r"\s+"," ",s or "").strip(); return s if len(s)<=n else s[:n-1]+"…"
# ilustrações: 2 por 2 por folha, na ordem da página; versão escura ocupa a célula ao lado da clara
pages={}
for i,o in enumerate(man["images"]):
    for kind in ("light","dark"):
        f=o.get(f"file_{kind}")
        if f and os.path.exists(f"{K}/{f}"): pages.setdefault(o["page"],[]).append((i,kind,o))
CW,CH,LAB,FOOT=960,620,34,50
for page,cells in pages.items():
    unit=f"hig-img_{page}"; d=f"{OUT}/{unit}"; os.makedirs(d,exist_ok=True)
    for x in glob.glob(f"{d}/*"): os.remove(x)
    md=[f"# {unit}: ilustrações da página {page} do HIG",""]; n=0; ok_cells=[]
    for c in cells:
        fp=f"{K}/{c[2]['file_'+c[1]]}"
        if fp.endswith(".svg"):
            png=fp[:-4]+".png"
            if not os.path.exists(png):
                subprocess.run(["qlmanage","-t","-s","512","-o",os.path.dirname(fp),fp],capture_output=True)
                if os.path.exists(fp+".png"): os.rename(fp+".png",png)
            if os.path.exists(png): c[2]["file_"+c[1]]=c[2]["file_"+c[1]][:-4]+".png"
        try: Image.open(f"{K}/{c[2]['file_'+c[1]]}").verify(); ok_cells.append(c)
        except Exception as e: skipped.append(f"{c[2]['file_'+c[1]]}: {e}")
    for s in range(0,len(ok_cells),4):
        n+=1; cc=code(unit,n); codes.setdefault(unit,{})[str(n)]=cc
        sheet=Image.new("RGB",(CW*2,(CH+LAB)*2+FOOT),(40,40,40)); dr=ImageDraw.Draw(sheet)
        md.append(f"## Folha {n:04d}")
        for k,(i,kind,o) in enumerate(ok_cells[s:s+4]):
            im=Image.open(f"{K}/{o['file_'+kind]}")
            bg=(255,255,255) if kind=="light" else (0,0,0)
            if im.mode in ("RGBA","LA","P"):
                im=im.convert("RGBA"); base=Image.new("RGB",im.size,bg); base.paste(im,mask=im.split()[-1]); im=base
            else: im=im.convert("RGB")
            im.thumbnail((CW-8,CH-8)); x=(k%2)*CW; y=(k//2)*(CH+LAB)
            dr.rectangle([x+2,y+LAB,x+CW-3,y+LAB+CH-3],fill=bg)
            sheet.paste(im,(x+(CW-im.width)//2,y+LAB+(CH-im.height)//2))
            dr.text((x+8,y+6),short(f"img {i:04d} {'escura' if kind=='dark' else 'clara'} · {o['heading']}",78),fill=(255,210,0),font=font)
            md.append(f"- img {i:04d} ({'versão escura' if kind=='dark' else 'versão clara'}). Seção: {o['heading']}. Texto antes: {short(o['before'],260)} Legenda: {short(o['caption'],260) or '(sem legenda)'} Alt: {short(o['alt'],400) or '(sem alt)'}")
        dr.text((12,(CH+LAB)*2+10),f"{unit}  folha {n:04d}",fill=(200,200,200),font=big)
        dr.text((CW*2-360,(CH+LAB)*2+10),f"CÓDIGO {cc}",fill=(120,255,160),font=big)
        sheet.save(f"{d}/{n:04d}.jpg",quality=88); md.append("")
    if n:
        md.insert(1,f"Folhas: {n}"); open(f"{d}/contexto_por_folha.md","w").write("\n".join(md))
        units.append({"id":unit,"kind":"hig-imagens","page":page,"sheets":n,"title":f"Ilustrações do HIG: {page}"})
# vídeos do HIG: 2 quadros por segundo sem repetição, no máximo 36 quadros, 3 por 3
W,H,L2=640,400,30
for o in man["videos"]:
    f=o.get("file")
    if not f or not os.path.exists(f"{K}/{f}"): skipped.append(f"video ausente {o.get('id')}"); continue
    unit="hig-vid_"+os.path.basename(f)[:-4]; d=f"{OUT}/{unit}"; os.makedirs(d,exist_ok=True)
    for x in glob.glob(f"{d}/*"): os.remove(x)
    r=subprocess.run(["ffmpeg","-hide_banner","-i",f"{K}/{f}","-vf","fps=2,mpdecimate,scale=640:-2,showinfo","-fps_mode","vfr","-q:v","3",f"{d}/f%05d.jpg"],capture_output=True,text=True)
    fr=sorted(glob.glob(f"{d}/f*.jpg")); ts=[float(t) for t in re.findall(r"pts_time:([\d.]+)",r.stderr)]
    if not fr or len(fr)!=len(ts): skipped.append(f"quadros falharam {unit}"); continue
    idx=list(range(len(fr)))
    if len(idx)>36: idx=[round(j*(len(fr)-1)/35) for j in range(36)]
    sel=[(fr[j],ts[j],j+1) for j in idx]
    md=[f"# {unit}: vídeo da página {o['page']} do HIG",f"Seção: {o['heading']}. Texto antes: {short(o['before'],300)}",f"Alt do vídeo (descrição oficial): {short(o['alt'],900)}",f"Quadros distintos: {len(fr)}, nas folhas: {len(sel)}",""]
    n=0
    for s in range(0,len(sel),9):
        n+=1; cc=code(unit,n); codes.setdefault(unit,{})[str(n)]=cc
        sheet=Image.new("RGB",(W*3,(H+L2)*3+FOOT),(18,18,18)); dr=ImageDraw.Draw(sheet)
        for k,(p,t,q) in enumerate(sel[s:s+9]):
            im=Image.open(p).convert("RGB"); im.thumbnail((W,H)); x=(k%3)*W; y=(k//3)*(H+L2)
            sheet.paste(im,(x+(W-im.width)//2,y+L2)); dr.text((x+8,y+4),f"q{q:03d} t={t:.1f}s",fill=(255,210,0),font=font)
        dr.text((12,(H+L2)*3+10),f"{unit[:48]}  folha {n:04d}",fill=(200,200,200),font=big)
        dr.text((W*3-360,(H+L2)*3+10),f"CÓDIGO {cc}",fill=(120,255,160),font=big)
        sheet.save(f"{d}/{n:04d}.jpg",quality=88); md.append(f"## Folha {n:04d}"); md.append("")
    for p in fr: os.remove(p)
    open(f"{d}/contexto_por_folha.md","w").write("\n".join(md))
    units.append({"id":unit,"kind":"hig-video","page":o["page"],"sheets":n,"title":f"Vídeo do HIG: {o['page']} ({o['id']})"})
json.dump(codes,open(f"{SEC}/codes_hig.json","w"))
json.dump(units,open(f"{OUT}/manifest.json","w"),ensure_ascii=False,indent=1)
print(f"unidades {len(units)} | folhas {sum(u['sheets'] for u in units)} | imagens: {sum(u['sheets'] for u in units if u['kind']=='hig-imagens')} folhas | vídeos: {sum(1 for u in units if u['kind']=='hig-video')} | puladas {len(skipped)}")
print("\n".join(skipped[:15]))
