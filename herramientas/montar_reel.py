"""Monta un reel vertical 1080x1920 a pantalla completa a partir de fotos.

Formato de redes de Petsforyou desde el 16/10/2026 (sustituye a la tarjeta
blanca de tarjeta.py): cada foto ocupa toda la pantalla con un zoom lento, pasa
a la siguiente con un fundido y lleva su frase en subtítulos grandes abajo. Si el guion
tiene "seccion", la primera escena lleva arriba la etiqueta de la sección (píldora de
su color con el nombre; desde el 19/10/2026 ya no hay portada borrosa de 1 s: el vídeo
arranca con la imagen real), con el gancho abajo en amarillo. Música de fondo con fundido al final.

Requisitos: pip install pillow imageio-ffmpeg
Uso: python herramientas/montar_reel.py guion.json  ->  <nombre>.mp4 junto al guion

guion.json (rutas relativas a la carpeta del guion):
{
  "nombre": "historia-rony",
  "musica": "audio/musica-heroe-epica.mp3",
  "seccion": "Historias de cuatro patas",   (etiqueta de la sección arriba en la 1.ª escena)
  "etiqueta": "Imágenes ilustrativas creadas con IA",   (opcional, abajo a la izquierda)
  "escenas": [
    {"foto": "img/1.jpg", "dur": 3.4, "gancho": "Frase gancho (abajo, en amarillo)", "texto": null},
    {"foto": "img/2.png", "dur": 4.0, "texto": "Subtítulo de esta escena", "x": 0.4}
  ]
}
"x" (0-1, por defecto 0.5) elige qué parte horizontal de una foto apaisada se
queda al recortarla a vertical (útil con imágenes generadas en 16:9).

Secciones y su color (los mismos del calendario de redes):
  Curiosidades de nuestras mascotas, Historias de cuatro patas, Producto del día,
  Del blog de Petsforyou, La familia Petsforyou, Los animales, nuestros amigos,
  Curiosidades del mundo animal, Ada y sus amigos, Las mascotas hablan.
  Cualquier otro nombre sale en gris. Para poner la portada a un vídeo ya
  montado (Ada, Las mascotas hablan) usa herramientas/portada_seccion.py.
"""
import json
import os
import subprocess
import sys
import textwrap
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 30
FADE = 0.6  # segundos de transición entre fotos
FONT = next((f for f in (
    "C:/Windows/Fonts/arialbd.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
) if os.path.exists(f)), None)
if FONT is None:
    sys.exit("No encuentro una fuente en negrita: instala fonts-dejavu-core")


COLORES = {
    "curiosidades de nuestras mascotas": (11, 138, 123),
    "curiosidades de mascotas": (11, 138, 123),
    "historias de cuatro patas": (196, 106, 6),
    "producto del día": (210, 58, 82),
    "del blog de petsforyou": (42, 100, 212),
    "la familia petsforyou": (154, 107, 47),
    "los animales, nuestros amigos": (14, 116, 144),
    "curiosidades del mundo animal": (162, 28, 175),
    "ada y sus amigos": (116, 66, 214),
    "las mascotas hablan": (55, 140, 46),
    "busca familia": (219, 39, 119),
    "noticias que cuentan": (71, 85, 105),
    "tu mascota y la ley": (30, 64, 175),
    "salud y mascotas": (5, 150, 105),
    "nosotros y nuestras mascotas": (234, 88, 12),
}


PORTADA = 1.6  # segundos de portada con el nombre de la sección (se ve ~1 s entera)


def capa_portada(seccion, salida):
    """Capa de la portada: velo oscuro, nombre de la sección grande en el centro y
    una barra de su color debajo."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 110))
    d = ImageDraw.Draw(img)
    color = COLORES.get(seccion.lower(), (90, 98, 110))
    f = ImageFont.truetype(FONT, 104)
    lineas = textwrap.wrap(seccion.upper(), 14)
    alto = 104 * 1.15
    y = H / 2 - alto * len(lineas) / 2 - 40
    for ln in lineas:
        w = d.textlength(ln, font=f)
        d.text(((W - w) / 2, y), ln, font=f, fill="white", stroke_width=6, stroke_fill="black")
        y += alto
    d.rounded_rectangle([W / 2 - 170, y + 30, W / 2 + 170, y + 52], radius=11, fill=color + (255,))
    f2 = ImageFont.truetype(FONT, 40)
    w = d.textlength("PETSFORYOU", font=f2)
    d.text(((W - w) / 2, y + 90), "PETSFORYOU", font=f2, fill=(255, 255, 255, 220),
           stroke_width=3, stroke_fill="black")
    img.save(salida)


def capa_etiqueta_seccion(seccion, salida):
    """Etiqueta de la sección ARRIBA, sobre la primera escena (desde el 19/10/2026 sustituye
    a la portada borrosa de 1 s): una píldora del color de la sección con su nombre en blanco
    y PETSFORYOU debajo. El vídeo empieza ya con la imagen real, que es lo que engancha
    (en TikTok el primer segundo decide si la gente se queda)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Velo suave arriba para que se lea sobre cualquier foto.
    for y in range(0, 520):
        a = int(150 * (1 - y / 520) ** 1.5)
        d.line([(0, y), (W, y)], fill=(0, 0, 0, a))
    color = COLORES.get(seccion.lower(), (90, 98, 110))
    f = ImageFont.truetype(FONT, 58)
    txt = seccion.upper()
    tw = d.textlength(txt, font=f)
    while tw > W - 160 and f.size > 36:
        f = ImageFont.truetype(FONT, f.size - 4)
        tw = d.textlength(txt, font=f)
    x0, y0 = (W - tw) / 2 - 44, 190
    d.rounded_rectangle([x0, y0, x0 + tw + 88, y0 + f.size + 46], radius=(f.size + 46) // 2,
                        fill=color + (240,))
    d.text(((W - tw) / 2, y0 + 20), txt, font=f, fill="white")
    f2 = ImageFont.truetype(FONT, 34)
    w2 = d.textlength("PETSFORYOU", font=f2)
    d.text(((W - w2) / 2, y0 + f.size + 66), "PETSFORYOU", font=f2, fill=(255, 255, 255, 235),
           stroke_width=3, stroke_fill="black")
    img.save(salida)


