"""Convierte una tarjeta de frase (foto 1080x1350 con el texto ya incluido, como las
de frases/) en el reel de la sección "Pensamientos": la encaja ENTERA sobre su propio
fondo desenfocado y oscurecido (nunca se recorta: cortaría la frase) y llama a
montar_reel.py para montar el vídeo final con música.

uso: python3 herramientas/tarjeta_a_reel.py frases/frase_07.jpg carruseles/pensamientos/2026-10-27-frase-07 pensamientos-frase-07
  argv[1] = tarjeta de origen (1080x1350)
  argv[2] = carpeta de salida (se crea si no existe)
  argv[3] = "nombre" del guion (también el nombre del .mp4 final)

Música fija de la sección: audio/musica-pensamientos-calma.mp3 (María, 24/10/2026:
cada sección la suya). Dos escenas de la misma tarjeta (5 s + 5 s, zoom alterno) para
que el reel "respire" sin mover la frase.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
import montar_reel

W, H = 1080, 1920


def componer(tarjeta: Path, salida: Path) -> None:
    im = Image.open(tarjeta).convert("RGB")
    bg = im.copy()
    bw, bh = bg.size
    escala = max(W / bw, H / bh)
    bg = bg.resize((int(bw * escala) + 2, int(bh * escala) + 2), Image.LANCZOS)
    bx, by = bg.size
    bg = bg.crop(((bx - W) // 2, (by - H) // 2, (bx - W) // 2 + W, (by - H) // 2 + H))
    bg = bg.filter(ImageFilter.GaussianBlur(40))
    bg = ImageEnhance.Brightness(bg).enhance(0.7)
    lienzo = bg.copy()
    y = 560
    lienzo.paste(im, (0, y))
    salida.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(salida, quality=92)


def main(tarjeta, carpeta_salida, nombre):
    tarjeta = Path(tarjeta)
    carpeta = Path(carpeta_salida)
    img_dir = carpeta / "img"
    img_dir.mkdir(parents=True, exist_ok=True)

    original = img_dir / "1.jpg"
    original.write_bytes(tarjeta.read_bytes())
    completa = img_dir / "1-completa.jpg"
    componer(tarjeta, completa)

    # Ruta relativa de la música desde la carpeta del guion hasta audio/ en la raíz del repo.
    subida = "../" * len(carpeta.parts)
    guion = {
        "nombre": nombre,
        "musica": f"{subida}audio/musica-pensamientos-calma.mp3",
        "seccion": "Pensamientos",
        "escenas": [
            {"foto": "img/1-completa.jpg", "dur": 5.0},
            {"foto": "img/1-completa.jpg", "dur": 5.0},
        ],
    }
    guion_path = carpeta / "guion.json"
    guion_path.write_text(json.dumps(guion, ensure_ascii=False, indent=2), encoding="utf-8")

    montar_reel.main(str(guion_path))
    print(f"vídeo: {carpeta / (nombre + '.mp4')}")


if __name__ == "__main__":
    main(*sys.argv[1:])
