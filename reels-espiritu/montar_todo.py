# -*- coding: utf-8 -*-
"""Reels «lo que nos hace distintos» (pedido de María, 19/11/2026). Prepara las imágenes, escribe los
guiones y monta con herramientas/montar_reel.py. Uso: python -I montar_todo.py [nombre ...]
Imagen: ("c", ruta[, x]) = a pantalla completa (recorte); ("f", ruta) = entera sobre su fondo desenfocado."""
import json, os, subprocess, sys
from PIL import Image, ImageFilter, ImageEnhance

D = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
B, C, P = "bib/", "cand/", "prod/"


def preparar(modo, ruta, salida):
    im = Image.open(os.path.join(D, ruta))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        fondo = Image.new("RGBA", im.size, "white")
        im = Image.alpha_composite(fondo, im)
    im = im.convert("RGB")
    if modo == "c":
        im.save(salida, quality=93)
        return
    s = max(W / im.width, H / im.height)
    bg = im.resize((int(im.width * s) + 1, int(im.height * s) + 1))
    x0, y0 = (bg.width - W) // 2, (bg.height - H) // 2
    bg = bg.crop((x0, y0, x0 + W, y0 + H)).filter(ImageFilter.GaussianBlur(45))
    bg = ImageEnhance.Brightness(bg).enhance(0.62)
    s = min(W / im.width, 1180 / im.height)
    fg = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, 790 - fg.height // 2))
    bg.save(salida, quality=93)


