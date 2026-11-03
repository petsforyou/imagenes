#!/usr/bin/env python3
"""Genera los archivos COMPLEMENTARIOS de Pinterest para Petsforyou (3/11/2026).

Pinterest ya tiene una fuente principal creada por la app de Shopify ("Shopify (ES, es)": España,
español; id de artículo = id de variante). Este script crea dos archivos que se dan de alta como
fuentes complementarias de esa principal:

  pinterest-paises.csv   id,override,price,availability,link     (una fila por variante y país)
  pinterest-idiomas.csv  id,override,title,description          (una fila por variante e idioma)

Reparto (María, 3/11/2026): español para España (principal) y América Latina; inglés para el resto,
incluida la UE salvo España. Entran TODOS los productos activos. Los que solo se envían a España y la
UE (no salen en /collections/all?country=US) llevan, FUERA de la UE: aviso de envío en la descripción
(en el idioma del catálogo) y un enlace a la página «aviso-envio-solo-ue-ada», que dice que ese
producto no se envía allí y lleva a los productos que sí se envían (decisión de María: nada de agotado).

Solo lee la web pública (sin claves). La web limita el ritmo: el script espera entre peticiones.

Uso:  python generar_pinterest.py [--salida carpeta] [--max N] [--sin-gz]
"""
import argparse, csv, gzip, html, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

BASE = "https://www.petsforyou.es"
UA = {"User-Agent": "Mozilla/5.0 (pinterest-feed-petsforyou)"}
PAUSA = 1.5
PAGINA_AVISO = "aviso-envio-solo-ue-ada"

# Países: América Latina = mercado «América Latina» de Shopify (27); UE = 26 (sin España);
# RESTO = primera lista de países con compras en Pinterest/Shopify; se amplía editando esta lista.
LATAM_ES = ["AG", "AR", "BZ", "BM", "BR", "CL", "CR", "DM", "EC", "SV", "HN", "JM", "NI", "PA", "PY", "PE",
            "TT", "DO", "GT", "GP", "GF", "CW", "BO", "MX", "CO", "UY", "VE"]
UE_EN = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT",
         "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "SE"]
RESTO_EN = ["GB", "US", "CA", "AU", "NZ", "CH", "NO", "IS", "IL", "JP", "KR", "IN", "SG", "MY", "TH", "VN",
            "PH", "ID", "HK", "TW", "AE", "SA", "TR", "ZA", "UA"]

AVISO = {
    "es-419": "Envío solo a España y la Unión Europea.",
    "en-US": "Ships to Spain and the EU only.",
}


def get(url, intentos=8):
    for i in range(intentos):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code in (429, 430, 503):
                time.sleep(8 * (i + 1))
                continue
            raise
        except Exception:
            time.sleep(4 * (i + 1))
    raise RuntimeError("no se pudo leer " + url)


def listar(ruta, pais, tope=None):
    """Todas las páginas de un products.json."""
    out, pagina = [], 1
    while True:
        d = json.loads(get(f"{BASE}{ruta}?limit=250&page={pagina}&country={pais}"))["products"]
        if not d:
            break
        out += d
        pagina += 1
        if tope and len(out) >= tope:
            break
        time.sleep(PAUSA)
    return out


def moneda(pais):
    h = get(f"{BASE}/en/products/cama-mullida-desenfundable-para-perros?country={pais}")
    m = re.search(r'Shopify\.currency\s*=\s*\{"active":"([A-Z]{3})"', h)
    return m.group(1) if m else "EUR"


def texto_plano(h):
    h = re.sub(r"<(br|/p|/li|/h\d)[^>]*>", " ", h or "", flags=re.I)
    h = re.sub(r"<[^>]+>", "", h)
    return re.sub(r"\s+", " ", html.unescape(h)).strip()[:9000]


