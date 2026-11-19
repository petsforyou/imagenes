# Reels «lo que nos hace distintos» (pedido de María, 19/11/2026) — MONTADOS, NADA PROGRAMADO: falta el sí de María

Seis reels de ejemplo, sin voz, 1080×1920, montados en el PC con `montar_todo.py` (usa `herramientas/montar_reel.py`). Guiones: `guion-pfy-*.json`. Fotogramas vistos: `fotogramas-pfy-*.jpg`. Sin precios (suben el 1/12). Sin «Black Friday».

Vídeos (repo público, tras el push): `https://raw.githubusercontent.com/petsforyou/imagenes/main/videos/<nombre>.mp4`

| n.º | día 20:30 (propuesta) | nombre del vídeo | gancho (fórmula) | música |
|---|---|---|---|---|
| 1 | sáb 21/11 | pfy-lo-que-no-vendemos | Tres cosas que esta tienda de mascotas se niega a vender. (6) | historias-emocionante-2 |
| 2 | lun 23/11 | pfy-aqui-todos-cuentan | En cada hogar del mundo hay un pequeño amigo que nos acompaña en la vida. (7, con el lema de María) | historias-emocionante-3 |
| 3 | jue 26/11 | pfy-nunca-vendemos-animales | Somos una tienda de mascotas. Y no vendemos mascotas. (3) | historias-emocionante |
| 4 | dom 29/11 | pfy-sal-de-ruta-con-tu-perro | Llegas con tu perro… y el cartel dice «perros no». (2) | mundo-animal-aventura |
| 5 | mié 2/12 | pfy-comer-de-verdad | Lee la etiqueta de su comida. ¿Reconoces los ingredientes? (2) | salud-tranquila |
| 6 | sáb 5/12 | pfy-hecho-aqui | Tres marcas españolas. La tercera le pone su nombre. (6) | producto-alegre |

Hueco: 20:30 (el de anuncios; los anuncios de producto son martes y viernes; los de grabado con nombre, 22, 25 y 28/11, 1, 4, 7, 10, 13 y 16/12: no se pisa ninguno). Mirado el 19/11 a las 15:45: las seis 20:30 libres en Metricool (solo pines de Pinterest a las 19:30 y 21:30 = 1 h justa) y en Postiz (vecinos 18:00/18:30 y 22:30). Las rutinas rellenan huecos cada 2 días: VOLVER A MIRAR cada día antes de programar.
Redes: Facebook, Instagram y YouTube por Postiz (n8n `pfyPostizPublicar1`); TikTok y Pinterest por Metricool (marca 7728783). Después, releer las dos colas.
«Hecho aquí» va el último (5/12) porque M!MADO está de vacaciones hasta el 4/12 y hoy solo tiene 1 producto activo (el champú sólido, el que sale en el reel).

Duraciones: 23,4 · 28,2 · 22,0 · 24,8 · 24,2 · 23,2 s. `comprobar_reel.py`: APTO los seis. Sonido sin escuchar (misma música y mezcla de siempre).
Reel 2 rehecho el 19/11 con el lema de María («En esta tienda cabemos todos… Por eso estamos en 48 países… Si hay algún pequeño amigo que nos falte, escríbenos»; dice «estamos en», palabras suyas) y reel 4 con senderismo, travesías y autocaravana (README de la app). 48 países (mercados ACTIVE de Shopify: 29 países con mercado propio + 19 de «Unión Europea»; dato de esa sesión, no releído aquí). Es «enviamos a», nunca «clientes en».
Pegas conocidas: los reels 3 y 4 comparten cuatro imágenes (las de la app de rutas); si molesta, se cambian las del 3. El reel 6 enseña el champú de M!MADO, hoy su único producto activo.