REELS = {
 "pfy-lo-que-no-vendemos": ("musica-historias-emocionante-2.mp3", [
  (3.6, "g", "Tres cosas que esta tienda de mascotas se niega a vender.", ("c", B + "A3_escena-3.png")),
  (3.2, "t", "Una: jaulas pequeñas para que viva un hámster.", ("f", C + "jaulapeq3.jpg")),
  (3.6, "t", "Aquí, la más pequeña mide 100 × 50 cm de suelo.", ("f", P + "jaula3.jpg")),
  (3.2, "t", "Dos: arneses para conejos y animales pequeños.", ("f", C + "conejo3.jpg")),
  (3.4, "t", "Tres: animales. Ninguno. Nunca.", ("c", B + "app8.png")),
  (3.6, "t", "A los que buscan casa los difundimos gratis.", ("c", B + "pfy2.png")),
  (3.4, "t", "Si a ellos no les hace bien, aquí no se vende.", ("c", B + "A3_escena-2.png")),
  (3.6, "t", "Hay ventas que no queremos. petsforyou.es", ("c", B + "app5.png")),
 ]),
 "pfy-aqui-todos-cuentan": ("musica-historias-emocionante-3.mp3", [
  (4.0, "g", "En cada hogar del mundo hay un pequeño amigo que nos acompaña en la vida.", ("c", B + "A3_escena-5.png")),
  (2.6, "t", "A veces es un hámster.", ("c", B + "A3_escena-1.png")),
  (2.6, "t", "A veces, un hurón.", ("c", B + "A4_escena-2.png")),
  (2.6, "t", "O una gallina.", ("c", C + "gallina2.jpg")),
  (2.6, "t", "Una tortuga.", ("c", B + "G02_escena-5.png")),
  (2.6, "t", "Un pez.", ("c", B + "C26_escena-3.png")),
  (2.6, "t", "Un pájaro.", ("f", C + "pajaro2.jpg")),
  (2.6, "t", "Un conejo, una cobaya, una chinchilla.", ("c", B + "G08_escena-5.png")),
  (2.6, "t", "Un perro. Un gato.", ("c", B + "NAV_09.png")),
  (3.0, "t", "Por eso estamos en 48 países.", ("c", B + "pfy5.png")),
  (3.2, "t", "Y por eso todos tienen aquí su sección.", ("c", B + "pfy6.png")),
  (3.8, "t", "En esta tienda cabemos todos. ¿Nos falta el tuyo? Escríbenos.", ("c", B + "A4_escena-4.png")),
 ]),
 "pfy-nunca-vendemos-animales": ("musica-historias-emocionante.mp3", [
  (3.8, "g", "Somos una tienda de mascotas. Y no vendemos mascotas.", ("c", C + "pata4.jpg")),
  (3.4, "t", "Un animal no es un producto.", ("f", C + "pata0.jpg")),
  (3.8, "t", "Cada semana difundimos gratis a uno que busca casa.", ("c", B + "app2.png")),
  (3.8, "t", "¿Quieres ayudar? Dona directamente a su protectora.", ("c", B + "app1.png")),
  (3.4, "t", "El dinero nunca pasa por nosotros.", ("c", B + "app4.png")),
  (3.8, "t", "Su final feliz no se compra. Se adopta.", ("c", B + "app7.png")),
  (3.6, "t", "Mira quién busca casa en petsforyou.es", ("c", B + "M01_escena-5.png")),
 ]),
 "pfy-sal-de-ruta-con-tu-perro": ("musica-mundo-animal-aventura.mp3", [
  (4.0, "g", "Llegas con tu perro… y el cartel dice «perros no».", ("c", B + "app1.png")),
  (3.4, "t", "Horas buscando rutas donde de verdad lo admitan.", ("c", B + "app2.png")),
  (3.4, "t", "Estamos haciendo una app para acabar con eso.", ("c", B + "app3.png")),
  (3.4, "t", "Rutas a pie con perro por toda Europa: senderismo y travesías.", ("c", B + "app4.png")),
  (3.4, "t", "Las guardas y se abren sin cobertura.", ("c", B + "app5.png")),
  (3.6, "t", "Con apartado de autocaravana y las normas de cada país.", ("c", B + "app6.png")),
  (3.6, "t", "Se llama Rutas con tu peludo. Está en pruebas.", ("c", B + "app7.png")),
  (4.2, "t", "¿La pruebas antes que nadie? Escribe a contacto@petsforyou.es", ("c", B + "app8.png")),
 ]),
 "pfy-hecho-aqui": ("musica-producto-alegre.mp3", [
  (3.6, "g", "Tres marcas españolas. La tercera le pone su nombre.", ("c", B + "pfy1.png")),
  (3.4, "t", "AriBabi: diseños propios y mucho color.", ("f", P + "ari1.jpg")),
  (3.2, "t", "Collar, correa y portabolsas a juego.", ("f", P + "ari3.jpg")),
  (3.4, "t", "M!MADO: champú sólido con aloe vera.", ("f", P + "mim1.jpg")),
  (3.2, "t", "Para perros y gatos.", ("f", P + "mim3.jpg")),
  (3.4, "t", "Mascotas Y Max: cuero hecho a mano en España.", ("f", P + "mym3.png")),
  (3.4, "t", "Y graban su nombre.", ("f", P + "mym5.png")),
  (3.8, "t", "Hecho aquí. Lo tienes en petsforyou.es", ("c", B + "pfy7.png")),
 ]),
 "pfy-comer-de-verdad": ("musica-salud-tranquila.mp3", [
  (3.8, "g", "Lee la etiqueta de su comida. ¿Reconoces los ingredientes?", ("f", C + "pienso5.jpg")),
  (3.4, "t", "En la comida natural se ven a simple vista.", ("f", P + "cru1.jpg")),
  (3.6, "t", "Cruda (BARF): carne y verduras sin cocinar.", ("f", P + "cru4.jpg")),
  (3.4, "t", "Cocinada: lista para servir.", ("f", P + "puro1.png")),
  (3.4, "t", "Con ingredientes como estos.", ("f", P + "puro2.png")),
  (3.4, "t", "Y snacks naturales deshidratados.", ("f", P + "puro3.png")),
  (3.6, "t", "El cambio, poco a poco y con tu veterinario.", ("f", P + "cru2.jpg")),
  (3.8, "t", "Para perros y gatos. Alimentación natural en petsforyou.es", ("c", B + "G39_escena-5.png")),
 ]),
}

for nombre, (musica, escenas) in REELS.items():
    if len(sys.argv) > 1 and nombre not in sys.argv[1:]:
        continue
    os.makedirs(os.path.join(D, "img", nombre), exist_ok=True)
    g = {"nombre": nombre, "musica": "../audio/" + musica, "escenas": []}
    for i, (dur, tipo, texto, (modo, ruta)) in enumerate(escenas, 1):
        rel = f"img/{nombre}/{i}.jpg"
        preparar(modo, ruta, os.path.join(D, rel))
        e = {"foto": rel, "dur": dur, "_origen": ruta}
        e["gancho" if tipo == "g" else "texto"] = texto
        g["escenas"].append(e)
    gp = os.path.join(D, f"guion-{nombre}.json")
    json.dump(g, open(gp, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    subprocess.run([sys.executable, os.path.join(D, "..", "herramientas", "montar_reel.py"), gp], check=True)
