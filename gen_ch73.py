#!/usr/bin/env python3
"""Regenerate Ch73 completely from Ch72 template with proper translations."""
import re, shutil, os
from deep_translator import GoogleTranslator

# Start fresh from Ch72
shutil.copy("72_favor_de_la_sombra/web/index.html", "73_el_arte_del_karma/web/index.html")
filepath = "73_el_arte_del_karma/web/index.html"
with open(filepath, "r") as f:
    html = f.read()

LANGS = {"en":"en","it":"it","zh":"zh-CN","ar":"ar","ru":"ru","de":"de","fr":"fr","ja":"ja","pt":"pt","vi":"vi"}
FLAGS = {"es":"🇪🇸","en":"🇬🇧","it":"🇮🇹","zh":"🇨🇳","ar":"🇦🇪","ru":"🇷🇺","de":"🇩🇪","fr":"🇫🇷","ja":"🇯🇵","pt":"🇵🇹","vi":"🇻🇳"}
LANG_NAMES = {"es":"Traducción Recreada","en":"Recreated Translation","it":"Traduzione Ricreata","zh":"重建的翻译","ar":"الترجمة المُعاد صياغتها","ru":"Воссозданный перевод","de":"Rekonstruierte Übersetzung","fr":"Traduction Recréée","ja":"再現された翻訳","pt":"Tradução Recriada","vi":"Bản Dịch Tái Hiện"}
ALL = ["es","en","it","zh","ar","ru","de","fr","ja","pt","vi"]
c_labels = {"es":"Causa","en":"Cause","it":"Causa","zh":"原因","ar":"سبب","ru":"Причина","de":"Ursache","fr":"Cause","ja":"原因","pt":"Causa","vi":"Nguyên nhân"}
e_labels = {"es":"Efecto","en":"Effect","it":"Effetto","zh":"影响","ar":"تأثير","ru":"Эффект","de":"Wirkung","fr":"Effet","ja":"効果","pt":"Efeito","vi":"Tác dụng"}

def tr(text, tgt):
    try: return GoogleTranslator(source='es', target=tgt).translate(text)
    except Exception as e:
        print(f"  WARN: translation failed for {tgt}: {e}")
        return text

# ═══ STEP 1: METADATA & TITLES ═══
print("Step 1: Metadata & Titles...")
reps = {
    "LXXII": "LXXIII", "第七十二章": "第七十三章", "第72章": "第73章",
    "الفصل الثاني والسبعون": "الفصل الثالث والسبعون",
    "CHƯƠNG LXXII": "CHƯƠNG LXXIII",
    "El Favor de la Sombra": "El Arte del Karma",
    "Shadow's Favor": "The Art of Karma",
    "Il favore dell'ombra": "L'arte del Karma",
    "暗影的青睐": "业力的艺术",
    "فضل الظل": "فن الكارما",
    "Благосклонность Тени": "Искусство Кармы",
    "Gunst des Schattens": "Die Kunst des Karma",
    "Faveur de l'Ombre": "L'Art du Karma",
    "シャドウの好意": "カルマの芸術",
    "Favor da Sombra": "A Arte do Karma",
    "Sự ủng hộ của Shadow": "Nghệ Thuật Của Nghiệp",
}
for old, new in reps.items():
    html = html.replace(old, new)

# ═══ STEP 1B: SUBTITLE/QUOTE ═══
sub_es = "Quien cuida su propio karma con la delicadeza de un artista supremo, adorna su alma con hilos de oro y renace en la más pura armonía celestial."
sub_en = "Whoever tends to their own karma with the delicacy of a supreme artist, adorns their soul with golden threads and is reborn in the purest celestial harmony."

subs = {"es": sub_es, "en": sub_en}
for code, gc in LANGS.items():
    if code != "en":
        subs[code] = tr(sub_es, gc)

