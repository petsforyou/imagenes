"""Monta un reel vertical 1080x1920 a pantalla completa a partir de fotos.

Formato de redes de Petsforyou desde el 16/10/2026 (sustituye a la tarjeta
blanca de tarjeta.py): cada foto ocupa toda la pantalla con un zoom lento, pasa
a la siguiente con un fundido y lleva su frase en subtítulos grandes abajo; la
primera escena lleva un gancho arriba. Música de fondo con fundido al final.

Requisitos: pip install pillow imageio-ffmpeg
Uso: python herramientas/montar_reel.py guion.json  ->  <nombre>.mp4 junto al guion

guion.json (rutas relativas a la carpeta del guion):
{
  "nombre": "historia-rony",
  "musica": "audio/musica-heroe-epica.mp3",
  "seccion": "Historias de cuatro patas",   (nombre de la sección: sale arriba en la primera escena)
  "etiqueta": "Imágenes ilustrativas creadas con IA",   (opcional, abajo a la izquierda)
  "escenas": [
    {"foto": "img/1.jpg", "dur": 3.4, "gancho": "Frase gancho arriba", "texto": null},
    {"foto": "img/2.png", "dur": 4.0, "texto": "Subtítulo de esta escena", "x": 0.4}
  ]
}
"x" (0-1, por defecto 0.5) elige qué parte horizontal de una foto apaisada se
queda al recortarla a vertical (útil con imágenes generadas en 16:9).

Secciones y su color (los mismos del calendario de redes):
  Curiosidades de mascotas, Historias de cuatro patas, Producto del día,
  Del blog de Petsforyou, La familia Petsforyou, Los animales, nuestros amigos,
  Curiosidades del mundo animal. Cualquier otro nombre sale en gris.
"""
import json
import os
import subprocess
import sys
import textwrap
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

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
    "curiosidades de mascotas": (11, 138, 123),
    "historias de cuatro patas": (196, 106, 6),
    "producto del día": (210, 58, 82),
    "del blog de petsforyou": (42, 100, 212),
    "la familia petsforyou": (154, 107, 47),
    "los animales, nuestros amigos": (14, 116, 144),
    "curiosidades del mundo animal": (162, 28, 175),
}


def etiqueta_seccion(d, seccion):
    """Etiqueta con el nombre de la sección arriba del todo, en su color."""
    f = ImageFont.truetype(FONT, 46)
    txt = seccion.upper()
    w = d.textlength(txt, font=f)
    x0, y0 = (W - w) / 2 - 34, 96
    d.rounded_rectangle([x0, y0, x0 + w + 68, y0 + 84], radius=42,
                        fill=COLORES.get(seccion.lower(), (90, 98, 110)) + (235,))
    d.text(((W - w) / 2, y0 + 16), txt, font=f, fill="white")


def capa_texto(texto, salida, arriba=None, etiqueta=None, seccion=None):
    """PNG transparente con el subtítulo abajo (y opcionalmente un gancho arriba)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Degradado oscuro abajo para que se lea sobre cualquier foto (sin recuadro).
    for y in range(H - 900, H):
        a = int(200 * ((y - (H - 900)) / 900) ** 1.6)
        d.line([(0, y), (W, y)], fill=(0, 0, 0, a))

    def bloque(txt, size, y_centro, ancho):
        f = ImageFont.truetype(FONT, size)
        lineas = textwrap.wrap(txt, ancho)
        alto = size * 1.18
        y = y_centro - alto * len(lineas) / 2
        for ln in lineas:
            w = d.textlength(ln, font=f)
            d.text(((W - w) / 2, y), ln, font=f, fill="white",
                   stroke_width=max(4, size // 14), stroke_fill="black")
            y += alto

    if texto:
        bloque(texto, 72, 1450, 24)
    if arriba or seccion:
        for y in range(0, 600):
            a = int(170 * (1 - y / 600) ** 1.6)
            d.line([(0, y), (W, y)], fill=(0, 0, 0, a))
    if seccion:
        etiqueta_seccion(d, seccion)
    if arriba:
        bloque(arriba, 86, 390 if seccion else 300, 20)
    if etiqueta:
        f = ImageFont.truetype(FONT, 30)
        d.text((40, H - 70), etiqueta, font=f, fill=(255, 255, 255, 200),
               stroke_width=2, stroke_fill="black")
    img.save(salida)


def clip(foto, capa, dur, salida, zoom_in=True, fx=0.5):
    """Foto a pantalla completa con zoom lento + capa de texto que entra con fundido.

    fx (0-1) elige qué parte horizontal de la foto se queda al recortar a vertical.
    """
    frames = int(dur * FPS)
    z = (f"zoom='1+0.10*on/{frames}'" if zoom_in
         else f"zoom='1.10-0.10*on/{frames}'")
    vf = (f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,"
          f"crop={W*2}:{H*2}:(iw-{W*2})*{fx}:(ih-{H*2})/2,zoompan={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={frames}:s={W}x{H}:fps={FPS},setsar=1[bg];"
          f"[1:v]format=rgba,fade=t=in:st=0.25:d=0.45:alpha=1[t];"
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
    for i, esc in enumerate(g["escenas"]):
        capa = tmp / f"t{i}.png"
        capa_texto(esc.get("texto"), capa, esc.get("gancho"), g.get("etiqueta"),
                   g.get("seccion") if i == 0 else None)
        c = tmp / f"c{i}.mp4"
        clip(str(base / esc["foto"]), str(capa), esc["dur"], str(c),
             zoom_in=i % 2 == 0, fx=esc.get("x", 0.5))
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
