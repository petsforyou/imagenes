"""Busca fotos libres en Openverse (licencia comercial) y hace una hoja de contactos.
Uso: python buscar_fotos_libres.py carpeta "tag=consulta" "tag2=consulta2" ...  (cada una baja hasta 6 candidatas)"""
import sys,json,urllib.request,urllib.parse,io,os
from PIL import Image,ImageDraw
d=sys.argv[1];os.makedirs(d+"/cand",exist_ok=True)
meta=json.load(open(d+"/cand/meta.json",encoding="utf8")) if os.path.exists(d+"/cand/meta.json") else {}
for a in sys.argv[2:]:
    tag,q=a.split("=",1)
    u="https://api.openverse.org/v1/images/?"+urllib.parse.urlencode({"q":q,"license_type":"commercial","page_size":12})
    try: r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"pfy"}),timeout=30))
    except Exception as e: print(tag,"ERR",e);continue
    n=0
    for x in r["results"]:
        if n>=6:break
        if (x.get("width") or 9999)<600 and (x.get("height") or 9999)<600: continue
        k=f"{tag}{n}"
        try:
            b=urllib.request.urlopen(urllib.request.Request(x["url"],headers={"User-Agent":"pfy"}),timeout=30).read()
            im=Image.open(io.BytesIO(b)).convert("RGB")
        except Exception as e: continue
        im.save(f"{d}/cand/{k}.jpg",quality=90)
        meta[k]={"creator":x.get("creator"),"license":x["license"].upper()+" "+(x.get("license_version") or ""),"title":x["title"],"page":x.get("foreign_landing_url"),"src":x["url"]}
        n+=1
    print(tag,n)
json.dump(meta,open(d+"/cand/meta.json","w",encoding="utf8"),ensure_ascii=False,indent=1)
ks=[k for k in meta if os.path.exists(f"{d}/cand/{k}.jpg")]
tags=sorted({''.join(c for c in k if not c.isdigit()) for k in ks})
for t in tags:
    kk=[k for k in ks if ''.join(c for c in k if not c.isdigit())==t]
    S=Image.new("RGB",(6*260,300),"white");dr=ImageDraw.Draw(S)
    for i,k in enumerate(kk[:6]):
        im=Image.open(f"{d}/cand/{k}.jpg");im.thumbnail((250,270));S.paste(im,(i*260,0));dr.text((i*260+4,278),k,fill="black")
    S.save(f"{d}/cand/sheet_{t}.jpg")