subtitle_pattern = r'(<p class="subtitle">)(.*?)(</p>)'
def build_subtitle_block(match):
    result = '<p class="subtitle">\n'
    quotes = {"es":('"','"'),"en":('"','"'),"it":('"','"'),"zh":('\u201c','\u201d'),"ar":('"','"'),"ru":('«','».'),"de":('\u201e','\u201c'),"fr":('« ',' »'),"ja":('「','」'),"pt":('"','"'),"vi":('"','"')}
    for lang in ALL:
        q1, q2 = quotes.get(lang, ('"','"'))
        result += f'                    <span class="{lang}">{q1}{subs[lang]}{q2}</span>\n'
    result += '                </p>'
    return result
html = re.sub(subtitle_pattern, build_subtitle_block, html, flags=re.DOTALL)
print("Step 1 done.")

# ═══ STEP 2: EXPLANATION ═══
print("Step 2: Explanation...")
expl_es = [
    "En el gran templo del universo, el karma no es simplemente una ley de compensaciones mecánicas, sino una disciplina de belleza suprema, un arte que debe ser cultivado con devoción y delicadeza. Cada pensamiento que emitimos, cada palabra que pronunciamos y cada acción que realizamos es una pincelada sobre el lienzo invisible de nuestro propio destino. Quien trata su conducta cotidiana con esmero, amor y compasión, puliendo hasta el más mínimo detalle de sus interacciones con los demás, está practicando la más alta alquimia kármica: la transformación del ser en una obra de arte viviente.",
    "¿Por qué el esmero en las pequeñas acciones tiene un efecto tan transformador? Porque la verdadera pureza moral no reside en los actos heroicos y visibles, sino en la sensibilidad silenciosa de los momentos cotidianos. Saludar con un respeto genuino, escuchar con atención sincera, consolar sin que nadie nos vea o reparar el daño ajeno con paciencia son los hilos de oro con los que se teje el alma. El universo no juzga la magnitud exterior del acto, sino la finura interior del corazón que lo produce. Quien adorna su vida de bondad silenciosa, está tejiendo un manto protector de pura luz a su alrededor.",
    "El fruto de cuidar el karma como un arte es de una belleza inconmensurable: el alma no solo se libera de las asperezas y deudas acumuladas, sino que se sintoniza con las frecuencias más elevadas de la creación. Al desencarnar, aquel que esculpió su karma con amor y esmero merece renacer en existencias de sublime armonía, rodeado de belleza, gracia espiritual y una paz que excede todo entendimiento. Porque el arte de la tierra se convierte en el palacio del cielo; quien creó belleza en lo pequeño, habitará en la gloria eterna de lo perfecto."
]
expl_en = [
    "In the grand temple of the universe, karma is not simply a mechanical law of compensation, but a discipline of supreme beauty, a sacred art that must be cultivated with deep devotion and care. Every thought we release, every word we utter, and every action we perform is a brushstroke upon the invisible canvas of our destiny. Whoever treats their daily conduct with reverence and compassion, polishing the smallest details of their interactions with others, is practicing the highest karmic alchemy: the transformation of the self into a living masterpiece.",
    "Why does meticulous care in small actions have such a transformative effect? Because true moral purity does not reside in loud, heroic deeds, but in the silent sensitivity of daily moments. Greeting someone with genuine respect, listening with sincere attention, offering comfort when no one is watching, or repairing another's hurt with patience —these are the golden threads with which the soul is woven. The universe does not judge the outer magnitude of the deed, but the inner refinement of the heart from which it flows. He who adorns his life with silent kindness weaves a protective mantle of pure light around his destiny.",
    "The fruit of tending to karma as a fine art is of an immeasurable beauty: the soul is not only liberated from its accumulated debts and rough edges, but it attunes to the highest frequencies of creation. Upon departure, the one who sculpted their karma with love and devotion is worthy of being reborn in an existence of sublime harmony, surrounded by elegance, spiritual grace, and a peace that surpasses all understanding. For the art of the earth becomes the palace of heaven; he who created beauty in small things shall dwell in the eternal glory of the perfect."
]

expl_all = {"es": expl_es, "en": expl_en}
for code, gc in LANGS.items():
    if code != "en":
        expl_all[code] = [tr(p, gc) for p in expl_es]
        print(f"  Explanation -> {code}")

