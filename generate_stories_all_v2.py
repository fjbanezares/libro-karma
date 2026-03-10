import os
import re
from deep_translator import GoogleTranslator

# Target languages
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

stories = {
    "01_esfuerzo_desinteresado": {
        "title": "La Semilla del Constructor",
        "story": "Imagina a un humilde constructor que, bajo un sol abrasador, levantaba un muro de piedra para proteger a su aldea. No cobraba nada, solo lo hacía por amor a su gente. Sus manos sangraban, y muchos le llamaban tonto por trabajar para los demás...\n\nPero cada piedra pesada que cargaba, sin saberlo, no solo construía un muro, sino que forjaba sus propios hombros. Estaba esculpiendo en su alma la fuerza de un gigante.\n\nEl tiempo pasó como un suspiro, y en otra vida, este mismo hombre despertó en una ciudad de hierro y asfalto. Allí vio un pesado vagón a punto de aplastar a un niño. Sin dudarlo, interpuso sus brazos y detuvo el amasijo de metal. La fuerza no vino de la nada; era el músculo espiritual de aquel constructor que regresó a él... para que pudiera ser el milagro que alguien estaba suplicando."
    },
    "02_fidelidad_y_familia": {
        "title": "El Espejo de las Promesas",
        "story": "Había una vez un hombre encantador que iba de pueblo en pueblo, enamorando corazones y luego marchándose en la oscuridad, dejando tras de sí solo lágrimas e ilusiones rotas. Creía ser libre como el viento...\n\nSin embargo, el universo tiene una memoria infinita. Años más tarde, o quizá en otra vida, este mismo hombre se encontró sentado frente a una mesa enorme, llena de manjares, pero completamente solo. Ningún amigo le visitaba, ningún amor se quedaba a su lado. Sentía un frío en el alma que ningún fuego podía calentar.\n\nAquella soledad no era un castigo cruel del cielo. Eran las mismas lágrimas que él había dejado caer, ahora convertidas en un mar que lo separaba del mundo. Comprendió entonces que cuando rompía el corazón de otro, en realidad, estaba vaciando el suyo propio. Y al derramar su primera lágrima sincera, el universo, con paciencia infinita, le entregó la primera semilla para por fin aprender a amar."
    },
    "03_generosidad_y_prosperidad": {
        "title": "El Pan de la Vida",
        "story": "Cuentan de una pobre campesina que apenas tenía un mendrugo de pan para cenar. Al escuchar un golpe en su puerta, encontró a un viajero agotado y hambriento. Sin pensarlo un segundo, partió su único pan y se lo entregó con una sonrisa cálida...\n\nLo que ella no podía ver es que, en el reino de lo invisible, dar no es quitar. Cada miga entregada con amor verdadero es una semilla plantada en la tierra fértil de la eternidad.\n\nY el cosmos le devolvió la cosecha. Tiempo después, la vemos caminando como una gran señora, dueña de inmensos graneros que alimentan a naciones enteras. No era la suerte ni el azar comercial; era el pan de aquella fría noche, que al entregarlo con el corazón, se multiplicó hasta el infinito, enseñándonos que solo poseemos para siempre... aquello que damos a los demás."
    },
    "04_respeto_por_la_vida": {
        "title": "El Suspiro del Viento",
        "story": "Un verdugo de corazón de hielo levantaba su espada sin emoción, cortando vidas como quien poda malas hierbas. Se creía el dueño del destino, superior a las vidas temblorosas que suplicaban piedad bajo su sombra...\n\nPero la balanza de la vida es justa e inquebrantable. Un día, su espíritu despertó siendo un frágil soldado acorralado en una trinchera. El estruendo de las bombas sacudía la tierra, y él se encogía de puro terror, sintiendo cómo cada suspiro podía ser el último.\n\nEl verdugo estaba aprendiendo, gota a gota, lo que era ser la presa. A través de su propio temblor, por fin pudo comprender la sacralidad preciosa de cada aliento. El universo no lo humillaba por venganza; le estaba rompiendo la coraza, para enseñarle, entre lágrimas de miedo, que toda vida merece ser protegida y amada."
    },
    "05_pureza_mental": {
        "title": "Las Sombras y la Luz",
        "story": "Había un hombre de palabras oscuras y pensamientos envidiosos. Disfrutaba susurrando mentiras y sembrando dudas, manchando la paz mental de cada persona que cruzaba en su camino. Se reía al ver a los demás confundidos y tristes...\n\nPero las sombras que creamos nunca nos abandonan del todo; nos esperan pacientemente. Y así, él acabó atrapado en una celda que no tenía rejas, sino terribles angustias y miedos invisibles. Su mente se llenó de un ruido ensordecedor que no lo dejaba dormir.\n\nEran todos los suspiros de desesperanza que él mismo había provocado, regresando a su origen. Sin embargo, en medio del tormento oscuro, el cielo le dejó una pequeña rendija... para que cuando por fin anhelara la luz pura con toda su alma, aprendiera el inmenso valor de la paz, y pudiera renacer para calmar la mente de los demás."
    },
    "06_sobriedad_y_claridad": {
        "title": "El Vaso Vacío",
        "story": "Un tabernero ambicioso mezclaba los licores para aturdir la mente de los viajeros. Se llenaba los bolsillos de monedas, mientras veía cómo sus clientes perdían su dignidad, su claridad y, muchas veces, su camino a casa...\n\nPero en la aritmética divina, robar el entendimiento a otro tiene un peso doloroso. Así que un día, el tabernero comenzó a sentir una niebla constante en su propia cabeza. No lograba pensar con claridad. El sueño huía de sus ojos y la lucidez se le escapaba como agua entre los dedos.\n\nEstaba cargando con toda la confusión que él mismo vendió en sus copas. Y mientras tropezaba en su propia ceguera intelectual, nació en él una sed inmensa por la verdad. Entendió que la claridad de la mente es un regalo sagrado de Dios, y prometió no volver a nublar jamás la luz de un hermano."
    },
    "07_manos_del_mal": {
        "title": "Las Manos del Alfarero",
        "story": "Imagina unas manos fuertes, hechas por el Creador para acariciar, ayudar y construir. Pero un joven decidió usar las suyas solo para golpear y robar el pan ajeno. Creía que sus puños eran su mayor poder contra el mundo...\n\nEl gran tejedor de destinos, con tristeza infinita, le retiró ese regalo. En su siguiente latido en la historia, despertó como una criatura que debía arrastrarse por el polvo de la tierra. No tenía manos para defenderse; no tenía cómo abrazar. Estaba completamente indefenso, viviendo la misma fragilidad a la que sometió a sus víctimas.\n\nY al verse sin el medio para ayudar al prójimo, valoró hasta las lágrimas la belleza del tacto. Esta dolorosa lección no era una condena vacía, sino el horno donde su alma se ablandaba... garantizando que, cuando volviera a tener manos, nunca más se cerrarían en un puño, sino que siempre estarían abiertas para acariciar y sanar."
    },
    "09_frio_egoismo": {
        "title": "El Frío de las Monedas",
        "story": "Un rico mercader se sentaba sobre montañas de monedas de oro, mientras cerraba la puerta a niños descalzos que tiritaban en la nieve. «Lo mío es mío», repetía, creyendo que su tesoro lo protegería de la muerte y del dolor...\n\nPero el egoísmo congela el alma. Al encadenar su riqueza, se separó de la gran familia humana. Tiempo después, la rueda de la vida giró, y él se encontró a sí mismo siendo un vagabundo perdido en una calle sin nombre. Nadie lo miraba. Nadie le daba calor.\n\nAquel mendigo que sufría el terrible frío del abandono, era él experimentando el mismo hielo que creó. Solo rompiéndose en llanto al descubrir el dolor del hambre, logrará descongelar su corazón... para comprender que el mayor tesoro no es retener, sino compartir el pan bajo el mismo techo del amor."
    },
    "10_infierno_sombras": {
        "title": "El Vestido de Fuego",
        "story": "Había un hombre implacable que construyó su poder sobre la sangre y el llanto de los inocentes. Creía que la crueldad era un escudo que nadie podría traspasar. Se reía de las lágrimas y no sentía ninguna piedad en el corazón...\n\nPero la vida es como un gran eco. Todo lo que lanzamos al abismo vuelve a nosotros con la misma fuerza vibratoria. Por eso, al cerrar los ojos, no encontró la nada; se halló atrapado en un valle de un calor asfixiante y un terror profundo. No eran castigos inventados ni demonios ajenos...\n\nEran todas y cada una de las agonías, miedos y gritos de quienes asesinó, concentrados alrededor suyo como un fuego abrasador que le gritaba la verdad. A través de este calor insoportable, la roca de su insensibilidad se fue fundiendo... hasta que, arrodillado frente a su propio dolor, suplicó el don de la compasión."
    },
    "11_mirada_desprecio": {
        "title": "El Espejo Roto",
        "story": "Cierta persona caminaba siempre mirando por encima del hombro, con la nariz en alto, tratando a los menos afortunados como si fueran basuras molestas. Creía en su propia perfección, incapaz de notar el dolor en los ojos de quienes humillaba...\n\nPero en el inmenso tapiz de Dios, todos somos hilos de la misma tela. Lastimar la existencia del otro es despreciarnos a nosotros mismos. Y así, el universo le llevó a una cama fría, atado a una enfermedad que lo desfiguraba y alejaba a todos a su alrededor.\n\nSe convirtió en el ser rechazado que él mismo despreciaba. Sus gritos por una simple caricia humana le rasgó por fin el velo de la soberbia. Comprendió el profundo valor de sentirse igual y hermanos. Al sollozar en su dolorosa soledad, nació la verdadera humildad... que lo haría invencible en el amor verdadero."
    },
    "12_peso_injusticia": {
        "title": "El Patrón de Arcilla",
        "story": "Era un jefe duro que robaba el sudor de sus jornaleros, pagándoles con humillación y migajas. Mientras él dormía en sábanas de seda fina, ellos apenas tenían cómo alimentar a sus familias. Se creía astuto y próspero...\n\nPero la balanza invisible del universo mide la justicia con exactitud. De la noche a la mañana, sus riquezas se esfumaron. Se vio en la calle, mendigando un rincón oscuro donde descansar, sintiendo el desprecio y el rigor de quienes pasaban a su lado.\n\nTuvo que ensuciar sus manos con el barro, sudar sangre por unas pocas monedas, y sentir la impotencia quemándole el pecho. Era necesario que el amo se hiciera esclavo, para que entendiera que el sustento es sagrado, que el trabajador merece honra... y que la verdadera riqueza es prosperar sin pisar jamás a nadie."
    }
}

