import json, os, re, time, urllib.request, html
K=os.path.expanduser("~/Downloads/apple-design-kb"); UA={"User-Agent":"Mozilla/5.0 (Macintosh) research crawler for internal design notes"}
def get(url, method="GET"):
    req=urllib.request.Request(url, headers=UA, method=method)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read() if method=="GET" else dict(r.headers)
def save(p, b):
    with open(p,"wb") as f: f.write(b)
log=open(f"{K}/crawl.log","a")
# 1. HIG pages as DocC JSON
paths=json.load(open(f"{K}/raw/hig_paths.json"))
for p in paths:
    slug=p.rstrip("/").split("/")[-1]; out=f"{K}/raw/hig/{slug}.json"
    if os.path.exists(out): continue
    try: save(out, get("https://developer.apple.com/tutorials/data"+p.rstrip("/")+".json")); log.write(f"HIG ok {slug}\n")
    except Exception as e: log.write(f"HIG FAIL {slug} {e}\n")
    time.sleep(0.4)
# 2. Other design pages
for p in ["/design/","/design/get-started/","/design/whats-new/","/design/resources/","/design/awards/"]:
    name=p.strip("/").replace("/","_") or "design"; out=f"{K}/raw/pages/{name}.html"
    if os.path.exists(out): continue
    try: save(out, get("https://developer.apple.com"+p)); log.write(f"PAGE ok {p}\n")
    except Exception as e: log.write(f"PAGE FAIL {p} {e}\n")
    time.sleep(0.4)
# 3. Video pages: html, media links, sizes
manifest=[]
for u in json.load(open(f"{K}/raw/video_urls.json")):
    vid=u.strip("/").replace("videos/play/","").replace("/","_"); out=f"{K}/raw/videos/{vid}.html"
    try:
        if not os.path.exists(out): save(out, get("https://developer.apple.com"+u)); time.sleep(0.4)
        h=open(out,encoding="utf-8",errors="ignore").read()
        title=html.unescape((re.search(r"<title>(.*?)</title>",h,re.S) or [None,""])[1]).split(" - ")[0].strip()
        sd=(re.findall(r'https://[^"\']+_sd\.mp4[^"\']*',h) or [None])[0]
        hd=(re.findall(r'https://[^"\']+_hd\.mp4[^"\']*',h) or [None])[0]
        m3u8=(re.findall(r'https://[^"\']+\.m3u8',h) or [None])[0]
        size=None
        if sd:
            try: size=int(get(sd.split("?")[0],"HEAD").get("Content-Length",0))
            except Exception as e: log.write(f"HEAD FAIL {vid} {e}\n")
        manifest.append({"id":vid,"url":"https://developer.apple.com"+u,"title":title,"sd":sd,"hd":hd,"m3u8":m3u8,"sd_bytes":size,"html_bytes":len(h)})
        log.write(f"VID ok {vid}\n")
    except Exception as e:
        manifest.append({"id":vid,"url":"https://developer.apple.com"+u,"error":str(e)}); log.write(f"VID FAIL {vid} {e}\n")
json.dump(manifest,open(f"{K}/raw/video_manifest.json","w"),indent=1)
print("HIG json:",len(os.listdir(f"{K}/raw/hig")),"| pages:",len(os.listdir(f"{K}/raw/pages")),"| video pages:",len(manifest),"| com mp4 SD:",sum(1 for m in manifest if m.get("sd")),"| SD total GB:",round(sum(m.get("sd_bytes") or 0 for m in manifest)/1e9,2))
