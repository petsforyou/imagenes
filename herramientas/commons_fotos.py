"""Baja de Wikimedia Commons (CC0/PD/CC-BY/CC-BY-SA) los archivos de una categoría o búsqueda y hace hoja de contactos.
Uso: python commons_fotos.py carpeta tag "cat:Category:Lynx pardinus" | "q:Iberian lynx cub" [max]"""
import sys,json,urllib.request,urllib.parse,io,os,re,time
from PIL import Image,ImageDraw
d,tag,spec=sys.argv[1:4];mx=int(sys.argv[4]) if len(sys.argv)>4 else 40
os.makedirs(d+"/cand",exist_ok=True)
H={"User-Agent":"petsforyou-bot/1.0 (contacto@petsforyou.es)"}
def api(**p):
    p.update(format="json",action="query")
    return json.load(urllib.request.urlopen(urllib.request.Request("https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(p),headers=H),timeout=30))
kind,val=spec.split(":",1)
g=dict(generator="categorymembers",gcmtitle=val,gcmtype="file",gcmlimit=mx) if kind=="cat" else dict(generator="search",gsrsearch=val,gsrnamespace=6,gsrlimit=mx)
r=api(prop="imageinfo",iiprop="url|extmetadata|size",iiurlwidth=900,**g)
mp=os.path.join(d,"cand","meta.json");meta=json.load(open(mp)) if os.path.exists(mp) else {}
n=0
for p in r.get("query",{}).get("pages",{}).values():
    ii=p["imageinfo"][0];em=ii["extmetadata"];lic=em.get("LicenseShortName",{}).get("value","")
    if not re.search(r"CC0|Public domain|CC BY|PD",lic,re.I) or re.search(r"NC|ND",lic):continue
    if not ii.get("thumburl") or not re.search(r"\.(jpe?g|png)(\?|$)",ii["url"],re.I):continue
    k=f"{tag}{n}"
    try:
        im=Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(ii["thumburl"],headers=H),timeout=30).read())).convert("RGB");time.sleep(0.5)
    except Exception as e:continue
    im.save(f"{d}/cand/{k}.jpg",quality=90)
    au=re.sub("<[^>]+>","",em.get("Artist",{}).get("value",""))
    meta[k]={"creator":au,"license":lic,"title":p["title"],"page":ii["descriptionurl"]};n+=1
json.dump(meta,open(mp,"w",encoding="utf8"),ensure_ascii=False,indent=1)
kk=[k for k in meta if k.startswith(tag) and k[len(tag):].isdigit()]
for s in range(0,len(kk),12):
    S=Image.new("RGB",(6*260,2*300),"white");dr=ImageDraw.Draw(S)
    for i,k in enumerate(kk[s:s+12]):
        im=Image.open(f"{d}/cand/{k}.jpg");im.thumbnail((250,270));x,y=(i%6)*260,(i//6)*300;S.paste(im,(x,y));dr.text((x+4,y+278),k,fill="black")
    S.save(f"{d}/cand/csheet_{tag}_{s//12}.jpg")
print(tag,n)