def unir_capas(*capas, salida):
    """Superpone varios PNG transparentes en uno."""
    base = Image.open(capas[0]).convert("RGBA")
    for c in capas[1:]:
        base = Image.alpha_composite(base, Image.open(c).convert("RGBA"))
    base.save(salida)


def capa_texto(texto, salida, gancho=None, etiqueta=None):
    """PNG transparente con el subtítulo abajo; el gancho (si lo hay) también abajo, en amarillo."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Degradado oscuro abajo para que se lea sobre cualquier foto (sin recuadro).
    for y in range(H - 900, H):
        a = int(200 * ((y - (H - 900)) / 900) ** 1.6)
        d.line([(0, y), (W, y)], fill=(0, 0, 0, a))

    def bloque(txt, size, y_centro, ancho, color="white"):
        f = ImageFont.truetype(FONT, size)
        lineas = textwrap.wrap(txt, ancho)
        alto = size * 1.18
        y = y_centro - alto * len(lineas) / 2
        for ln in lineas:
            w = d.textlength(ln, font=f)
            d.text(((W - w) / 2, y), ln, font=f, fill=color,
                   stroke_width=max(4, size // 14), stroke_fill="black")
            y += alto

    if gancho and texto:
        bloque(gancho, 80, 1260, 22, (255, 216, 74))
        bloque(texto, 72, 1580, 24)
    elif gancho:
        bloque(gancho, 84, 1450, 21, (255, 216, 74))
    elif texto:
        bloque(texto, 72, 1450, 24)
    if etiqueta:
        f = ImageFont.truetype(FONT, 30)
        d.text((40, H - 70), etiqueta, font=f, fill=(255, 255, 255, 200),
               stroke_width=2, stroke_fill="black")
    img.save(salida)


def clip(foto, capa, dur, salida, zoom_in=True, fx=0.5, fundido=True):
    """Foto a pantalla completa con zoom lento + capa de texto que entra con fundido.

    fx (0-1) elige qué parte horizontal de la foto se queda al recortar a vertical.
    """
    frames = int(dur * FPS)
    z = (f"zoom='1+0.10*on/{frames}'" if zoom_in
         else f"zoom='1.10-0.10*on/{frames}'")
    vf = (f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,"
          f"crop={W*2}:{H*2}:(iw-{W*2})*{fx}:(ih-{H*2})/2,zoompan={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={frames}:s={W}x{H}:fps={FPS},setsar=1[bg];"
          f"[1:v]format=rgba{',fade=t=in:st=0.25:d=0.45:alpha=1' if fundido else ''}[t];"
          f"[bg][t]overlay=0:0:shortest=1,format=yuv420p")
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-i", foto,
                    "-loop", "1", "-t", str(dur), "-i", capa,
                    "-filter_complex", vf, "-t", str(dur), "-r", str(FPS),
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", salida],
                   check=True)


def main(guion_path):
    g = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    base = Path(guion_path).parent
    tmp = base / "tmp" / g["nombre"]
    tmp.mkdir(parents=True, exist_ok=True)

    clips, durs = [], []
    etiqueta_sec = None
    if g.get("seccion"):
        # Desde el 19/10/2026: nada de portada borrosa aparte. La etiqueta de la sección va
        # arriba, encima de la primera escena, y el vídeo arranca ya con la imagen real.
        etiqueta_sec = tmp / "etiqueta_seccion.png"
        capa_etiqueta_seccion(g["seccion"], etiqueta_sec)
    for i, esc in enumerate(g["escenas"]):
        capa = tmp / f"t{i}.png"
        capa_texto(esc.get("texto"), capa, esc.get("gancho"), g.get("etiqueta"))
        if i == 0 and etiqueta_sec:
            unir_capas(capa, etiqueta_sec, salida=capa)
        c = tmp / f"c{i}.mp4"
        clip(str(base / esc["foto"]), str(capa), esc["dur"], str(c),
             zoom_in=i % 2 == 0, fx=esc.get("x", 0.5), fundido=i > 0)
        clips.append(c)
        durs.append(esc["dur"])

    # Encadenar con fundidos (xfade) y poner la música.
    inputs = sum([["-i", str(c)] for c in clips], [])
    filtro, prev, t = [], "[0:v]", 0.0
    for i in range(1, len(clips)):
        t += durs[i - 1] - FADE
        out = f"[v{i}]"
        filtro.append(f"{prev}[{i}:v]xfade=transition=fade:duration={FADE}:offset={t:.2f}{out}")
        prev = out
    total = sum(durs) - FADE * (len(clips) - 1)
    musica = str(base / g["musica"])
    filtro.append(f"[{len(clips)}:a]atrim=0:{total:.2f},afade=t=in:d=0.5,"
                  f"afade=t=out:st={total-1.5:.2f}:d=1.5,volume=0.9[a]")
    salida = base / f"{g['nombre']}.mp4"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", *inputs,
                    "-stream_loop", "-1", "-i", musica,
                    "-filter_complex", ";".join(filtro), "-map", prev, "-map", "[a]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                    "-movflags", "+faststart", "-t", f"{total:.2f}", str(salida)],
                   check=True)
    print(f"{salida}  ({total:.1f} s)")


if __name__ == "__main__":
    main(sys.argv[1])
