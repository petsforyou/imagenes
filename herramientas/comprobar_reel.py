#!/usr/bin/env python3
"""
comprobar_reel.py  -  Comprobación de calidad de un reel ANTES de programarlo.

Norma de María (26/10/2026): todo reel cuenta una historia completa, dura 20-30 s,
lleva al menos 4 imágenes DISTINTAS que ilustran lo que se dice (fotos reales, libres
o generadas), y nada de láminas gráficas (flechas, iconos, interrogantes, señales de
aviso, fondos lisos). Ver instrucciones/Reels - cómo se cuenta una historia.md

Uso:   python herramientas/comprobar_reel.py reel.mp4 [reel2.mp4 ...]
Salida: una línea por reel con APTO o NO APTO y el motivo; código de salida 0 si
todos son aptos, 1 si alguno no lo es. Requisitos: pip install pillow imageio-ffmpeg

Qué mide (de forma automática, a modo de ayuda; NO sustituye a mirar los fotogramas):
 - duración (mínimo 20 s, máximo 31 s; las series de Ada y Las mascotas hablan quedan fuera);
 - imágenes distintas (mínimo 4) y cuántas veces se repite la misma;
 - fotogramas «gráficos» (pocos colores = lámina plana con icono o flecha);
 - fotogramas casi vacíos (fondo liso).
"""
import math
import os
import subprocess
import sys
import tempfile

import imageio_ffmpeg
from PIL import Image

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
MIN_SEG, MAX_SEG = 20.0, 31.0
MIN_IMAGENES = 4
UMBRAL_ENTROPIA = 3.5     # variedad de grises en la zona central: láminas con flecha/icono 1,4-2,3; fotos > 4,2
UMBRAL_HASH = 8           # distancia máxima entre dos fotogramas de la MISMA imagen


def duracion(path):
    r = subprocess.run([FFMPEG, "-i", path], capture_output=True, text=True)
    for linea in r.stderr.splitlines():
        if "Duration" in linea:
            h, m, s = linea.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0


def fotogramas(path, carpeta):
    # un fotograma por segundo, reducido (suficiente para comparar)
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", path, "-vf", "fps=1,scale=108:-1",
                    os.path.join(carpeta, "f_%03d.png")], check=True)
    return [Image.open(os.path.join(carpeta, f)).convert("RGB")
            for f in sorted(os.listdir(carpeta)) if f.startswith("f_")]


def zona_central(im):
    w, h = im.size
    # evita el rótulo de arriba y los subtítulos de abajo
    return im.crop((0, int(h * 0.22), w, int(h * 0.62)))


def dhash(im, n=8):
    g = im.convert("L").resize((n + 1, n))
    px = list(g.getdata())
    bits = []
    for y in range(n):
        for x in range(n):
            bits.append(1 if px[y * (n + 1) + x] > px[y * (n + 1) + x + 1] else 0)
    return bits


def distancia(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def entropia(im):
    """Variedad de grises de la zona central (bits). Bajo = lámina plana, icono o fondo liso."""
    g = zona_central(im).convert("L")
    hist = g.histogram()
    n = float(sum(hist))
    return -sum((c / n) * math.log2(c / n) for c in hist if c)


def comprobar(path):
    problemas, avisos = [], []
    dur = duracion(path)
    if dur < MIN_SEG:
        problemas.append(f"dura {dur:.1f} s (mínimo {MIN_SEG:.0f} s)")
    if dur > MAX_SEG:
        avisos.append(f"dura {dur:.1f} s (más de {MAX_SEG:.0f} s)")
    with tempfile.TemporaryDirectory() as tmp:
        frames = fotogramas(path, tmp)
        if not frames:
            return False, ["no se pudo leer el vídeo"], []
        graficos = [i for i, f in enumerate(frames) if entropia(f) < UMBRAL_ENTROPIA]
        gset = set(graficos)
        grupos = []   # una imagen REAL distinta cada uno (las láminas gráficas no cuentan)
        usos = []
        for i, f in enumerate(frames):
            if i in gset:
                continue
            h = dhash(zona_central(f))
            for k, g in enumerate(grupos):
                if distancia(h, g) <= UMBRAL_HASH:
                    usos[k] += 1
                    break
            else:
                grupos.append(h)
                usos.append(1)
    distintas = len(grupos)
    if distintas < MIN_IMAGENES:
        problemas.append(f"solo {distintas} imágenes distintas (mínimo {MIN_IMAGENES})")
    if graficos:
        segs = ", ".join(str(i) for i in graficos[:8])
        problemas.append(f"{len(graficos)} fotogramas parecen láminas gráficas o lisas (segundos {segs}): "
                         "nada de flechas, iconos, interrogantes ni fondos lisos")
    repetidas = [u for u in usos if u * 1.0 > max(4.5, dur * 0.3)]
    if repetidas:
        avisos.append("una misma imagen ocupa más del 30 % del reel")
    return not problemas, problemas, avisos


def main(rutas):
    ok_total = True
    for ruta in rutas:
        ok, problemas, avisos = comprobar(ruta)
        nombre = os.path.basename(ruta)
        if ok:
            print(f"APTO     {nombre}" + (f"  (avisos: {'; '.join(avisos)})" if avisos else ""))
        else:
            ok_total = False
            print(f"NO APTO  {nombre}: {'; '.join(problemas)}" + (f"  (avisos: {'; '.join(avisos)})" if avisos else ""))
    return 0 if ok_total else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