def translate_es(text_es):
    d = {"en": get_trans(text_es, "en", "en")}
    for code, g_code in lang_map.items():
        d[code] = get_trans(text_es, code, g_code)
    return d

def get_trans(text_es, lang_code, g_code):
    try:
        if lang_code == "en": g_code = "en"
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error translating to {lang_code}: {e}")
        return text_es

def format_paragraphs(text_content, lang_class):
    # Split text into paragraphs by \n\n
    paragraphs = text_content.split('\n\n')
    formatted = ""
    for p in paragraphs:
        # Wrap each paragraph
        formatted += f'<p class="{lang_class}" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">{p}</p>\n                '
    return formatted.strip()

def build_block(d_t, d_s):
    html = f'<div class="story-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">\n'
    # Titles
    for code in ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]:
        html += f'                <h3 class="{code}" style="color: var(--gold); text-align: center; font-family: \'Cinzel\', serif; margin-bottom: 2rem;">{d_t[code]}</h3>\n'
    
    # Text
    for code in ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]:
        html += format_paragraphs(d_s[code], code) + "\n                "
    
    html += "</div>"
    return html

def inject(chapter, blk):
    filepath = f"{chapter}/web/index.html"
    if not os.path.exists(filepath): return
    with open(filepath, "r") as f:
        content = f.read()
    
    # First, let's remove the previously injected block
    old_block_pattern = r'<div class="story-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem;">.*?</div>(?=\s*<div class="moral fade-in">)'
    
    new_content = re.sub(old_block_pattern, '', content, flags=re.DOTALL)
    
    # Now inject the new one before `<div class="moral fade-in">`
    new_content = re.sub(r'(\s*<div class="moral fade-in">)', r'\n            ' + blk + r'\1', new_content)
    
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Injected new moving parables in {chapter}")
    else:
        print(f"Could not inject into {chapter}")

for chapter, payload in stories.items():
    print(f"Processing story for {chapter}...")
    trans_t = {"es": payload["title"]}
    trans_t.update(translate_es(payload["title"]))
    
    trans_s = {"es": payload["story"]}
    trans_s.update(translate_es(payload["story"]))
    
    blk = build_block(trans_t, trans_s)
    inject(chapter, blk)
