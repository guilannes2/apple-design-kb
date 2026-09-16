import glob, html, json, os, re
K=os.path.expanduser("~/Downloads/apple-design-kb")
vi={v["id"]:v for v in json.load(open(f"{K}/text/video_index.json"))}
n_ok=0; tot=0; empty=[]
for f in sorted(glob.glob(f"{K}/raw/videos/*.html")):
    vid=os.path.basename(f)[:-5]; h=open(f,encoding="utf-8").read()
    i=h.find('id="transcript-content"')
    if i<0: empty.append(vid); continue
    j=h.find("</section>",i); seg=h[i:j]
    items=[]
    for t,txt in re.findall(r'data-start="([\d.]+)">(.*?)</span>',seg,flags=re.S):
        s=html.unescape(re.sub(r"<[^>]+>"," ",txt)); s=re.sub(r"\s+"," ",s).strip()
        if s: items.append({"t":float(t),"text":s})
    if not items: empty.append(vid); continue
    json.dump({"id":vid,"source":"apple-transcript","segments":items},open(f"{K}/text/timed/{vid}.json","w"),ensure_ascii=False)
    n_ok+=1; tot+=sum(len(x["text"]) for x in items)
print("com tempo:",n_ok,"| chars:",tot,"| sem transcrição com tempo:",len(empty))
print("sem:",empty)