## Datos comprobados el 19/11/2026 (web pública petsforyou.es, products.json y pages.json)
- Jaulas de hámster para vivir a la venta: 9, todas de 100 × 50 cm de suelo o más (la menor: 100 × 50 × 50 y 100 × 50 × 52,5). OJO: hay además una «Jaula de viaje para hámster con botella de agua» (transportín pequeño): por eso el reel dice «jaulas pequeñas para que viva un hámster».
- Arneses para conejo o animales pequeños: 0 productos con «arnés» en Hámsters, Mascotas pequeñas, Conejos y Hurones.
- Animales: la página Adopta dice «No vendemos animales ni lo haremos nunca», «Cada semana difundimos gratis un animal que busca casa» y «el dinero va directo a la protectora y nunca pasa por Petsforyou».
- Secciones por especie con productos: Hámsters 142, Hurones 28, Gallinas 19, Reptiles y tortugas 40, Peces 37, Pájaros 86, Conejos 66, Conejillos de Indias 38, Chinchillas 17, Perros 1.452, Gatos 853.
- App «Rutas con tu peludo»: en pruebas cerradas (Play Alpha y TestFlight), NO se puede descargar en abierto: el reel pide probadores por contacto@. Lo que dice (rutas a pie con perro por Europa, guardadas sin cobertura, campings y normas de cada país) sale del README de la app y de su política de privacidad en la web.
- Marcas españolas: colecciones AriBabi (34), M!MADO (1 activo hoy) y Mascotas Y Max (16). «Hecho a mano en España» y «personalizado con su nombre» salen de los títulos de las fichas de Mascotas Y Max. De AriBabi y M!MADO NO se dice dónde se fabrican (sin comprobar).
- Comida natural: cruda/BARF = 13 productos, todos de CRU (afiliado); cocinada = 12 propios (Puromenu, solo península) + 18 de afiliado. Sin promesas de salud. El texto lleva el aviso «Enlace de afiliado».

## Imágenes
Biblioteca de Drive (Lumina, IA; carpeta `bib/`), fotos reales de las fichas de Shopify (`prod/`) y fotos libres de Openverse (`cand/`, créditos abajo). Ningún animal en adopción real.
Créditos de las fotos libres: gallina, leoncillo sabino (CC BY 2.0); hámster en jaula, cdrussorusso (CC BY 2.0); periquitos, PuppiesAreProzac (CC BY-SA 2.0); conejo, Waranya Mooldee (CC0, StockSnap); cuenco de pienso, mrdorkesq (CC BY-SA 2.0); mano y pata, Egan Snow (CC BY-SA 2.0); persona y perro, smerikal (CC BY-SA 2.0). Todas de Flickr salvo la de StockSnap.

## Textos de publicación (máx. 5 hashtags)

### 1 · pfy-lo-que-no-vendemos — título: Tres cosas que esta tienda de mascotas se niega a vender
Tres cosas que esta tienda de mascotas se niega a vender.

Jaulas pequeñas para que viva un hámster: aquí la más pequeña mide 100 × 50 cm de suelo.
Arneses para conejos y otros animales pequeños.
Y animales: ninguno, nunca. A los que buscan casa los difundimos gratis.

Si a ellos no les hace bien, aquí no se vende.

Imágenes ilustrativas. Fotos: cdrussorusso (CC BY 2.0) y W. Mooldee (CC0).

#bienestaranimal #hamsters #conejos #adoptanocompres #petsforyou

### 2 · pfy-aqui-todos-cuentan — título: En cada hogar del mundo hay un pequeño amigo
En esta tienda cabemos todos.

En todos los hogares del mundo hay un pequeño amigo que nos acompaña en la vida. A veces es un hámster. A veces, un hurón, una gallina, una tortuga, un pez, un pájaro, un conejo… o un perro y un gato.

Por eso estamos en 48 países y por eso todos tienen aquí su sección. Si no es así y hay algún pequeño amigo que nos falte, escríbenos.

Imágenes ilustrativas. Fotos: leoncillo sabino (CC BY 2.0) y PuppiesAreProzac (CC BY-SA 2.0).

#mascotas #hamsters #hurones #gallinas #petsforyou

### 3 · pfy-nunca-vendemos-animales — título: Somos una tienda de mascotas. Y no vendemos mascotas
Somos una tienda de mascotas. Y no vendemos mascotas.

Un animal no es un producto. Por eso cada semana difundimos gratis a uno que busca casa.

¿Quieres ayudar? Dona directamente a su protectora: el dinero nunca pasa por nosotros.

Su final feliz no se compra. Se adopta. Mira quién busca casa: enlace en la bio.

Imágenes ilustrativas. Fotos: Egan Snow y smerikal (CC BY-SA 2.0).

#adoptanocompres #adopcion #protectoras #bienestaranimal #petsforyou

### 4 · pfy-sal-de-ruta-con-tu-perro — título: Llegas con tu perro… y el cartel dice «perros no»
Llegas con tu perro… y el cartel dice «perros no».

