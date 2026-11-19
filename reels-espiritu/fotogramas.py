# -*- coding: utf-8 -*-
"""Hoja de fotogramas (uno por escena) de un reel montado. Uso: python -I fotogramas.py nombre"""
import json, os, subprocess, sys
import imageio_ffmpeg
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__))
FF = imageio_ffmpeg.get_ffmpeg_exe()
for n in sys.argv[1:]:
    g = json.load(open(os.path.join(D, f"guion-{n}.json"), encoding="utf8"))
    t, ims = 0.0, []
    for i, e in enumerate(g["escenas"]):
        mid = t + e["dur"] * 0.62
        t += e["dur"] - 0.6
        out = os.path.join(D, "tmp", f"f_{n}_{i}.jpg")
        subprocess.run([FF, "-y", "-loglevel", "error", "-ss", f"{mid:.2f}", "-i", os.path.join(D, n + ".mp4"),
                        "-frames:v", "1", "-vf", "scale=300:-1", out], check=True)
        ims.append(Image.open(out))
    cols = 5
    rows = (len(ims) + cols - 1) // cols
    S = Image.new("RGB", (cols * 304, rows * 538), "white")
    for i, im in enumerate(ims):
        S.paste(im, ((i % cols) * 304, (i // cols) * 538))
    S.save(os.path.join(D, f"fotogramas-{n}.jpg"), quality=82)
    print(n, len(ims), "escenas", f"{t + 0.6:.1f} s")