expl_html = '<!-- ═══ EXPLICACIÓN KÁRMICA ═══ -->\n            <div class="story-block fade-in">\n'
for lang in ALL:
    dc = expl_all[lang][0][0]; rest = expl_all[lang][0][1:]
    expl_html += f'                <!-- {lang.upper()} -->\n'
    expl_html += f'                <p class="{lang}"><span class="drop-cap">{dc}</span>{rest}</p>\n'
    for p in expl_all[lang][1:]:
        expl_html += f'                <p class="{lang}">{p}</p>\n'
    expl_html += '\n'
expl_html += '            </div>'

# Replaces the entire explanation block
html = re.sub(r'<!-- ═══ EXPLICACIÓN KÁRMICA ═══ -->.*?</div>\s*\n\s*\n\s*<!-- ═══ PARÁBOLA ═══ -->', expl_html + '\n\n            <!-- ═══ PARÁBOLA ═══ -->', html, flags=re.DOTALL)
print("Step 2 done.")

# ═══ STEP 3: PARABLE ═══
print("Step 3: Parable...")
title_es = "El Telar de Seda de Oro"
title_en = "The Loom of Golden Silk"
parable_es = [
    "En una pequeña aldea en las laderas de Annam, vivía un viejo tejedor llamado An. Tenía un ojo ciego y vestía prendas humildes, pero su telar producía milagros. An no trabajaba para los ricos ni para los nobles; su vida estaba consagrada a reparar las ropas raídas de los huérfanos, los mendigos y las viudas del pueblo. Sin embargo, An no se limitaba a remendar las prendas: sobre cada rotura, cada mancha o cada jirón, bordaba con paciencia hermosas flores silvestres utilizando finos hilos de seda de oro. Sus vecinos le preguntaban extrañados: 'An, ¿por qué gastas tu preciosa seda de oro en los harapos de los mendigos?'. El anciano sonreía con dulzura y respondía: 'Cada alma es un templo sagrado del cielo. Si reparo sus ropas con hilos feos y toscos, les recuerdo su miseria; pero si coso oro sobre su pobreza, les recuerdo que son preciosos para el universo. Cuidar de su dignidad es el arte de mi vida'.",
    "El gobernador de la provincia, un hombre cruel y soberbio que había acumulado inmensas riquezas a costa del hambre del pueblo, oyó hablar de la fama del tejedor. Un día, llegó a la cabaña de An escoltado por sus guardias, trayendo consigo varios rollos de seda fina que habían sido confiscados por la fuerza a unos agricultores hambrientos. 'An', ordenó el gobernador con arrogancia, lanzando un pesado cofre de monedas de oro al suelo, 'quiero que tejas el tapiz más suntuoso para mi palacio usando esta seda confiscada. Si lo haces, este oro será tuyo y vivirás en la abundancia. Pero si te niegas, quemaré tu telar y te arrojaré a las bestias para que te devoren'.",
    "El anciano tejedor miró fijamente la seda confiscada, luego el oro, y finalmente los ojos del tirano. Con una serenidad inquebrantable, juntó sus manos temblorosas y dijo: 'Gran señor, no es posible tejer una obra de arte con hilos que están empapados del llanto y el sufrimiento de los inocentes. La belleza del tejido se marchitaría y el humo del dolor envenenaría mi karma y el aire de tu palacio. Prefiero que quemes mi telar de madera antes que permitir que mis manos tejan un solo hilo de injusticia'. Enfurecido por la negativa, el gobernador ordenó prender fuego a la cabaña de An, destruyendo su telar y desterrando al anciano de la comarca en medio de una gélida tormenta.",
    "An caminó sin rumbo bajo la lluvia helada, sin rencor ni amargura en su corazón. Tiritando de frío, se refugió bajo las raíces de un anciano baniano. Mientras sentía que sus fuerzas le abandonaban, el anciano no maldijo al tirano; en cambio, cerró los ojos y oró con profunda compasión, pidiendo que el gobernador encontrara la luz y liberara su propia alma de los hilos oscuros que estaba tejiendo. Al amanecer, cuando los aldeanos lo encontraron sin vida, presenciaron un prodigio: el cielo se había cubierto de miles de hilos de luz dorada que tejían un manto de protección sobre el valle, y una fragancia exquisita a jazmín inundaba el aire. El anciano An había completado su obra maestra: su propio karma, un tejido de infinita belleza y amor puro que ascendía radiante hacia los cielos."
]
parable_en = [
    "In a small village nestled along the misty slopes of Annam, there lived an old weaver named An. He was blind in one eye and wore humble, threadbare robes, yet his loom produced miracles. An did not work for the wealthy or the nobles; his life was entirely consecrated to repairing the torn, dirty garments of orphans, beggars, and widows. Yet, An did not merely patch their clothes: over every tear, stain, or rip, he patiently embroidered beautiful wild flowers using fine threads of golden silk. His neighbors, mystified, would ask: 'An, why do you waste your precious golden silk on the rags of beggars?' The old man would smile gently and reply: 'Every soul is a sacred temple of the heavens. If I repair their garments with rough, ugly threads, I remind them of their misery; but if I sew gold onto their poverty, I remind them that they are precious to the universe. Protecting their dignity is the art of my life.'",
    "The governor of the province, a cruel and arrogant man who had accumulated vast wealth by starving his people, heard of the weaver's fame. One day, he arrived at An’s cabin escorted by his guards, bringing rolls of fine silk that had been forcibly confiscated from starving farmers. 'An,' the governor ordered arrogantly, throwing a heavy chest of gold coins to the floor, 'I want you to weave the most sumptuous tapestry for my palace using this confiscated silk. If you do, this gold shall be yours and you will live in abundance. But if you refuse, I will burn your loom and throw you to the beasts to be devoured.'",
    "The old weaver looked at the stolen silk, then at the gold, and finally into the eyes of the tyrant. With unshakable serenity, he folded his trembling hands and said: 'Noble lord, it is impossible to weave a work of art using threads soaked in the tears and suffering of the innocent. The beauty of the fabric would wither, and the smoke of their sorrow would poison my karma and the very air of your palace. I would rather you burn my wooden loom than allow my hands to weave a single thread of injustice.' Infuriated by his refusal, the governor ordered his guards to set fire to An’s cottage, destroying his loom and banishing the old man from the region into a freezing monsoonal storm.",
    "An walked aimlessly through the icy rain, yet there was no resentment or bitterness in his heart. Shivering with cold, he sought shelter beneath the massive roots of an ancient banyan tree. As he felt his strength fading, the old man did not curse the tyrant; instead, he closed his eyes and prayed with deep compassion, asking that the governor find the light and free his own soul from the dark threads he was weaving. At dawn, when the villagers found his lifeless body, they witnessed a miracle: the sky was covered with thousands of golden threads, weaving a protective canopy of light over the valley, and an exquisite scent of jasmine filled the air. Old An had completed his final masterpiece: his own karma, a tapestry of infinite beauty and pure love that ascended radiantly into the heavens."
]

