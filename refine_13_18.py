import os
import re
import json
from deep_translator import GoogleTranslator

# Target languages
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

import time

def get_trans(text_es, lang_code, g_code):
    try:
        if lang_code == "en": g_code = "en"
        for i in range(5):
            try:
                return GoogleTranslator(source='es', target=g_code).translate(text_es)
            except Exception as e:
                print(f"Retrying {lang_code}... attempt {i+1} error: {e}")
                time.sleep(3)
        return text_es
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

def trans_dict(text_es):
    d = {"es": text_es, "en": get_trans(text_es, "en", "en")}
    for code, g_code in lang_map.items():
        d[code] = get_trans(text_es, code, g_code)
    return d

def str_to_paragraphs(text):
    # This takes the string and wraps parts in <p>...</p> tags
    # Wait, in the HTML, we inject it into `<p class="...">`.
    # It's better to return a LIST of strings, each being a paragraph.
    parts = text.split('\n\n')
    return [p.strip() for p in parts if p.strip()]

def trans_paragraphs(paragraphs):
    # paragraphs is a list of ES strings.
    # Returns a dict of languages -> list of strings
    d = {"es": paragraphs}
    d["en"] = [get_trans(p, "en", "en") for p in paragraphs]
    for code, g_code in lang_map.items():
        d[code] = [get_trans(p, code, g_code) for p in paragraphs]
    return d

