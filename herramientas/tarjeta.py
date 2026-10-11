"""Tarjeta 1080x1350 con el estilo de los carruseles de PetsForYou.

uso: python3 tarjeta.py salida.png foto.jpg "ANTETITULO" "Título" "Pie de foto" "1/5" ["crédito"]
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

FONDO = (245, 239, 230)
NARANJA = (200, 113, 63)
OSCURO = (40, 36, 33)
GRIS = (95, 88, 82)
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def partir(draw, texto, fuente, ancho):
    lineas, actual = [], ""
    for palabra in texto.split():
        prueba = (actual + " " + palabra).strip()
        if draw.textlength(prueba, font=fuente) <= ancho:
            actual = prueba
        else:
            lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas


def centrado(draw, y, lineas, fuente, color, salto):
    for l in lineas:
        w = draw.textlength(l, font=fuente)
        draw.text(((1080 - w) / 2, y), l, font=fuente, fill=color)
        y += salto
    return y


def main(salida, foto, ante, titulo, pie, pagina, credito=""):
    W, H = 1080, 1350
    im = Image.new("RGB", (W, H), FONDO)
    d = ImageDraw.Draw(im)
    y = 60
    if ante:
        f = ImageFont.truetype(BOLD, 34)
        y = centrado(d, y, [ante.upper()], f, NARANJA, 50)
    ft = ImageFont.truetype(BOLD, 58)
    y = centrado(d, y, partir(d, titulo, ft, 900), ft, OSCURO, 70) + 10
    d.rounded_rectangle((W / 2 - 40, y, W / 2 + 40, y + 6), 3, fill=NARANJA)
    y += 36
    fp = ImageFont.truetype(REG, 38)
    lineas_pie = partir(d, pie, fp, 880) if pie else []
    alto_pie = len(lineas_pie) * 52
    alto_foto = H - y - alto_pie - 130
    ancho_foto = 900
    ph = ImageOps.fit(Image.open(foto).convert("RGB"), (ancho_foto, alto_foto), Image.LANCZOS)
    mask = Image.new("L", ph.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0) + ph.size, 36, fill=255)
    im.paste(ph, ((W - ancho_foto) // 2, y), mask)
    if credito:
        fc = ImageFont.truetype(REG, 24)
        w = d.textlength(credito, font=fc)
        x0, y0 = (W + ancho_foto) / 2 - w - 22, y + alto_foto - 44
        d.text((x0 + 1, y0 + 1), credito, font=fc, fill=(0, 0, 0))
        d.text((x0, y0), credito, font=fc, fill=(255, 255, 255))
    y += alto_foto + 40
    centrado(d, y, lineas_pie, fp, GRIS, 52)
    if pagina:
        fn = ImageFont.truetype(REG, 26)
        d.text((W - 110, H - 60), pagina, font=fn, fill=(160, 150, 140))
    im.save(salida)


if __name__ == "__main__":
    main(*sys.argv[1:])
