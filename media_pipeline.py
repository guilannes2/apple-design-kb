import json, os, re, subprocess, time, glob, hashlib, sys, concurrent.futures as cf
from PIL import Image, ImageDraw, ImageFont
K=os.path.expanduser("~/Downloads/apple-design-kb")
SEC=sys.argv[1]; SALT=open(f"{SEC}/salt").read().strip()
ONLY=sys.argv[2].split(",") if len(sys.argv)>2 and sys.argv[2] else None
man={v["id"]:v for v in json.load(open(f"{K}/raw/video_manifest.json"))}
LOG=open(f"{K}/media_pipeline.log","a")
def log(s): LOG.write(time.strftime("%H:%M:%S ")+s+"\n"); LOG.flush()
def run(cmd): return subprocess.run(cmd,capture_output=True,text=True)
def fmt(t): t=int(t); return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}" if t>=3600 else f"{t//60:02d}:{t%60:02d}"
def done(vid): return os.path.exists(f"{K}/frames/{vid}/DONE.json")
def download(vid):
    v=man[vid]; out=f"{K}/media/{vid}.mp4"
    if done(vid): return vid,"já processado"
    if os.path.exists(out): return vid,"já baixado"
    try:
        if v.get("sd"):
            r=run(["curl","-sSL","--retry","5","--retry-delay","5","-o",out+".part",v["sd"].split("?")[0]])
            if r.returncode!=0: raise RuntimeError(r.stderr[-300:])
            os.rename(out+".part",out)
        elif v.get("m3u8"):
            tmp=f"{K}/media/{vid}.hls.mp4"
            r=run(["yt-dlp","-q","--no-warnings","--no-progress","-f","bv*[height<=720]+ba/b[height<=720]/bv*+ba/b","--merge-output-format","mp4","-o",tmp,v["m3u8"]])
            if r.returncode!=0 or not os.path.exists(tmp): raise RuntimeError(r.stderr[-400:])
            os.rename(tmp,out)
        else: return vid,"sem mídia"
        return vid,f"baixado {os.path.getsize(out)//1_000_000} MB"
    except Exception as e:
        log(f"DL FAIL {vid} {e}"); return vid,"FALHA"
SELECT="select='gt(isnan(prev_selected_t)+gte(t-prev_selected_t,12)+gt(scene,0.10)*gte(t-prev_selected_t,1.5),0)',showinfo"
def timed(vid, src, fd):
    p=f"{K}/text/timed/{vid}.json"
    if os.path.exists(p): return json.load(open(p))
    wav=f"{fd}/audio.wav"; run(["ffmpeg","-y","-loglevel","error","-i",src,"-vn","-ac","1","-ar","16000",wav])
    base=f"{K}/text/transcripts_whisper/{vid}"
    r=run(["whisper-cli","-m",os.path.expanduser("~/.whisper-models/ggml-large-v3-turbo.bin"),"-l","en","-t","2","-f",wav,"-oj","-otxt","-of",base,"-np"])
    os.remove(wav); log(f"WHISPER {vid} rc={r.returncode}")
    if not os.path.exists(base+".json"): return {"id":vid,"source":"none","segments":[]}
    j=json.load(open(base+".json"))
    segs=[{"t":s["offsets"]["from"]/1000,"text":s["text"].strip()} for s in j.get("transcription",[]) if s["text"].strip()]
    d={"id":vid,"source":"whisper-local-large-v3-turbo","segments":segs}; json.dump(d,open(p,"w"),ensure_ascii=False); return d
def process(vid):
    fd=f"{K}/frames/{vid}"; sd=f"{K}/sheets/{vid}"; src=f"{K}/media/{vid}.mp4"
    if done(vid): return vid,"já processado"
    if not os.path.exists(src): return vid,"sem arquivo"
    for d in (fd,sd):
        os.makedirs(d,exist_ok=True)
        for f in glob.glob(f"{d}/*"): os.remove(f)
    dur=float(run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",src]).stdout.strip() or 0)
    r=run(["ffmpeg","-hide_banner","-threads","2","-i",src,"-filter_threads","1","-vf","fps=4,scale=640:-2,"+SELECT,"-fps_mode","vfr","-q:v","4",f"{fd}/%06d.jpg"])
    frames=sorted(glob.glob(f"{fd}/*.jpg")); times=[float(x) for x in re.findall(r"pts_time:([\d.]+)",r.stderr)]
    if not frames or len(times)!=len(frames):
        log(f"FRAMES FAIL {vid} frames={len(frames)} times={len(times)} {r.stderr[-300:]}"); return vid,"FALHA quadros"
    tr=timed(vid,src,fd); segs=tr["segments"]
    try: font=ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf",22); big=ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf",30)
    except Exception: font=big=ImageFont.load_default()
    W,H,LAB,FOOT=640,360,30,48; codes={}; md=[f"# {vid}: {man[vid]['title']}",f"Duração: {fmt(dur)} | quadros: {len(frames)} | folhas: {(len(frames)+8)//9} | transcrição: {tr['source']}",""]
    starts=list(range(0,len(frames),9))
    for k,s in enumerate(starts):
        n=k+1; chunk=list(zip(frames[s:s+9],times[s:s+9]))
        code=hashlib.sha1(f"{SALT}|{vid}|{n}".encode()).hexdigest()[:5].upper(); codes[n]=code
        sheet=Image.new("RGB",(W*3,(H+LAB)*3+FOOT),(18,18,18)); d=ImageDraw.Draw(sheet)
        for i,(f,t) in enumerate(chunk):
            im=Image.open(f).convert("RGB"); im.thumbnail((W,H)); x=(i%3)*W; y=(i//3)*(H+LAB)
            sheet.paste(im,(x+(W-im.width)//2,y+LAB)); d.text((x+8,y+4),f"q{s+i+1:04d}  t={fmt(t)}",fill=(255,210,0),font=font)
        d.text((12,(H+LAB)*3+8),f"{vid}  folha {n:04d}/{len(starts):04d}",fill=(200,200,200),font=big)
        d.text((W*3-360,(H+LAB)*3+8),f"CÓDIGO {code}",fill=(120,255,160),font=big)
        sheet.save(f"{sd}/{n:04d}.jpg",quality=85)
        t0=chunk[0][1]; t1=times[s+9] if s+9<len(times) else dur+1
        spoken=" ".join(x["text"] for x in segs if t0<=x["t"]<t1) if segs else ""
        if k==0 and segs: spoken=" ".join(x["text"] for x in segs if x["t"]<t1)
        md.append(f"## Folha {n:04d} ({fmt(t0)} a {fmt(min(t1,dur))})"); md.append(spoken or "(sem fala neste intervalo)"); md.append("")
    open(f"{sd}/fala_por_folha.md","w").write("\n".join(md))
    allc=json.load(open(f"{SEC}/codes.json")) if os.path.exists(f"{SEC}/codes.json") else {}
    allc[vid]=codes; json.dump(allc,open(f"{SEC}/codes.json.tmp","w")); os.replace(f"{SEC}/codes.json.tmp",f"{SEC}/codes.json")
    info={"id":vid,"title":man[vid]["title"],"duration_s":round(dur),"frames":len(frames),"sheets":len(starts),"transcript":tr["source"],"transcript_segments":len(segs)}
    for f in frames: os.remove(f)
    os.remove(src)
    json.dump(info,open(f"{fd}/DONE.json","w"))
    return vid,f"{len(frames)} quadros, {len(starts)} folhas, vídeo apagado"
ids=[i for i,v in man.items() if (v.get("sd") or v.get("m3u8")) and (ONLY is None or i in ONLY)]
log(f"INÍCIO {len(ids)} vídeos")
import threading; lock=threading.Lock()
with cf.ThreadPoolExecutor(2) as dl, cf.ThreadPoolExecutor(1) as pr:
    futs=[]
    for f in cf.as_completed([dl.submit(download,i) for i in ids]):
        vid,msg=f.result(); log(f"DL {vid}: {msg}")
        if msg not in ("FALHA","sem mídia"): futs.append(pr.submit(process,vid))
    for f in cf.as_completed(futs):
        vid,msg=f.result(); log(f"PROC {vid}: {msg}")
infos=[json.load(open(p)) for p in glob.glob(f"{K}/frames/*/DONE.json")]
json.dump(sorted(infos,key=lambda x:x["id"]),open(f"{K}/sheets/manifest.json","w"),ensure_ascii=False,indent=1)
s=f"processados {len(infos)} de {len(man)} | quadros {sum(i['frames'] for i in infos)} | folhas {sum(i['sheets'] for i in infos)} | horas {round(sum(i['duration_s'] for i in infos)/3600,1)}"
log("FIM "+s); print(s)