# Let's write the deeply spaced, parable-style stories. Max 3-4 paragraphs.
new_stories = {
    "13_amor_y_respeto": {
        "story_es": "Es una ley sutil e ineludible que nuestro fuero interno, tarde o temprano, cincela nuestro exterior. Aquel que camina por el mundo regando respeto, consideración y una sonrisa sincera, no pierde su esencia, sino que la multiplica...\n\nCuando ofrecemos amor incondicional a cada vida que se cruza en nuestro sendero, nuestra propia alma se ilumina desde lo invisible. Ese candor interno no se disuelve en el viento; por lo tanto, acaba aflorando a la superficie en las vidas venideras.\n\nAsí pues, el universo esculpe en la próxima encarnación un rostro hermoso, afable y sereno; un puente de belleza física y magnetismo compasivo que reflejará la pureza que el espíritu guardó para siempre.",
        "parable_text": "Había en un arrabal polvoriento un anciano cuyo rostro estaba surcado por profundas arrugas; sin embargo, quienes lo miraban hallaban siempre una paz inexplicable.\n\nÉl no poseía riquezas ni estatuas a su nombre, pero trataba tanto al magnate como al mendigo con idéntico y profundo respeto. Nadie sospechaba que, en los silenciosos telares del destino, esa constancia cálida estaba tejiendo la luz de su futuro.\n\nYa que el universo no reparte la belleza física como un mero lance del azar, sino como un pago ineludible del afecto que en el pasado esparcimos. Quien abriga el mundo con dulzura, terminará forzando a los astros a iluminar de belleza su propia carne."
    },
    "14_peso_deudores": {
        "story_es": "Recibir ayuda en tiempos de necesidad es humano, pero recostarse perpetuamente en el dolor y sacrificio ajeno —sin ofrecer jamás reciprocidad ni gratitud— genera un anclaje energético sombrío...\n\nEl confort obtenido a costa del sudor del hermano forja, de forma invisible, una pesada cadena en el pecho. Esta falsa ligereza exige un precio exacto cuando la balanza del cosmos pasa la factura.\n\nPor lo tanto, el transgresor es despojado de su paz en ciclos posteriores, experimentando una melancolía que no cesa, y un vacío emocional agobiante similar al peso de los favores que egoístamente consumió sin devolver.",
        "parable_text": "Un joven de modales complacientes no dudaba en exigir, día tras día, grandes favores, cobijo y recursos de quienes lo amaban. Él creía, en su soberbia, que el afecto ajeno era su derecho de nacimiento...\n\nPero, con el paso de los inviernos y a pesar de haber llenado sus graneros, comenzó a sentir un peso asfixiante sobre los hombros; una angustia sorda que ninguna distracción podía callar.\n\nAsí fue como descubrió, muy a su pesar, que todo el consuelo que tomamos del prójimo y nunca compensamos, se convierte irremediablemente en la pesada nostalgia que anclará al corazón el día de mañana."
    },
    "15_desperdicio_y_escasez": {
        "story_es": "Tener la fortuna de la prosperidad no debe ser jamás un escudo para la indiferencia ni el despilfarro. Cuando tiramos o despreciamos el alimento, ignorando olímpicamente que millones padecen hambre, quebramos nuestra conexión vital con la providencia...\n\nEste acto de absoluta arrogancia rasga los hilos dorados de la supervivencia. La soberbia de malgastar lo que nutre a los cuerpos no cae en saco roto; el universo lo registra como un profundo desprecio por la vida misma.\n\nYa que el balance divino exige respeto, quien tira el pan hoy será condenado mañana a sudar sangre, polvo y lágrimas en tierras yerras, solo para rogar por las migajas que en el pasado arrojó al lodo.",
        "parable_text": "Cuentan que un próspero terrateniente organizaba majestuosos banquetes donde se jactaba ordenando tirar a los perros grandes manjares intactos, tan solo para divertir a sus invitados con su opulencia...\n\nAquellos años de ceguera terminaron abruptamente al girar la Rueda. De pronto, se halló a sí mismo en un paramo desolado en una vida posterior, buscando agua entre grietas secas y rogando por un mísero bocado para sobrevivir a una fatiga devoradora.\n\nFue allí, entre el llanto y el polvo, donde comprendió su error: quien humilla a la tierra desperdiciando el fruto de su vientre, la tierra le humillará cerrándole el sustento."
    },
    "16_adiccion_y_ceguera": {
        "story_es": "Someter el prodigio sagrado de la lucidez mediante la sumisión a pócimas sedantes y adicciones oscuras es, tal vez, la claudicación existencial más triste. Entregarse a la embriaguez constante no es más que cegar los propios ojos espirituales...\n\nAcostumbrar nuestra consciencia a huir hacia el letargo y la confusión entorpece irremisiblemente el cerebro. Esta indolencia no solo daña el momento presente, sino que mutila el potencial cognitivo completo del alma.\n\nPor lo tanto, aquellos que deciden apagar voluntariamente su brillo intelectual en vida, arrastrarán en sus encarnaciones venideras una penumbra espesa, naciendo cautivos del letargo mental y de una incapacidad atroz para comprender el mundo que les rodea.",
        "parable_text": "Incapaz de lidiar con las heridas del mundo, un hombre decidió recluirse en las sombras de una taberna ahumada, ahogando su vitalidad en licores ardientes... Y así, noche tras noche, prefirió la oscuridad de la bruma a la gloria de estar vivo y despierto.\n\nPero los sentidos tienen memoria. Al rehusarse a ejercitar el milagro de la razón, la inteligencia lo fue abandonando como un río que se escurre entre los dedos.\n\nAl despertar a un nuevo ciclo, se descubrió perdido en una profunda neblina que nunca se disipaba. Y entendió, con amarga quietud, que quien rechaza el dolor embriagando el cerebro, también renuncia eternamente al placer de la luz."
    },
    "17_orfandad_filial": {
        "story_es": "Las raíces de nuestra encarnación son, por derecho divino, aquellos que nos han prestado su sangre. Quien voltea el rostro, reniega, o maldice a los padres que lo criaron, está talando el propio soporte sutil de su existencia...\n\nLa ingratitud filial corta indiscriminadamente aquel cordón dorado que nos ancla a la compasión cósmica. Es la afrenta capital contra aquellos que nos arroparon cuando no éramos más que llanto e indefensión.\n\nPor lo tanto, la justicia universal es drástica con quien desmiembra la familia natural: arroja invariablemente al infractor al próximo nacimiento sumido en la orfandad absoluta, el abandono y el llanto silencioso de no tener jamás unos brazos que lo contengan.",
        "parable_text": "Ataviado con ropas de seda y jactándose de haber 'forjado su propio destino', un joven adinerado cerró la pesada puerta a sus padres ancianos, riendo ante sus ruegos por cobijo, y arguyendo que ya no le eran útiles...\n\nLo que el joven soberbio ignoraba, es que el universo pesa las lágrimas de los padres sobre los hijos. Y al romper el vínculo por desdén, el telar cortó de tajo su continuidad protectora.\n\nCuando exhaló su último aliento y volvió a nacer, su primer respiro fue bajo la tormenta fría, abandonado cruelmente entre las piedras. Así, descubrió en la intemperie desgarradora, el valor infinito que encierra poder pronunciar la palabra 'madre'."
    },
    "18_pereza_laboral": {
        "story_es": "El mundo se sostiene sobre el pulso invisible y armónico de todos los seres que se esmeran en brindar su talento al servicio del prójimo. Escabullirse por sistema, defraudar la labor con indolencia y elegir holgazanear mientras los hermanos sostienen el peso, rompe el equilibrio...\n\nEsta patética artimaña de falsear el propio sudor agota el flujo de la abundancia reservada. Todo lo que eludimos forzosamente acaba amontonándose como una losa frente a nuestras oportunidades.\n\nPor lo tanto, quien no contribuye hoy ennobleciendo el trabajo, se topará invariablemente con que la vida le cierra todo acceso, siendo arrojado posteriormente a los pantanos cruentos de la miseria y a sufrir perpetuamente un agobiante desempleo.",
        "parable_text": "Un mozo ágil fue contratado en un gran taller rebosante de encargos, al amparo de un techo seguro. Sin embargo, dedicaba sus horas a esconder sus herramientas y dormitar bajo fardos, sintiéndose astuto por no cansar su cuerpo mientras los demás trabajaban hasta el ocaso...\n\nPero la astucia que se burla del esfuerzo no tarda en cobrar su ironía. Tras malgastar sus años de vigor renegando de su trabajo, el engranaje de su destino se estancó oxidado para siempre.\n\nLlegado un nuevo amanecer, la miseria lo encontró suplicando por una sola hora de faena dura, sentado bajo la lluvia frente a inmensos portones de hierro herméticamente cerrados; deseando, ahora más que nunca, limpiar el sudor de su frente que antaño tanto despreció."
    }
}