titles = {"es": title_es, "en": title_en}
paras = {"es": parable_es, "en": parable_en}
for code, gc in LANGS.items():
    if code != "en":
        titles[code] = tr(title_es, gc)
        paras[code] = [tr(p, gc) for p in parable_es]
        print(f"  Parable -> {code}")

pb = '<div class="story-block parable-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">\n'
for lang in ALL:
    pb += f'                <h3 class="{lang}" style="color: var(--gold); text-align: center; font-family: \'Cinzel\', serif; margin-bottom: 2rem;">{titles[lang]}</h3>\n'
for lang in ALL:
    for p in paras[lang]:
        pb += f'                <p class="{lang}" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">{p}</p>\n'
pb += '            </div>'

# Replaces the parable block
html = re.sub(r'<div class="story-block parable-block fade-in"[^>]*>.*?</div>\s*\n\s*<!-- ═══ ART ═══ -->', pb + '\n\n            <!-- ═══ ART ═══ -->', html, flags=re.DOTALL)
print("Step 3 done.")

# ═══ STEP 4: MORAL ═══
print("Step 4: Moral...")
moral_es = "Quien borda con hilos de oro la dignidad del desamparado y prefiere ver quemar su telar antes que tejer con hilos de injusticia, está labrando en su karma la obra de arte más sagrada, cuyo brillo celestial jamás podrá extinguirse."
moral_en = "Whoever embroiders the dignity of the helpless with threads of gold and chooses to see their loom burn rather than weave with threads of injustice, is carving in their karma the most sacred masterpiece, whose celestial brilliance can never be extinguished."