Estamos haciendo una app para acabar con eso: Rutas con tu peludo. Rutas a pie con perro por toda Europa (senderismo y travesías), que se guardan y se abren sin cobertura, con apartado de autocaravana y las normas de cada país.

Está en pruebas (Android y iPhone). ¿La pruebas antes que nadie? Escríbenos a contacto@petsforyou.es.

Imágenes ilustrativas creadas con IA.

#viajarconperro #rutasconperro #senderismoconperro #perros #petsforyou

### 5 · pfy-comer-de-verdad — título: Lee la etiqueta de su comida. ¿Reconoces los ingredientes?
Lee la etiqueta de su comida. ¿Reconoces los ingredientes?

En la comida natural se ven a simple vista. Cruda (BARF): carne y verduras sin cocinar. Cocinada: lista para servir. Y snacks naturales deshidratados.

Si quieres probar, haz el cambio poco a poco y consúltalo antes con tu veterinario.

Toda la alimentación natural, para perros y gatos: enlace en la bio.

Enlace de afiliado: parte de esta sección son productos de otras tiendas y, si compras desde nuestro enlace, nos llevamos una pequeña comisión sin coste para ti. Foto del cuenco: mrdorkesq (CC BY-SA 2.0).

#comidanatural #barf #perros #gatos #petsforyou

### 6 · pfy-hecho-aqui — título: Tres marcas españolas. La tercera le pone su nombre
Tres marcas españolas. La tercera le pone su nombre.

AriBabi: collar, correa y portabolsas a juego, con diseños propios y mucho color.
M!MADO: champú sólido con aloe vera para perros y gatos.
Mascotas Y Max: cuero hecho a mano en España, con su nombre grabado si quieres.

Las tres están en Petsforyou: enlace en la bio.

Imágenes ilustrativas en la primera y la última escena.

#marcasespañolas #hechoenespaña #perros #mascotas #petsforyou

## Avisos para María (encontrados al comprobar; no se ha tocado nada)
1. La «Jaula de viaje para hámster con botella de agua» está activa. Es un transportín, pero se llama «jaula» y es pequeña: quien vea el reel 1 puede echárnoslo en cara. Propuesta: llamarla «Transportín de viaje para hámster».
2. Existe un reel de consejos (G08, vídeo `nov-g08.mp4`) que dice «Para pasear, mejor un arnés bien ajustado» hablando de conejos y cobayas. Choca con «no vendemos arneses para conejos». El índice de la biblioteca lo fechaba el 23/11, pero ese día NO está en la cola (mirado 19/11): sin comprobar si ya salió o si está en otra fecha. Si sigue programado, conviene quitarlo.
3. «Cada semana difundimos gratis un animal» lo dice la web; si ahora no sale uno cada semana, cambiar la frase del reel 3 por «Difundimos gratis a los que buscan casa».

## PROGRAMADOS el 19/11/2026 ~16:27 (sí de María: «Sí, prográmalos»)
Los seis, a las 20:30 de su día. Postiz (Facebook, Instagram, YouTube): n8n `pfyPostizPublicar1`, ejecuciones 1056-1061, respuesta 201 con 3 postId cada una; cola del 5/12 releída (ejecución 1062): las 3 redes en QUEUE a las 19:30 UTC. Metricool (TikTok y Pinterest, PENDING en la respuesta): 434372863 (21/11), 434372907 (23/11), 434372997 (26/11), 434373069 (29/11), 434373133 (2/12), 434373179 (5/12).
Para quitar uno: Metricool, pasarlo a borrador con `updateScheduledPost`; Postiz, desde https://redes.petsforyou.es.

## Dos reels más (pedidos por María el 19/11 al dar el sí) — MONTADOS, SIN PROGRAMAR
| nombre | gancho (fórmula) | música | duración |
|---|---|---|---|
| pfy-marcas-del-mundo | Buscamos marcas por medio mundo. Nos quedamos con estas. (5) | producto-alegre | 23,6 s |
| pfy-adopcion-sin-juzgar | ¿Adoptado o elegido? Aquí no juzgamos a nadie. (3) | historias-emocionante-4 | 20,6 s |

