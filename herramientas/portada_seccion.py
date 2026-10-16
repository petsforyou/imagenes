"""Pone delante de un vídeo ya montado la portada de 1 s con el nombre de la sección.

Es la misma portada que monta montar_reel.py (nombre grande sobre la primera
imagen desenfocada, barra del color de la sección y PETSFORYOU). Se usa para los
vídeos que no salen de montar_reel.py: capítulos de Ada y sus amigos y
monólogos de Las mascotas hablan. Salida 1080x1920, 30 fps, con el audio del
vídeo original (que entra cuando termina el fundido de la portada).

Requisitos: pip install pillow imageio-ffmpeg
Uso: python herramientas/portada_seccion.py --video capitulo.mp4 \
        --seccion "Ada y sus amigos" --salida capitulo-con-portada.mp4
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from montar_reel import FADE, FFMPEG, FPS, PORTADA, H, W, capa_portada, clip  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--seccion", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--fotograma", type=float, default=1.0,
                    help="segundo del vídeo que se usa de fondo de la portada")
    a = ap.parse_args()

    tmp = Path(tempfile.mkdtemp(prefix="portada-"))
    fondo = tmp / "fondo.png"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-ss", str(a.fotograma), "-i", a.video,
                    "-frames:v", "1", str(fondo)], check=True)
    Image.open(fondo).convert("RGB").filter(ImageFilter.GaussianBlur(18)).save(tmp / "fondo.jpg", quality=92)
    capa_portada(a.seccion, tmp / "capa.png")
    portada = tmp / "portada.mp4"
    clip(str(tmp / "fondo.jpg"), str(tmp / "capa.png"), PORTADA, str(portada),
         zoom_in=False, fundido=False)

    off = PORTADA - FADE
    filtro = (f"[1:v]scale={W}:{H}:force_original_aspect_ratio=decrease,"
              f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS},setsar=1,format=yuv420p,settb=1/{FPS}[v1];"
              f"[0:v]fps={FPS},format=yuv420p,settb=1/{FPS}[v0];"
              f"[v0][v1]xfade=transition=fade:duration={FADE}:offset={off:.2f}[v];"
              f"[1:a]aresample=48000,aformat=channel_layouts=stereo,"
              f"adelay={int(off * 1000)}:all=1[a]")
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(portada), "-i", a.video,
                    "-filter_complex", filtro, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", a.salida], check=True)
    print(a.salida)


if __name__ == "__main__":
    main()
