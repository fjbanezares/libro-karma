#!/usr/bin/env python3
"""Regenerate Ch71 completely from Ch70 template with proper translations."""
import re, shutil
from deep_translator import GoogleTranslator

# Start fresh from Ch70
shutil.copy("70_orgullo_secreto/web/index.html", "71_pureza_servicio/web/index.html")
filepath = "71_pureza_servicio/web/index.html"
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

# ═══ STEP 1: METADATA ═══
print("Step 1: Metadata...")
reps = {
    "LXX": "LXXI", "第七十章": "第七十一章", "第70章": "第71章",
    "الفصل السبعون": "الفصل الحادي والسبعون",
    "La Corona Que Se Quiebra": "La Escoba Sagrada",
    "The Crown That Shatters": "The Sacred Broom",
    "La Corona Che Si Spezza": "La Scopa Sacra",
    "破碎的王冠": "神圣的扫帚",
    "التاج الذي ينكسر": "المكنسة المقدسة",
    "Корона, которая разбивается": "Священная метла",
    "Die Krone, die zerbricht": "Der heilige Besen",
    "La Couronne Qui Se Brise": "Le Balai Sacré",
    "砕ける王冠": "聖なる箒",
    "A Coroa Que Se Parte": "A Vassoura Sagrada",
    "Vương Miện Vỡ Tan": "Cây Chổi Thiêng Liêng",
}
for old, new in reps.items():
    html = html.replace(old, new)

sub_base = "Quien limpia el lugar más humilde con amor puro, barre también las sombras de su karma y abre las puertas del cielo con una fregona."
subtitle_pattern = r'(<p class="subtitle">)(.*?)(</p>)'
def build_subtitle_block(match):
    subs = {"es": sub_base}
    for code, gc in LANGS.items():
        subs[code] = tr(sub_base, gc)
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
    "En la jerarquía invisible del karma, hay un acto que brilla con una luz tan pura que tiene el poder de acelerar la disolución de las deudas espirituales acumuladas durante vidas enteras: limpiar los espacios donde los demás se purifican. Un baño público, una letrina, un aseo comunitario —esos lugares que todos necesitan pero que nadie quiere tocar— son los templos secretos del servicio desinteresado. Quien los limpia con dedicación y sin asco, sin esperar reconocimiento ni recompensa, está ejecutando una de las alquimias kármicas más poderosas que existen: transformar la suciedad exterior en pureza interior.",
    "¿Por qué un acto tan aparentemente insignificante tiene un efecto kármico tan monumental? Porque limpiar lo que otros ensucian sin quejarse es la expresión más radical de la humildad. No hay cámaras filmando, no hay aplausos esperando, no hay premios Nobel para quienes friegan el suelo de un baño público a las cinco de la madrugada. Es el acto invisible por excelencia, y precisamente por eso, el universo lo recompensa con una generosidad que excede toda lógica humana. Cada baldosa que brilla por el trabajo de esas manos anónimas emite una frecuencia que los ángeles reconocen, que los guardianes kármicos registran y que las puertas del cielo no pueden ignorar.",
    "El efecto descrito en este karma es doblemente hermoso: por un lado, el karma negativo acumulado se disipa con una velocidad extraordinaria, como si cada fregona pasada por el suelo barriera también las manchas del alma. Por otro, el destino siguiente —la próxima vida, el próximo ciclo— se abre en un lugar puro, elevado, luminoso. Es la ley de la correspondencia perfecta: quien creó pureza en el lugar más impuro del mundo, merece renacer en el lugar más puro del universo. No hay corona de rey que valga más que un par de guantes de goma gastados por el amor silencioso."
]
expl_all = {"es": expl_es}
for code, gc in LANGS.items():
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
html = re.sub(r'<!-- ═══ EXPLICACIÓN KÁRMICA ═══ -->.*?</div>\s*\n\s*\n\s*<!-- ═══ PARÁBOLA ═══ -->', expl_html + '\n\n            <!-- ═══ PARÁBOLA ═══ -->', html, flags=re.DOTALL)
print("Step 2 done.")