def titulo(prod, v):
    return prod["title"] + ("" if v["title"] == "Default Title" else " - " + v["title"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=".")
    ap.add_argument("--max", type=int, default=0, help="solo los N primeros productos (pruebas)")
    ap.add_argument("--sin-gz", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.salida, exist_ok=True)

    paises = ([(p, "es-419") for p in LATAM_ES] + [(p, "en-GB") for p in UE_EN] + [(p, "en-US") for p in RESTO_EN])
    cache = os.path.join(a.salida, "monedas.json")
    monedas = json.load(open(cache)) if os.path.exists(cache) else {}
    for p, _ in paises:
        if p not in monedas:
            monedas[p] = moneda(p)
            time.sleep(PAUSA)
    json.dump(monedas, open(cache, "w"))
    print("monedas:", sorted(set(monedas.values())), file=sys.stderr)

    es = listar("/products.json", "ES", a.max)
    en = {p["id"]: p for p in listar("/en/products.json", "ES", a.max)}
    fuera = {p["handle"] for p in listar("/collections/all/products.json", "US")}
    if a.max:
        es = es[: a.max]
    print(f"productos: {len(es)}; los que salen de la UE: {len(fuera)}", file=sys.stderr)

    # Precios por moneda (la web da el precio de Shopify en la moneda del país)
    precios = {}
    for mon in sorted(set(monedas.values()) - {"EUR"}):
        pais = next(p for p, _ in paises if monedas[p] == mon)
        precios[mon] = {v["id"]: float(v["price"]) for pr in listar("/products.json", pais, a.max) for v in pr["variants"]}
    print("precios leídos para", sorted(precios), file=sys.stderr)

    h_p = open(os.path.join(a.salida, "pinterest-paises.csv"), "w", newline="", encoding="utf-8")
    h_i = open(os.path.join(a.salida, "pinterest-idiomas.csv"), "w", newline="", encoding="utf-8")
    fp = csv.writer(h_p, quoting=csv.QUOTE_ALL)
    fi = csv.writer(h_i, quoting=csv.QUOTE_ALL)
    fp.writerow(["id", "override", "price", "availability", "link"])
    fi.writerow(["id", "override", "title", "description"])
    nfp = nfi = nsolo = 0
    for pr in es:
        pe = en.get(pr["id"], pr)
        ve_by = {v["id"]: v for v in pe["variants"]}
        solo = pr["handle"] not in fuera
        d_es, d_en = texto_plano(pr["body_html"]), texto_plano(pe["body_html"])
        if solo:
            nsolo += 1
        for v in pr["variants"]:
            vid = v["id"]
            t_es, t_en = titulo(pr, v), titulo(pe, ve_by.get(vid, v))
            for loc, t, d, av in (("es-419", t_es, d_es, solo), ("en-GB", t_en, d_en, False), ("en-US", t_en, d_en, solo)):
                fi.writerow([vid, loc, t, (AVISO[loc] + " " + d) if av else d])
                nfi += 1
            eur = float(v["price"])
            disp = "in stock" if v.get("available", True) else "out of stock"
            for pais, loc in paises:
                fuera_ue = loc != "en-GB"
                if solo and fuera_ue:
                    # producto que no se envía allí: precio en euros y enlace a la página de aviso
                    t = t_es if loc == "es-419" else t_en
                    pre = "" if loc == "es-419" else "/en"
                    link = f"{BASE}{pre}/pages/{PAGINA_AVISO}?producto=" + urllib.parse.quote(t[:80])
                    precio = f"{eur:.2f} EUR"
                else:
                    mon = monedas[pais]
                    val = precios[mon].get(vid, eur) if mon != "EUR" else eur
                    precio = f"{val:.2f} {mon}"
                    link = "" if loc == "es-419" else f"{BASE}/en/products/{pr['handle']}?variant={vid}"
                fp.writerow([vid, pais, precio, disp, link])
                nfp += 1
    h_p.close()
    h_i.close()
    print(f"filas países: {nfp}; filas idiomas: {nfi}; productos solo UE: {nsolo}", file=sys.stderr)

    if not a.sin_gz:
        for nombre in ("pinterest-paises.csv", "pinterest-idiomas.csv"):
            ruta = os.path.join(a.salida, nombre)
            with open(ruta, "rb") as f, gzip.open(ruta + ".gz", "wb", 9) as g:
                g.write(f.read())
            print(nombre, os.path.getsize(ruta), "->", os.path.getsize(ruta + ".gz"), "bytes gz", file=sys.stderr)


if __name__ == "__main__":
    main()