morals = {"es": moral_es, "en": moral_en}
for code, gc in LANGS.items():
    if code != "en":
        morals[code] = tr(moral_es, gc)

moral_html = ""
for lang in ALL:
    moral_html += f'<span class="{lang}">{morals[lang]}</span>\n                '
html = re.sub(r'<div class="moral fade-in">\s*.*?</div>', f'<div class="moral fade-in">\n                {moral_html.strip()}\n            </div>', html, flags=re.DOTALL)
print("Step 4 done.")

# ═══ STEP 5: INSPIRATION ═══
print("Step 5: Inspiration...")
cause_es = "Cuidar del propio karma y de las acciones cotidianas como una fina obra de arte, con infinito esmero, compasión y delicadeza en cada palabra, pensamiento y acto."
cause_en = "To care for one's own karma and daily actions as a fine art, with infinite devotion, compassion, and delicacy in every word, thought, and deed."

effect_es = "Renacer en una existencia de sublime armonía, gracia espiritual y belleza circundante, libre de deudas y asperezas kármicas."
effect_en = "To be reborn in an existence of sublime harmony, spiritual grace, and beautiful surroundings, free from karmic debts and obstacles."

causes = {"es": cause_es, "en": cause_en}
effects = {"es": effect_es, "en": effect_en}
for code, gc in LANGS.items():
    if code != "en":
        causes[code] = tr(cause_es, gc)
        effects[code] = tr(effect_es, gc)
        print(f"  Inspiration -> {code}")

# Explicit Vietnamese (Gốc) strings from original temple mural
vi_cause_original = "Biết gìn giữ nghiệp lành như một nghệ thuật, thận trọng trong từng ý nghĩ và hành vi."
vi_effect_original = "Đời đời hưởng phước báo thanh cao, thân tâm tự tại, cảnh giới trang nhã."

vi_text = f'''<p class="vi" style="color: #fff; font-style: italic; margin-bottom: 2rem; font-family: 'EB Garamond', serif; font-size: 1.2rem;">
                        <strong>🇻🇳 Tiếng Việt (Gốc):</strong><br>
                        Nhân: {vi_cause_original}<br>
                        Quả: {vi_effect_original}
                    </p>\n'''

box_html = '<div class="translation-box" style="background: rgba(0,0,0,0.4); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--gold); max-width: 800px; margin: 0 auto;">\n'
box_html += f'                    {vi_text}'
for code in ALL:
    c_val = vi_cause_original if code == "vi" else causes[code]
    e_val = vi_effect_original if code == "vi" else effects[code]
    box_html += f'                    <p class="{code}" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197,160,89,0.1); padding: 1rem; border-left: 3px solid var(--gold);">\n                        <strong>{FLAGS[code]} {LANG_NAMES[code]}:</strong><br>\n                        <strong>{c_labels[code]}:</strong> {c_val}<br>\n                        <strong>{e_labels[code]}:</strong> {e_val}\n                    </p>\n'
box_html += '                </div>'

new_insp = f'''<div class="original-inspiration fade-in" style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid rgba(197,160,89,0.3);">
                <h3 class="es" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: 'Cinzel', serif;">La Inspiración Original</h3>
                <h3 class="en" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: 'Cinzel', serif;">The Original Inspiration</h3>
                <center>
                    <img src="assets/pasaje_original.png" alt="Tranh Nhân Quả Original" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 2rem;">
                </center>
                {box_html}
            </div>'''

html = re.sub(r'<div class="original-inspiration fade-in"[^>]*>.*?</div>\s*</div>', new_insp + '\n            </div>', html, flags=re.DOTALL)
print("Step 5 done.")

with open(filepath, "w") as f:
    f.write(html)
print("\n=== CH73 HTML SUCCESSFULLY GENERATED AND TRANSLATED ===")