# ═══ STEP 3: PARABLE ═══
print("Step 3: Parable...")
title_es = "La Mujer Que Barría Estrellas"
parable_es = [
    "En las afueras de Hội An había una estación de autobuses con los baños más sucios de toda la provincia. Nadie quería aquel trabajo. Hasta que llegó una mujer llamada Phượng, viuda de cincuenta y tres años, que aceptó el puesto que todos rechazaban. Phượng no limpiaba aquellos baños como quien cumple una condena: los limpiaba como quien cuida un jardín. Cada mañana, a las cuatro, fregaba las baldosas con jabón de jazmín que ella misma preparaba. Pulía los espejos hasta que reflejaban el amanecer. Ponía una flor fresca —siempre una flor— en un vasito junto a cada lavabo.",
    "Los conductores se burlaban: «¿Para qué pones flores en un váter?». Ella sonreía sin responder. Un niño de seis años llamado Minh, que viajaba cada semana con su madre, siempre corría a saludarla: «¡Tía Phượng, hoy hay un jazmín!». Y ella le respondía arrodillándose: «Porque hoy es un buen día para que todo esté limpio, cariño. Incluso los lugares que nadie mira merecen estar bonitos».",
    "Una noche de monzón, el río se desbordó e inundó la estación. Todos huyeron. Phượng se quedó. Con el barro hasta las rodillas, ayudó a una anciana a salir del agua, cargó a tres niños aterrados, improvisó refugio en el techo. Cuando los rescatistas llegaron, encontraron a Phượng empapada, abrazando a siete personas que había salvado. Un bombero dijo: «Señora, usted es una heroína». Phượng respondió tiritando: «No, hijo. Yo solo limpio. Y esta noche, lo que había que limpiar eran las lágrimas».",
    "Phượng murió tres años después, dormida, con una sonrisa inexplicable. El pequeño Minh llevó una flor de jazmín a su tumba cada semana durante un año. La leyenda cuenta que, la noche que Phượng falleció, los vecinos vieron una escalera de luz dorada que descendía desde las nubes hasta su ventana, con cada peldaño cubierto de flores frescas. Porque el universo no olvida a quienes limpian lo que nadie quiere tocar. Y a quienes barren el suelo con amor, les reserva el privilegio de barrer las estrellas."
]
titles = {"es": title_es}; paras = {"es": parable_es}
for code, gc in LANGS.items():
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
html = re.sub(r'<div class="story-block parable-block fade-in"[^>]*>.*?</div>\s*\n\s*<!-- ═══ ART ═══ -->', pb + '\n\n            <!-- ═══ ART ═══ -->', html, flags=re.DOTALL)
print("Step 3 done.")

# ═══ STEP 4: MORAL ═══
print("Step 4: Moral...")
moral_es = "Las manos que limpian lo que nadie quiere tocar son las mismas que el cielo toma primero; porque no hay escalera más alta que la que se construye con humildad, agua limpia y una flor de jazmín en el lugar más olvidado del mundo."
morals = {"es": moral_es}
for code, gc in LANGS.items():
    morals[code] = tr(moral_es, gc)
moral_html = ""
for lang in ALL:
    moral_html += f'<span class="{lang}">{morals[lang]}</span>\n                '
html = re.sub(r'<div class="moral fade-in">\s*.*?</div>', f'<div class="moral fade-in">\n                {moral_html.strip()}\n            </div>', html, flags=re.DOTALL)
print("Step 4 done.")

# ═══ STEP 5: INSPIRATION ═══
print("Step 5: Inspiration...")
cause_es = "Mantener limpios los baños y aseos públicos con dedicación y sin esperar reconocimiento, realizando un servicio humilde que beneficia a todos."
effect_es = "El karma negativo acumulado se disipa con rapidez extraordinaria, y la persona renace en lugares puros, elevados y lujosos, recibiendo una recompensa celestial proporcional a la pureza que creó."
causes = {"es": cause_es}; effects = {"es": effect_es}
for code, gc in LANGS.items():
    causes[code] = tr(cause_es, gc); effects[code] = tr(effect_es, gc)
    print(f"  Inspiration -> {code}")

vi_text = '<p class="vi" style="color: #fff; font-style: italic; margin-bottom: 2rem; font-family: \'EB Garamond\', serif; font-size: 1.2rem;">\n                        <strong>🇻🇳 Tiếng Việt (Gốc):</strong><br>\n                        Nhân: Giữ sạch sẽ những khu vệ sinh.<br>\n                        Quả: Nghiệp xấu mau hết, sinh về nơi thanh tịnh, sang trọng.\n                    </p>\n'
box_html = '<div class="translation-box" style="background: rgba(0,0,0,0.4); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--gold); max-width: 800px; margin: 0 auto;">\n'
box_html += f'                    {vi_text}'
for code in ALL:
    box_html += f'                    <p class="{code}" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197,160,89,0.1); padding: 1rem; border-left: 3px solid var(--gold);">\n                        <strong>{FLAGS[code]} {LANG_NAMES[code]}:</strong><br>\n                        <strong>{c_labels[code]}:</strong> {causes[code]}<br>\n                        <strong>{e_labels[code]}:</strong> {effects[code]}\n                    </p>\n'
box_html += '                </div>'

new_insp = f'''<div class="original-inspiration fade-in" style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid rgba(197,160,89,0.3);">
                <h3 class="es" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: 'Cinzel', serif;">La Inspiración Original</h3>
                <h3 class="en" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: 'Cinzel', serif;">The Original Inspiration</h3>
                <center>
                    <img src="assets/pasaje_original.png" alt="Tranh Nhân Quả Original" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 2rem;">
                </center>
                {box_html}
            </div>'''
html = re.sub(r'<div class="original-inspiration fade-in"[^>]*>.*?</div>\s*</div>', new_insp, html, flags=re.DOTALL)

with open(filepath, "w") as f:
    f.write(html)
print("\n=== CH71 FULLY REGENERATED WITH TRANSLATIONS ===")