María pidió «marcas exclusivas»: NO se dice «exclusivas» porque no está comprobado que solo las vendamos nosotros. Lo que se dice de cada marca (país, hecho a mano, talleres locales) sale de la página «Nuestras marcas» de la web: Bestia (Bulgaria), Purré (Polonia), Mellow (Cracovia), Pawsome Pets (Nueva York), Lilly+Dash (Melbourne), Fur & Whiskers (Australia). Fotos reales de sus fichas.
Adopción: palabras de María («hay veces que es mejor elegir a nuestro compañero, por compatibilidad, por salud, y no tenemos por qué quedarnos solos… no juzgamos a nadie»). OJO: los reels 1 y 3 ya programados llevan #adoptanocompres y «Su final feliz no se compra. Se adopta»; si María quiere el tono «no juzgamos», conviene cambiar ese hashtag por #adopcion.
Huecos: el 30/11 y el 3/12 hay anuncio de Navidad a las 20:00 (20:30 no vale). 20:30 libre en Metricool el dom 6/12 (mirado 19/11); Postiz sin mirar.

### pfy-marcas-del-mundo — título: Buscamos marcas por medio mundo. Nos quedamos con estas
Buscamos marcas por medio mundo. Nos quedamos con estas.

Bestia, de Bulgaria, para perros grandes y fuertes. Purré, de Polonia, cosido en talleres locales. Mellow, de Cracovia, con lana natural y hecho a mano. Pawsome Pets, de Nueva York. Lilly+Dash, de Melbourne. Fur & Whiskers, de Australia.

Es nuestra selección Premium: enlace en la bio.

#mascotas #perros #gatos #hechoamano #petsforyou

### pfy-adopcion-sin-juzgar — título: ¿Adoptado o elegido? Aquí no juzgamos a nadie
¿Adoptado o elegido? Aquí no juzgamos a nadie.

Promovemos la adopción: difundimos gratis a los que buscan casa, y nunca venderemos animales.

Pero hay veces que es mejor elegir a nuestro compañero, por compatibilidad o por salud. Y nadie tiene por qué quedarse solo.

Venga de donde venga, aquí tiene su sitio.

Imágenes ilustrativas. Foto: Egan Snow (CC BY-SA 2.0).

#adopcion #mascotas #perros #gatos #petsforyou

## Los dos nuevos, PROGRAMADOS el 19/11 ~16:43
- 19/11 ~16:43 · reels espíritu, los dos nuevos PROGRAMADOS (María: «Sí, prográmalos»): pfy-adopcion-sin-juzgar el dom 6/12 20:30 y pfy-marcas-del-mundo el mié 9/12 20:30. Huecos mirados antes en Metricool (vacío 19:35-21:25) y Postiz (ejecuciones 1063-1064: vecinos 9:00 y 18:30). Postiz: ejecuciones 1065 y 1066, 201 con 3 postId cada una (cola sin releer después). Metricool (TikTok y Pinterest, PENDING): 434394524 y 434394563. Pendiente de María: cambiar o no #adoptanocompres en los reels del 21/11 y 26/11.

## Tres reels de ideas de Claude (María, 19/11: «haz los tres reels de tus ideas») — MONTADOS, SIN PROGRAMAR
Todo lo que dicen sale de la página «Quiénes somos» de la web (leída el 19/11) y, lo del carrito, de «Nuestras marcas». APTO los tres; un fotograma por escena visto. Sin nombre ni datos personales de María.
| nombre | gancho (fórmula) | música | duración |
|---|---|---|---|
| pfy-contesto-yo | ¿Quién hay al otro lado cuando escribes a una tienda? (1) | superacion-inspiradora-3 | 21,0 s |
| pfy-plazos-honestos | ¿Cuántas veces te han dicho «llega mañana»… y no llegó? (2) | curiosidades | 21,4 s |
| pfy-precios-claros | ¿Por qué sube y baja el precio de lo que compras para tu mascota? (1) | blog-suave | 21,0 s |

Peros antes de programar:
- «Si escribes, contesto yo»: vale para el correo; los comentarios de las redes los contestan las rutinas automáticas. No decir «no hay robot».
- «Precios claros» («si el proveedor baja el precio, yo lo bajo», «sin precios inflados»): los precios SUBEN el 1/12 y la web lleva la barra «Black Friday: precios rebajados» hasta el 30/11. Publicarlo pegado a esas fechas puede volverse en contra: mejor a mediados de diciembre o no publicarlo.
- «Envío gratis a toda España, sin mínimo» lo dice la web; no lo he comprobado en el carrito.

### pfy-contesto-yo — título: ¿Quién hay al otro lado cuando escribes a una tienda?
¿Quién hay al otro lado cuando escribes a una tienda?