print("Translating massive refined multi-paragraph payload...")
compiled_data = {}
for chap, raw_texts in new_stories.items():
    print("Translating " + chap)
    
    # parse paragraphs
    story_es_paragraphs = str_to_paragraphs(raw_texts["story_es"])
    parable_es_paragraphs = str_to_paragraphs(raw_texts["parable_text"])
    
    trans_story_dict = trans_paragraphs(story_es_paragraphs)
    trans_parable_dict = trans_paragraphs(parable_es_paragraphs)
    
    compiled_data[chap] = {
        "story": trans_story_dict,
        "parable_text": trans_parable_dict
    }

# Also load existing titles to reuse them
with open("chapters_13_18_data.json", "r", encoding='utf8') as f:
    old_data = json.load(f)

for chap in new_stories.keys():
    old_data[chap]["story"] = compiled_data[chap]["story"]
    old_data[chap]["parable_text"] = compiled_data[chap]["parable_text"]

with open("chapters_13_18_data.json", "w", encoding='utf8') as f:
    json.dump(old_data, f, ensure_ascii=False)

# Now Let's update index.html for the 6 chapters
langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]

for ch in new_stories.keys():
    fpath = f"{ch}/web/index.html"
    if not os.path.exists(fpath): continue

    with open(fpath, "r", encoding='utf8') as f:
        html = f.read()

    data = old_data[ch]

    # Rebuild main story block
    main_story_html = f"""<div class="story-block fade-in">\n"""
    # For each paragraph, we output it. Wait, previously I had to output a complete block of 10 languages at once, 
    # but the simplest representation is paragraphs grouped by language or interspersed. 
    # Usually we intersperse grouped by lang so the lang selector works.
    
    # `data["story"]` is a dict { "es": [p1, p2, p3], "en": [p1, p2, p3] }
    # So for each lang, we make string of all paragraphs for that lang.
    for l in langs:
        for i, p in enumerate(data["story"][l]):
            if i == 0:
                main_story_html += f'                <p class="{l}"><span class="drop-cap">{p[0]}</span>{p[1:]}</p>\n'
            else:
                main_story_html += f'                <p class="{l}">{p}</p>\n'
    main_story_html += "            </div>"

    html = re.sub(r'<div class="story-block fade-in">.*?</div>', main_story_html, html, count=1, flags=re.DOTALL)

    # Rebuild parable
    para_html = f"""<div class="story-block parable-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">\n"""
    for l in langs:
        para_html += f'                <h3 class="{l}" style="color: var(--gold); text-align: center; font-family: \'Cinzel\', serif; margin-bottom: 2rem;">{data["parable_title"][l]}</h3>\n'
    
    for l in langs:
        for p in data["parable_text"][l]:
            para_html += f'                <p class="{l}" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">{p}</p>\n'
    para_html += "            </div>"

    html = re.sub(r'<div class="story-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">.*?</div>', para_html, html, count=1, flags=re.DOTALL)
    # in case it was already replaced with `parable-block`
    html = re.sub(r'<div class="story-block parable-block fade-in".*?</div>', para_html, html, count=1, flags=re.DOTALL)

    # Now inject the beautiful "art.jpg" at the bottom.
    # We will put it right after the `.translation-box` inside `.original-inspiration`.
    # Wait, the prompt says "las imagenes que hass hecho son preciosas pero que las pongas al final". 
    # Putting it before the translation box or after the `.original-inspiration` div? 
    # Let's put it right after `.original-inspiration` ends, before `<div class="linktree-subtle`
    
    # First, clear it if it's already there (to be idempotent)
    html = re.sub(r'<div class="final-art fade-in".*?</div>\s*', '', html, flags=re.DOTALL)

    art_html = f"""
            <div class="final-art fade-in" style="text-align: center; margin-top: 4rem; margin-bottom: 2rem;">
                <img src="assets/art.jpg" alt="Obra de Arte Karma" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            </div>
    """
    
    # insert before <div class="linktree-subtle
    html = re.sub(r'(\s*<div class="linktree-subtle)', r'\n' + art_html + r'\1', html)

    with open(fpath, "w", encoding='utf8') as f:
        f.write(html)
    print(f"Updated full spacing and art injection for {fpath}")

print("Done part 3: Perfecting spacing, Jesus-style parables & Art placement.")
