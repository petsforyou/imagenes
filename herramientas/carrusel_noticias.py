"""Carrusel de 5 láminas (1080x1350) para la sección «Noticias que cuentan».

Lámina 1: portada con el nombre de la sección y la semana. Láminas 2-4: una
noticia cada una (etiqueta, titular, qué cambia, por qué te importa, fuente).
Lámina 5: cierre. Lenguaje llano: frases cortas, sin jerga.

Requisitos: pip install pillow
Uso: python herramientas/carrusel_noticias.py guion.json  ->  <nombre>_1.png ... _5.png junto al guion

guion.json:
{
  "nombre": "noticias-que-cuentan-2026-10-20",
  "semana": "Semana del 12 al 18 de octubre",
  "portada": "Lo que cambia para ti y tu mascota",       (frase corta bajo el título)
  "noticias": [
    {"etiqueta": "NORMATIVA", "titulo": "...", "que": "Qué cambia, 2-3 frases llanas.",
     "importa": "Por qué te importa, 1-2 frases.", "fuente": "BOE, 14/10/2026"},
    ... (3 noticias)
  ],
  "cierre": "¿Te ha servido? Guárdalo y compártelo con quien tenga mascota."
}
"""
import json
import os
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
AZUL = (31, 58, 104)      # color de la sección (el mismo del calendario)
AZUL_CLARO = (226, 233, 244)
AMARILLO = (255, 216, 74)
TINTA = (24, 30, 40)
GRIS = (92, 102, 116)
FONDO = (250, 250, 247)


def fuente(negrita, size):
    for f in (("C:/Windows/Fonts/arialbd.ttf" if negrita else "C:/Windows/Fonts/arial.ttf"),
              ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if negrita
               else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")):
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    sys.exit("No encuentro una fuente: instala fonts-dejavu-core")


def parrafo(d, texto, x, y, size, ancho_px, color, negrita=False, interlineado=1.3):
    """Escribe el texto ajustado a ancho_px palabra a palabra; devuelve la y final."""
    f = fuente(negrita, size)
    linea = ""
    for p in texto.split():
        prueba = (linea + " " + p).strip()
        if linea and d.textlength(prueba, font=f) > ancho_px:
            d.text((x, y), linea, font=f, fill=color)
            y += size * interlineado
            linea = p
        else:
            linea = prueba
    if linea:
        d.text((x, y), linea, font=f, fill=color)
        y += size * interlineado
    return y


def pie(d, n, total, oscuro=False):
    f = fuente(True, 28)
    color = (255, 255, 255) if oscuro else GRIS
    d.text((70, H - 80), "PETSFORYOU", font=f, fill=color)
    t = f"{n}/{total}"
    d.text((W - 70 - d.textlength(t, font=f), H - 80), t, font=f, fill=color)


def portada(g, salida):
    img = Image.new("RGB", (W, H), AZUL)
    d = ImageDraw.Draw(img)
    f = fuente(True, 132)
    y = 300
    for ln in ("NOTICIAS", "QUE", "CUENTAN"):
        d.text((70, y), ln, font=f, fill=(255, 255, 255))
        y += 145
    d.rounded_rectangle([70, y + 30, 400, y + 52], radius=11, fill=AMARILLO)
    y = parrafo(d, g.get("portada", "Lo que cambia para ti y tu mascota"), 70, y + 100, 48, W - 140,
                (255, 255, 255), negrita=True)
    parrafo(d, g["semana"], 70, y + 30, 36, W - 140, AZUL_CLARO)
    pie(d, 1, 5, oscuro=True)
    img.save(salida)


def lamina(nt, n, salida):
    img = Image.new("RGB", (W, H), FONDO)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 150], fill=AZUL)
    f = fuente(True, 34)
    d.text((70, 58), "NOTICIAS QUE CUENTAN", font=f, fill=(255, 255, 255))
    et = nt["etiqueta"].upper()
    fe = fuente(True, 30)
    w = d.textlength(et, font=fe)
    d.rounded_rectangle([70, 200, 70 + w + 44, 256], radius=28, fill=AMARILLO)
    d.text((92, 211), et, font=fe, fill=TINTA)
    y = parrafo(d, nt["titulo"], 70, 300, 58, W - 140, TINTA, negrita=True, interlineado=1.18)
    y += 30
    d.text((70, y), "QUÉ CAMBIA", font=fuente(True, 28), fill=AZUL)
    y = parrafo(d, nt["que"], 70, y + 44, 38, W - 140, TINTA)
    y += 30
    caja_y = y
    y2 = parrafo(ImageDraw.Draw(Image.new("RGB", (W, H))), nt["importa"], 100, caja_y + 70, 36, W - 200, TINTA)
    d.rounded_rectangle([70, caja_y, W - 70, y2 + 30], radius=18, fill=AZUL_CLARO)
    d.text((100, caja_y + 26), "POR QUÉ TE IMPORTA", font=fuente(True, 28), fill=AZUL)
    parrafo(d, nt["importa"], 100, caja_y + 70, 36, W - 200, TINTA)
    parrafo(d, "Fuente: " + nt["fuente"], 70, H - 150, 28, W - 140, GRIS)
    pie(d, n, 5)
    img.save(salida)


def cierre(g, salida):
    img = Image.new("RGB", (W, H), AZUL)
    d = ImageDraw.Draw(img)
    y = parrafo(d, g.get("cierre", "¿Te ha servido? Guárdalo y compártelo con quien tenga mascota."),
                70, 420, 64, W - 140, (255, 255, 255), negrita=True, interlineado=1.2)
    d.rounded_rectangle([70, y + 40, 400, y + 62], radius=11, fill=AMARILLO)
    parrafo(d, "Cada semana, las noticias que de verdad te afectan, contadas claras.", 70, y + 110, 40,
            W - 140, AZUL_CLARO)
    d.text((70, H - 220), "petsforyou.es", font=fuente(True, 48), fill=AMARILLO)
    pie(d, 5, 5, oscuro=True)
    img.save(salida)


def main(guion_path):
    g = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    base = Path(guion_path).parent
    if len(g["noticias"]) != 3:
        sys.exit("El carrusel lleva exactamente 3 noticias")
    salidas = [base / f"{g['nombre']}_{i}.png" for i in range(1, 6)]
    portada(g, salidas[0])
    for i, nt in enumerate(g["noticias"]):
        lamina(nt, i + 2, salidas[i + 1])
    cierre(g, salidas[4])
    for s in salidas:
        print(s)


if __name__ == "__main__":
    main(sys.argv[1])
