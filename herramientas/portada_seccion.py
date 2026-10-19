"""Pone la etiqueta de la sección encima del principio de un vídeo ya montado.

Desde el 19/10/2026 ya no se añade 1 s de portada borrosa delante: el vídeo
arranca con su propia imagen y, durante los primeros segundos, lleva arriba la
etiqueta de la sección (píldora de su color con el nombre y PETSFORYOU), que se
desvanece. Es la misma etiqueta que pone montar_reel.py en la primera escena.
Se usa para los vídeos que no salen de montar_reel.py: capítulos de Ada y sus
amigos y monólogos de Las mascotas hablan. Salida 1080x1920, 30 fps, con el
audio original intacto (el vídeo dura lo mismo que el original).

Requisitos: pip install pillow imageio-ffmpeg
Uso: python herramientas/portada_seccion.py --video capitulo.mp4 \
        --seccion "Ada y sus amigos" --salida capitulo-con-portada.mp4
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from montar_reel import FFMPEG, FPS, H, W, capa_etiqueta_seccion  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--seccion", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--segundos", type=float, default=3.0,
                    help="cuánto tiempo se ve la etiqueta antes de desvanecerse")
    ap.add_argument("--fotograma", type=float, default=None, help="(obsoleto, se ignora)")
    a = ap.parse_args()

    tmp = Path(tempfile.mkdtemp(prefix="etiqueta-"))
    capa = tmp / "etiqueta.png"
    capa_etiqueta_seccion(a.seccion, capa)

    fin = a.segundos
    filtro = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease,"
              f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS},setsar=1[v0];"
              f"[1:v]format=rgba,fade=t=out:st={fin - 0.5:.2f}:d=0.5:alpha=1[e];"
              f"[v0][e]overlay=0:0:enable='lt(t,{fin:.2f})',format=yuv420p[v]")
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", a.video,
                    "-loop", "1", "-t", f"{fin:.2f}", "-i", str(capa),
                    "-filter_complex", filtro, "-map", "[v]", "-map", "0:a?",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", a.salida], check=True)
    print(a.salida)


if __name__ == "__main__":
    main()
