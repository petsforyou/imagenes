"""Monta un episodio de "Las mascotas hablan" (formato desde el 17/10/2026).

Primero la intro de la sección (videos/intro-mascotas-hablan.mp4: los cinco
protagonistas en su versión "mascotas hablan": labrador, gato, Rick el conejo
blanco, hurón y el hámster roquero) con el título "LAS MASCOTAS HABLAN" encima,
el título del episodio y quién habla; después, el monólogo tal cual (1080x1920).

Requisitos: pip install pillow imageio-ffmpeg
Uso:
  python herramientas/mascotas_hablan.py --monologo monologo.mp4 \
      --titulo "El paseo es mi periódico" --actor "el labrador" --salida mh-paseo.mp4
"""
import argparse
import os
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 30
INTRO = RAIZ / "videos" / "intro-mascotas-hablan.mp4"
FONT = next((f for f in (
    "C:/Windows/Fonts/impact.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
) if os.path.exists(f)), None)
if FONT is None:
    sys.exit("No encuentro una fuente en negrita: instala fonts-dejavu-core")


def rotulo(titulo, actor, salida):
    """PNG transparente: título de la sección arriba y episodio abajo (en las franjas negras de la intro)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    def centrado(txt, size, y, color, ancho):
        f = ImageFont.truetype(FONT, size)
        for ln in textwrap.wrap(txt, ancho):
            w = d.textlength(ln, font=f)
            d.text(((W - w) / 2, y), ln, font=f, fill=color, stroke_width=max(4, size // 14), stroke_fill="black")
            y += int(size * 1.08)
        return y

    centrado("LAS MASCOTAS HABLAN", 128, 70, "#ffd84a", 12)
    y = centrado(f"«{titulo}»", 66, 1660, "white", 26)
    if actor:
        centrado(f"Hoy habla {actor}", 48, y + 8, "#ffd84a", 34)
    img.save(salida)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--monologo", required=True)
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--actor", default="")
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        png = Path(tmp) / "rotulo.png"
        rotulo(a.titulo, a.actor, png)
        norm = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:black,"
                f"setsar=1,fps={FPS},format=yuv420p")
        filtro = (
            f"[0:v]{norm}[iv];[1:v]format=rgba,fade=t=in:st=0.2:d=0.4:alpha=1[t];"
            f"[iv][t]overlay=0:0:shortest=1,format=yuv420p[v0];"
            f"[0:a]aresample=48000,aformat=channel_layouts=stereo[a0];"
            f"[2:v]{norm},fade=t=in:st=0:d=0.25[v1];"
            f"[2:a]aresample=48000,aformat=channel_layouts=stereo[a1];"
            f"[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]"
        )
        subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(INTRO), "-loop", "1", "-i", str(png),
                        "-i", a.monologo, "-filter_complex", filtro, "-map", "[v]", "-map", "[a]",
                        "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "160k",
                        "-movflags", "+faststart", a.salida], check=True)
    print(a.salida)


if __name__ == "__main__":
    main()
