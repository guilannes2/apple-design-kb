# Apaga a mídia e os quadros depois que a base está fechada, mantendo textos, notas, logs e verificações.
# Uso: python limpeza_final.py --dry  (só mostra)  |  python limpeza_final.py --apagar
import os, sys, shutil, glob
K=os.path.expanduser("~/Downloads/apple-design-kb")
ALVOS=["media","media_hig","sheets","sheets_hig","frames"]
MANTER=["kb","text","raw","groups.json"]
def tamanho(p):
    t=0
    for r,_,fs in os.walk(p):
        for f in fs:
            try: t+=os.path.getsize(os.path.join(r,f))
            except OSError: pass
    return t
def main():
    if "--apagar" not in sys.argv and "--dry" not in sys.argv:
        print("use --dry ou --apagar"); return
    total=0; linhas=[]
    for a in ALVOS:
        p=f"{K}/{a}"
        if not os.path.isdir(p): continue
        t=tamanho(p); n=sum(len(fs) for _,_,fs in os.walk(p)); total+=t
        linhas.append(f"{a}: {n} arquivos, {t/1e9:.2f} GB")
    # os marcadores DONE.json de cada vídeo ficam registrados antes de apagar
    dones=glob.glob(f"{K}/frames/*/DONE.json")
    if dones:
        import json
        reg=[json.load(open(p)) for p in dones]
        json.dump(sorted(reg,key=lambda x:x["id"]),open(f"{K}/raw/frames_processados.json","w"),ensure_ascii=False,indent=1)
        linhas.append(f"registro de {len(reg)} vídeos processados salvo em raw/frames_processados.json")
    print("\n".join(linhas)); print(f"total a liberar: {total/1e9:.2f} GB")
    if "--apagar" in sys.argv:
        for a in ALVOS:
            p=f"{K}/{a}"
            if os.path.isdir(p): shutil.rmtree(p)
        print("apagado. mantidos:", ", ".join(MANTER))
main()
