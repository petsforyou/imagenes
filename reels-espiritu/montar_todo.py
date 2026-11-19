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
 "pfy-marcas-del-mundo": ("musica-producto-alegre.mp3", [
  (3.6, "g", "Buscamos marcas por medio mundo. Nos quedamos con estas.", ("f", P + "m_lilly-dash_3.jpg")),
  (3.4, "t", "Bestia, de Bulgaria: para perros grandes y fuertes.", ("f", P + "m_bestia_6.jpg")),
  (3.4, "t", "Purré, de Polonia: cosido en talleres locales.", ("f", P + "m_purre_7.jpg")),
  (3.4, "t", "Mellow, de Cracovia: lana natural, hecho a mano.", ("f", P + "m_mellow_5.jpg")),
  (3.4, "t", "Pawsome Pets, de Nueva York: pintado a mano.", ("f", P + "m_pawsome-pets-new-york_1.jpg")),
  (3.4, "t", "Lilly+Dash, de Melbourne: bouclé y diseño.", ("f", P + "m_lilly-dash_4.jpg")),
  (3.4, "t", "Fur & Whiskers, de Australia: paseo a juego.", ("f", P + "m_fur-whiskers_5.jpg")),
  (3.8, "t", "Nuestra selección Premium. En petsforyou.es", ("f", P + "m_lilly-dash_2.jpg")),
 ]),
 "pfy-adopcion-sin-juzgar": ("musica-historias-emocionante-4.mp3", [
  (3.6, "g", "¿Adoptado o elegido? Aquí no juzgamos a nadie.", ("c", B + "NAV_09.png")),
  (3.6, "t", "Promovemos la adopción: difundimos gratis a los que buscan casa.", ("c", B + "pfy3.png")),
  (3.2, "t", "Y nunca venderemos animales.", ("c", C + "pata4.jpg")),
  (3.4, "t", "Pero a veces es mejor elegir a nuestro compañero.", ("c", B + "M01_escena-5.png")),
  (3.2, "t", "Por compatibilidad. Por salud.", ("c", B + "G39_escena-5.png")),
  (3.4, "t", "Nadie tiene por qué quedarse solo.", ("c", B + "app2.png")),
  (3.8, "t", "Venga de donde venga, aquí tiene su sitio. petsforyou.es", ("c", B + "pfy6.png")),
 ]),
 "pfy-contesto-yo": ("musica-superacion-inspiradora-3.mp3", [
  (3.8, "g", "¿Quién hay al otro lado cuando escribes a una tienda?", ("c", B + "pfy3.png")),
  (3.4, "t", "Aquí no hay centro de atención al cliente.", ("c", B + "app2.png")),
  (3.4, "t", "Hay una persona. La que eligió cada producto.", ("c", B + "A4_escena-4.png")),
  (3.6, "t", "Solo elijo lo que compraría para mis propios animales.", ("c", B + "G41_escena-4.png")),
  (3.2, "t", "No soy una gran superficie.", ("c", B + "pfy2.png")),
  (3.4, "t", "Si escribes, contesto yo.", ("c", B + "A3_escena-5.png")),
  (3.8, "t", "Escríbeme: contacto@petsforyou.es", ("c", B + "pfy6.png")),
 ]),
 "pfy-plazos-honestos": ("musica-curiosidades.mp3", [
  (3.8, "g", "¿Cuántas veces te han dicho «llega mañana»… y no llegó?", ("c", B + "G16_escena-1.png")),
  (3.4, "t", "Esperar sin saber cuánto es lo peor.", ("c", B + "G16_escena-3.png")),
  (3.6, "t", "Aquí, si algo tarda dos semanas, lo ves antes de comprar.", ("c", B + "HOOK_20.png")),
  (3.6, "t", "El plazo de tu pedido sale en el carrito, antes de pagar.", ("c", B + "app5.png")),
  (3.4, "t", "Prefiero decírtelo a que te lleves la sorpresa.", ("c", B + "NAV_11.png")),
  (3.4, "t", "Y el envío, gratis a toda España, sin mínimo.", ("c", B + "A4_escena-5.png")),
  (3.8, "t", "Plazos honestos. petsforyou.es", ("c", B + "HOOK_18.png")),
 ]),
 "pfy-precios-claros": ("musica-blog-suave.mp3", [
  (3.8, "g", "¿Por qué sube y baja el precio de lo que compras para tu mascota?", ("f", P + "m_fur-whiskers_5.jpg")),
  (3.4, "t", "Detrás hay un proveedor y un transporte.", ("f", P + "m_lilly-dash_4.jpg")),
  (3.6, "t", "Si el proveedor baja el precio, yo lo bajo.", ("f", P + "m_purre_7.jpg")),
  (3.4, "t", "Si el transporte se abarata, también.", ("f", P + "m_mellow_5.jpg")),
  (3.2, "t", "Sin precios inflados.", ("f", P + "m_lilly-dash_2.jpg")),
  (3.4, "t", "Y el envío, gratis a toda España, sin mínimo.", ("c", B + "NAV_09.png")),
  (3.8, "t", "Precios claros y honestos. petsforyou.es", ("c", B + "G39_escena-5.png")),
 ]),
 "pfy-cumple-la-ley": ("musica-ley-sobria.mp3", [
  (3.6, "g", "¿Seguro que tu mascota cumple la ley?", ("c", B + "HOOK_18.png")),
  (3.4, "t", "La normativa pide cosas a perros, gatos y otras mascotas.", ("c", B + "G39_escena-5.png")),
  (3.2, "t", "Y casi nadie nos las ha contado.", ("c", B + "A3_escena-1.png")),
  (3.4, "t", "En nuestra app lo compruebas tú mismo.", ("c", B + "pfy3.png")),
  (3.6, "t", "También qué pide cada país de Europa para viajar con ella.", ("c", B + "app3.png")),
  (3.4, "t", "Y veterinarios de urgencias cerca de ti.", ("c", B + "G20_escena-4.png")),
  (3.8, "t", "App Petsforyou. En App Store y Google Play.", ("c", B + "pfy6.png")),
 ]),
 "pfy-tambien-explicamos": ("musica-blog-suave.mp3", [
  (3.8, "g", "Antes de comprarle nada, ¿sabes qué necesita de verdad?", ("c", B + "A4_escena-1.png")),
  (3.4, "t", "Por eso no solo vendemos. También explicamos.", ("c", B + "app2.png")),
  (3.4, "t", "En el blog: consejos de salud y cuidados.", ("f", P + "i_guia.jpg")),
  (3.4, "t", "Guías para elegir bien: razas de perros y de gatos.", ("f", P + "i_razas.jpg")),
  (3.4, "t", "El primer año de tu cachorro, mes a mes.", ("f", P + "i_cachorro.jpg")),
  (3.4, "t", "Y guía de tallas en la ropa, para acertar.", ("f", P + "i_ropa.jpg")),
  (3.8, "t", "Saber antes de comprar. petsforyou.es", ("c", B + "NAV_09.png")),
 ]),
 "pfy-para-ti-tambien": ("musica-producto-alegre.mp3", [
  (3.6, "g", "¿Y para ti? Tú también eres de su familia.", ("c", B + "A4_escena-4.png")),
  (3.2, "t", "Tazas con gato.", ("f", P + "i_taza2.jpg")),
  (3.2, "t", "Para el café de cada mañana.", ("f", P + "i_taza.jpg")),
  (3.2, "t", "Pendientes con su huella.", ("f", P + "i_pend.jpg")),
  (3.2, "t", "Un anillo con su patita.", ("f", P + "i_anillo.jpg")),
  (3.4, "t", "Tarjetas pintadas a mano en Nueva York.", ("f", P + "i_tarjeta.jpg")),
  (3.8, "t", "Para quien quiere a su animal. petsforyou.es", ("c", B + "pfy6.png")),
 ]),
 "pfy-app-todo": ("musica-curiosidades-pegadiza.mp3", [
  (3.6, "g", "Una app de mascotas que no es solo una tienda.", ("c", B + "pfy3.png")),
  (3.0, "t", "Te dice si tu mascota cumple la ley.", ("c", B + "HOOK_18.png")),
  (3.2, "t", "Qué pide cada país de Europa para viajar con ella.", ("c", B + "app3.png")),
  (3.0, "t", "Veterinarios de urgencias cerca de ti.", ("c", B + "G20_escena-4.png")),
  (3.0, "t", "Consejos de salud y cuidados.", ("f", P + "i_guia.jpg")),
  (3.0, "t", "Series para ver en familia.", ("c", B + "pfy4.png")),
  (3.0, "t", "Un asistente que te ayuda a elegir.", ("c", B + "app2.png")),
  (4.0, "t", "Y la tienda entera. App Petsforyou, en App Store y Google Play.", ("c", B + "pfy6.png")),
 ]),
 "pfy-app-rutas-por-dentro": ("musica-superacion-inspiradora-2.mp3", [
  (3.8, "g", "¿Esa ruta le va bien a tu perro? Esta app te lo dice.", ("c", B + "M03_escena-1.png")),
  (3.4, "t", "Le cuentas cómo es: tamaño, edad y forma física.", ("c", B + "app8.png")),
  (3.2, "t", "Y cada ruta te dice si le va bien.", ("c", B + "app4.png")),
  (3.2, "t", "Rutas a pie por toda Europa, en el mapa.", ("c", B + "pfy5.png")),
  (3.2, "t", "Las guardas y se abren sin cobertura.", ("c", B + "app5.png")),
  (3.4, "t", "Antes de salir: mochila y seguridad.", ("c", B + "M01_escena-5.png")),
  (3.6, "t", "Y autocaravana: áreas cerca de la salida.", ("c", B + "app6.png")),
  (4.2, "t", "Rutas con tu peludo. Está en pruebas: escribe a contacto@petsforyou.es", ("c", B + "app7.png")),
 ]),
 "pfy-app-rutas-autocaravana": ("musica-mundo-animal-aventura.mp3", [
  (3.8, "g", "¿Tu autocaravana pasa por ahí? Esta app te avisa antes.", ("c", B + "app6.png")),
  (3.6, "t", "Pones su altura, peso y largo. Y te avisa de gálibos y límites.", ("c", B + "app3.png")),
  (3.2, "t", "Calcula la ruta según tu altura y tu peso.", ("c", B + "pfy5.png")),
  (3.0, "t", "Gasolineras con GLP en el mapa.", ("c", B + "app7.png")),
  (3.2, "t", "Con precios del día en España y Francia.", ("c", B + "app1.png")),
  (3.6, "t", "Qué pide cada país para cruzar la frontera con tu perro.", ("c", B + "app4.png")),
  (3.2, "t", "Y rutas a pie con perro por toda Europa.", ("c", B + "app5.png")),
  (4.2, "t", "Rutas con tu peludo. Está en pruebas: escribe a contacto@petsforyou.es", ("c", B + "app8.png")),
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