Aquí no hay centro de atención al cliente. Hay una persona, la misma que eligió cada producto pensando en sus propios animales. No soy una gran superficie.

Si escribes, contesto yo: contacto@petsforyou.es

Imágenes ilustrativas creadas con IA.

#mascotas #tiendademascotas #perros #gatos #petsforyou

### pfy-plazos-honestos — título: ¿Cuántas veces te han dicho «llega mañana»… y no llegó?
¿Cuántas veces te han dicho «llega mañana»… y no llegó?

Aquí, si algo tarda dos semanas, lo ves antes de comprar: el plazo de tu pedido sale en el carrito, antes de pagar. Prefiero decírtelo a que te lleves la sorpresa.

Y el envío es gratis a toda España, sin mínimo de compra.

Imágenes ilustrativas creadas con IA.

#mascotas #comprasonline #perros #gatos #petsforyou

### pfy-precios-claros — título: ¿Por qué sube y baja el precio de lo que compras para tu mascota?
¿Por qué sube y baja el precio de lo que compras para tu mascota?

Detrás hay un proveedor y un transporte. Si el proveedor baja el precio, yo lo bajo. Si el transporte se abarata, también. Sin precios inflados.

Y el envío es gratis a toda España, sin mínimo de compra.

Imágenes ilustrativas en las dos últimas escenas.

#mascotas #preciosclaros #perros #gatos #petsforyou

## DESCARTADOS por María (19/11)
- 19/11 ~17:40 · reels espíritu, criterio de María: los tres reels de ideas (contesto-yo, plazos-honestos, precios-claros) NO se programan. No quiere que se vea que es una sola persona, y no puede afirmar plazos honestos ni precios claros («ha sido un caos desde que empecé, aunque no hay voluntad de que no sea así»). Aviso dado: la página «Quiénes somos» de la web sí dice las tres cosas; sin tocar.

## Seis reels más (María, 19/11 tarde: ideas 4, 5 y 6, la app con todo y la app de rutas) — MONTADOS, SIN PROGRAMAR
En plural («nosotros»), sin «una sola persona» y sin prometer plazos ni precios. APTO los seis; un fotograma por escena visto.
| nombre | gancho | duración | de dónde sale lo que dice |
|---|---|---|---|
| pfy-cumple-la-ley | ¿Seguro que tu mascota cumple la ley? | 20,8 s | ficha de la app en App Store y Google Play (leídas 19/11, las dos públicas) |
| pfy-tambien-explicamos | Antes de comprarle nada, ¿sabes qué necesita de verdad? | 21,0 s | blog (sitemap), ebooks «Razas de perros», «Razas de gatos», «El primer año de tu cachorro», guía de tallas en fichas de ropa |
| pfy-para-ti-tambien | ¿Y para ti? Tú también eres de su familia. | 20,0 s | colección «Accesorios para amantes de mascotas» (fotos reales) |
| pfy-app-todo | Una app de mascotas que no es solo una tienda. | 21,6 s | ficha de la app: ley, viajar por Europa, veterinarios de urgencias, blog, series, asistente |
| pfy-app-rutas-por-dentro | ¿Esa ruta le va bien a tu perro? Esta app te lo dice. | 23,8 s | README y política de privacidad de «Rutas con tu peludo» |
| pfy-app-rutas-autocaravana | ¿Tu autocaravana pasa por ahí? Esta app te avisa antes. | 23,6 s | código de la app (textos es.json y `src/caravaning`) |

Ojo con la app de rutas: sigue en pruebas cerradas, los dos reels lo dicen y piden escribir a contacto@. María pidió «gasolineras de toda Europa, precios GLP»: en el código los precios oficiales solo están en España y Francia (`PAISES_CON_PRECIO = ['ES','FR']`); en el resto, las gasolineras y el GLP salen de OpenStreetMap sin precio. Por eso el reel dice «Gasolineras con GLP en el mapa» y «precios del día en España y Francia». Avisos de altura: «Pon la altura, el peso y el largo… te avisaremos si el acceso tiene un gálibo o un límite de peso» (texto de la app). Fronteras: apartado «Cruzar fronteras con tu perro». No comprobado en un móvil: solo en el código.
El asistente de la app es de inteligencia artificial (lo dice su ficha); el reel dice «un asistente que te ayuda a elegir».
