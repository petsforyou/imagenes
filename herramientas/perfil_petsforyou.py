"""Piezas fijas del perfil de Instagram (17-10-2026).

- Carrusel «Así es Petsforyou» (5 láminas 1080x1350) para fijar en el perfil.
- 5 historias 1080x1920 que sirven de portada de los destacados
  (Envíos, Familia, Historias, Consejos, Tienda): círculo de color con la
  palabra en el centro, para que la portada del destacado se vea igual en todos.

Uso: python herramientas/perfil_petsforyou.py  ->  perfil/*.png
"""
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "perfil"
OUT.mkdir(exist_ok=True)

VERDE = (11, 138, 123)
CREMA = (247, 243, 236)
TINTA = (27, 34, 48)
AMARILLO = (255, 216, 74)
BLANCO = (255, 255, 255)


def f(negrita, size):
    for p in (("C:/Windows/Fonts/arialbd.ttf" if negrita else "C:/Windows/Fonts/arial.ttf"),
              ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if negrita
               else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)


def texto(d, s, x, y, size, ancho, color, negrita=False, centro=False, inter=1.25):
    fu = f(negrita, size)
    lineas, linea = [], ""
    for p in s.split():
        prueba = (linea + " " + p).strip()
        if linea and d.textlength(prueba, font=fu) > ancho:
            lineas.append(linea)
            linea = p
        else:
            linea = prueba
    if linea:
        lineas.append(linea)
    for ln in lineas:
        xx = x + (ancho - d.textlength(ln, font=fu)) / 2 if centro else x
        d.text((xx, y), ln, font=fu, fill=color)
        y += size * inter
    return y


def foto(ruta, w, h):
    return ImageOps.fit(Image.open(BASE / "fotos" / ruta).convert("RGB"), (w, h), centering=(0.5, 0.45))


def pie(d, n):
    fu = f(True, 26)
    d.text((70, 1350 - 70), "PETSFORYOU", font=fu, fill=GRIS)
    t = f"{n}/5"
    d.text((1080 - 70 - d.textlength(t, font=fu), 1350 - 70), t, font=fu, fill=GRIS)


GRIS = (110, 118, 128)
W, H = 1080, 1350


def lamina_foto(ruta, titulo, cuerpo, n, nombre, etiqueta=None):
    img = Image.new("RGB", (W, H), CREMA)
    img.paste(foto(ruta, W, 760), (0, 0))
    d = ImageDraw.Draw(img)
    if etiqueta:
        fe = f(True, 30)
        w = d.textlength(etiqueta, font=fe)
        d.rounded_rectangle([70, 690, 70 + w + 44, 744], radius=27, fill=AMARILLO)
        d.text((92, 700), etiqueta, font=fe, fill=TINTA)
    y = texto(d, titulo, 70, 800, 62, W - 140, TINTA, negrita=True, inter=1.15)
    texto(d, cuerpo, 70, y + 24, 38, W - 140, TINTA)
    pie(d, n)
    img.save(OUT / nombre)


def lamina_lista(n, nombre):
    img = Image.new("RGB", (W, H), VERDE)
    d = ImageDraw.Draw(img)
    texto(d, "Qué vas a encontrar aquí", 70, 110, 66, W - 140, BLANCO, negrita=True, inter=1.15)
    items = [
        ("Historias de cuatro patas", "rescates y héroes reales, cada noche"),
        ("Curiosidades de nuestras mascotas", "un dato que no sabías, cada día"),
        ("Producto del día", "un consejo útil y lo que te ayuda"),
        ("Los animales, nuestros amigos", "noticias de todas las especies"),
        ("Noticias que cuentan", "normas y novedades, en lenguaje llano"),
        ("Ada y sus amigos", "nuestra serie, martes y viernes"),
    ]
    y = 330
    for t, s in items:
        d.ellipse([70, y + 14, 92, y + 36], fill=AMARILLO)
        d.text((120, y), t, font=f(True, 40), fill=BLANCO)
        d.text((120, y + 50), s, font=f(False, 32), fill=(214, 238, 234))
        y += 140
    pie(d, n)
    img.save(OUT / nombre)


def historia(palabra, frase, ruta, nombre):
    img = foto(ruta, 1080, 1920) if ruta else Image.new("RGB", (1080, 1920), CREMA)
    capa = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    if ruta:
        dc.rectangle([0, 0, 1080, 1920], fill=(0, 0, 0, 70))
    img = Image.alpha_composite(img.convert("RGBA"), capa).convert("RGB")
    d = ImageDraw.Draw(img)
    # Círculo central: es lo que Instagram usa como portada del destacado.
    r = 300
    cx, cy = 540, 860
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=VERDE, outline=BLANCO, width=10)
    fu = f(True, 84 if len(palabra) <= 8 else 70)
    w = d.textlength(palabra.upper(), font=fu)
    d.text((cx - w / 2, cy - 48), palabra.upper(), font=fu, fill=BLANCO)
    caja_y = 1290
    d.rounded_rectangle([90, caja_y, 990, caja_y + 300], radius=30, fill=(255, 255, 255, 235))
    texto(d, frase, 130, caja_y + 50, 46, 820, TINTA, negrita=True, centro=True)
    fp = f(True, 36)
    w = d.textlength("petsforyou.es", font=fp)
    d.text(((1080 - w) / 2, 1700), "petsforyou.es", font=fp, fill=BLANCO if ruta else VERDE)
    img.save(OUT / nombre)


if __name__ == "__main__":
    lamina_foto("cloe-3-mirada.jpg", "Así es Petsforyou",
                "Una tienda pequeña, hecha por gente que vive con animales. Desliza y te contamos quiénes somos.",
                1, "asi-es-1.png", etiqueta="HOLA 👋".replace(" 👋", ""))
    lamina_foto("familia-11-zara-mango.jpg", "Quiénes somos",
                "Somos María y nuestra familia de cuatro patas: Cloe, Zara, Mango y Maya. Desde Zamora, para toda España.",
                2, "asi-es-2.png", etiqueta="ZARA Y MANGO")
    lamina_lista(3, "asi-es-3.png")
    lamina_foto("familia-4-a-mis-pies.jpg", "Nuestra tienda",
                "Cosas para perros, gatos, conejos, hámsters, cobayas y hurones, elegidas pensando en su bienestar. Envío gratis a España y la UE.",
                4, "asi-es-4.png")
    lamina_foto("familia-6-regazo.jpg", "¿Y el tuyo, cómo es?",
                "Cuéntanoslo en comentarios y síguenos para no perderte nada. Te esperamos en petsforyou.es",
                5, "asi-es-5.png")
    historia("Envíos", "Envío gratis a España y la UE. El plazo de cada producto está en su ficha.",
             None, "hist-envios.png")
    historia("Familia", "Cloe, Zara, Mango y Maya: la familia que hay detrás de Petsforyou.",
             "familia-3-paseo.jpg", "hist-familia.png")
    historia("Historias", "Historias reales de animales que nos emocionan, cada noche.",
             "familia-13-husmeando.jpg", "hist-historias.png")
    historia("Consejos", "Curiosidades y consejos para cuidarlos mejor, cada día.",
             "cloe-22-rascador.jpg", "hist-consejos.png")
    historia("Tienda", "Camas, ropa, juguetes, paseo y más. Todo en petsforyou.es",
             "familia-6-regazo.jpg", "hist-tienda.png")
    print("ok")
