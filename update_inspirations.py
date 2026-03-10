import os
import re

chapters = ["07_manos_del_mal", "08_pedestal_soberbia", "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"]

common_texts = {
    "title": {"es": "La Inspiración Original", "en": "The Original Inspiration", "it": "L'Ispirazione Originale", "zh": "最初的灵感", "ar": "الإلهام الأصلي", "ru": "Оригинальное вдохновение", "de": "Die Ursprüngliche Inspiration", "fr": "L'Inspiration Originale", "ja": "元のインスピレーション", "pt": "A Inspiração Original"},
    "desc": {"es": "La historia que hemos generado para este capítulo está inspirada por este pasaje de la escena original de los murales «Tranh Nhân Quả» (Ilustraciones del Karma) del Templo Linh Ung en Da Nang, capturado en la fotografía original.",
             "en": "The story we generated for this chapter is inspired by this passage from the original scene of the \"Tranh Nhân Quả\" (Karma Illustrations) murals at the Linh Ung Temple in Da Nang, captured in the original photograph.",
             "it": "La storia che abbiamo generato per questo capitolo è ispirata a questo passaggio della scena originale dei murales «Tranh Nhân Quả» del Tempio Linh Ung a Da Nang, catturato nella fotografia originale.",
             "zh": "我们为本章生成的故事灵感来自于岘港灵应寺“Tranh Nhân Quả”（因果图）壁画原始场景的这一段，在原始照片中被捕捉下来。",
             "ar": "القصة التي أنشأناها لهذا الفصل مستوحاة من هذا المقطع من المشهد الأصلي لجداريات \"Tranh Nhân Quả\" في معبد Linh Ung في دا نانغ، والتي تم التقاطها في الصورة الأصلية.",
             "ru": "История, которую мы создали для этой главы, вдохновлена этим фрагментом оригинальной сцены фресок «Tranh Nhân Quả» в храме Линь Унг в Дананге, запечатленном на оригинальной фотографии.",
             "de": "Die Geschichte, die wir für dieses Kapitel generiert haben, ist von dieser Passage der ursprünglichen Szene der Wandmalereien „Tranh Nhân Quả“ im Linh Ung-Tempel in Da Nang inspiriert, die auf dem Originalfoto festgehalten wurde.",
             "fr": "L'histoire que nous avons générée pour ce chapitre est inspirée de ce passage de la scène originale des fresques « Tranh Nhân Quả » du temple Linh Ung à Da Nang, capturée sur la photographie originale.",
             "ja": "私たちがこの章のために作成した物語は、ダナンのリンウン寺にある「Tranh Nhân Quả」（カルマのイラスト）壁画の元のシーンのこの一節からインスピレーションを得ており、元の写真に収められています。",
             "pt": "A história que geramos para este capítulo foi inspirada nesta passagem da cena original dos murais «Tranh Nhân Quả» no Templo Linh Ung em Da Nang, capturada na fotografia original."},
}

# The translations for the translations box
trans_7 = {
    "es": "<strong>Traducción:</strong><br>Causa: Usar las manos para actos malvados.<br>Efecto: Renace como una especie sin manos.",
    "en": "<strong>Translation:</strong><br>Cause: Using hands to do evil things.<br>Effect: Brings rebirth as species without hands.",
    "it": "<strong>Traduzione:</strong><br>Causa: Usare le mani per compiere azioni malvagie.<br>Effetto: Rinasce come una specie senza mani.",
    "zh": "<strong>翻译:</strong><br>原因: 用手做恶事。<br>结果: 来生变成没有手的物种。",
    "ar": "<strong>الترجمة:</strong><br>السبب: استخدام اليدين لفعل أفعال شريرة.<br>النتيجة: يولد كأنواع بدون أيدي.",
    "ru": "<strong>Перевод:</strong><br>Причина: Использование рук для совершения злых дел.<br>Следствие: Возрождается в виде вида без рук.",
    "de": "<strong>Übersetzung:</strong><br>Ursache: Hände für böse Taten nutzen.<br>Wirkung: Wird als handloses Lebewesen wiedergeboren.",
    "fr": "<strong>Traduction :</strong><br>Cause : Utiliser ses mains pour faire de mauvaises actions.<br>Effet : Renait sous forme d'une espèce sans mains.",
    "ja": "<strong>翻訳:</strong><br>原因：手を使って悪事を行う。<br>結果：手のない種として生まれ変わる。",
    "pt": "<strong>Tradução:</strong><br>Causa: Usar as mãos para praticar ações malignas.<br>Efeito: Renasce como uma espécie sem mãos.",
}
trans_8 = {
    "es": "<strong>Traducción:</strong><br>Causa: Ser arrogante e irrespetuoso con los demás.<br>Efecto: Trae bajo estatus social.",
    "en": "<strong>Translation:</strong><br>Cause: Being arrogant and disrespectful towards others.<br>Effect: Brings low social status.",
    "it": "<strong>Traduzione:</strong><br>Causa: Essere arroganti e irrispettosi verso gli altri.<br>Effetto: Porta a un basso stato sociale.",
    "zh": "<strong>翻译:</strong><br>原因: 骄傲自大不尊重他人。<br>结果: 导致极低的社会地位。",
    "ar": "<strong>الترجمة:</strong><br>السبب: الغطرسة وعدم الاحترام للآخرين.<br>النتيجة: يجلب تدني الوضع الاجتماعي.",
    "ru": "<strong>Перевод:</strong><br>Причина: Высокомерие и неуважение к другим.<br>Следствие: Приводит к низкому социальному статусу.",
    "de": "<strong>Übersetzung:</strong><br>Ursache: Arrogant und respektlos gegenüber anderen sein.<br>Wirkung: Führt zu einem niedrigen sozialen Status.",
    "fr": "<strong>Traduction :</strong><br>Cause : Être arrogant et irrespectueux envers les autres.<br>Effet : Entraîne un faible statut social.",
    "ja": "<strong>翻訳:</strong><br>原因：他者に対して傲慢で無礼である。<br>結果：低い社会的地位をもたらす。",
    "pt": "<strong>Tradução:</strong><br>Causa: Ser arrogante e desrespeitoso com os outros.<br>Efeito: Traz um baixo status social.",
}
trans_9 = {
    "es": "<strong>Traducción:</strong><br>Causa: Ser tacaño y no ayudar en la vida anterior.<br>Efecto: Renace como un pobre abandonado.",
    "en": "<strong>Translation:</strong><br>Cause: Being stingy and unhelpful in the previous life.<br>Effect: Brings rebirth as a poor and neglected.",
    "it": "<strong>Traduzione:</strong><br>Causa: Essere avari e non d'aiuto nella vita precedente.<br>Effetto: Rinasce povero e trascurato.",
    "zh": "<strong>翻译:</strong><br>原因: 吝啬且前世不愿助人。<br>结果: 来生变成贫困和被忽视的人。",
    "ar": "<strong>الترجمة:</strong><br>السبب: البخل وعدم المساعدة في الحياة السابقة.<br>النتيجة: يولد كفقير ومُهمَل.",
    "ru": "<strong>Перевод:</strong><br>Причина: Скупость и отказ в помощи в прошлой жизни.<br>Следствие: Возрождается бедным и оставленным.",
    "de": "<strong>Übersetzung:</strong><br>Ursache: Im vorigen Leben geizig und wenig hilfsbereit.<br>Wirkung: Wird als arm und vernachlässigt wiedergeboren.",
    "fr": "<strong>Traduction :</strong><br>Cause : Être avare et refuser d'aider dans la vie précédente.<br>Effet : Renait pauvre et négligé.",
    "ja": "<strong>翻訳:</strong><br>原因：前世でケチで助けにならない。<br>結果：貧しく放置された者として生まれ変わる。",
    "pt": "<strong>Tradução:</strong><br>Causa: Ser mesquinho e não ajudar na vida anterior.<br>Efeito: Renasce como um pobre e negligenciado.",
}
trans_10 = {
    "es": "<strong>Traducción:</strong><br>Causa: Ser un ladrón y asesino en la vida anterior.<br>Efecto: Trae renacimiento en el infierno y sufrimiento por fuego y cuchillos.",
    "en": "<strong>Translation:</strong><br>Cause: Being a thief and murderer in the previous life.<br>Effect: Brings rebirth into hell and suffering from fire and knives.",
    "it": "<strong>Traduzione:</strong><br>Causa: Essere stati ladri o assassini nella vita precedente.<br>Effetto: Rinasce all'inferno soffrendo per fuoco e lame.",
    "zh": "<strong>翻译:</strong><br>原因: 前生是小偷和杀人犯。<br>结果: 重生地狱遭受刀剑和火烧的折磨。",
    "ar": "<strong>الترجمة:</strong><br>السبب: أن تكون لصًا وقاتلًا في حياة سابقة.<br>النتيجة: يجلب الولادة في الجحيم والمعاناة من النار والسكاكين.",
    "ru": "<strong>Перевод:</strong><br>Причина: Быть вором или убийцей в прошлой жизни.<br>Следствие: Приносит возрождение в аду и страдания от огня и ножей.",
    "de": "<strong>Übersetzung:</strong><br>Ursache: In einem früheren Leben Dieb und Mörder gewesen sein.<br>Wirkung: Bringt die Wiedergeburt in der Hölle und Leiden durch Feuer und Messer.",
    "fr": "<strong>Traduction :</strong><br>Cause : Avoir été voleur et assassin dans la vie précédente.<br>Effet : Entraîne une renaissance en enfer et des souffrances par le feu et les couteaux.",
    "ja": "<strong>翻訳:</strong><br>原因：前世で泥棒や殺人者であった。<br>結果：地獄に生まれ変わり、火とナイフによる苦しみがもたらされる。",
    "pt": "<strong>Tradução:</strong><br>Causa: Ser ladrão e assassino na vida anterior.<br>Efeito: Traz o renascimento no inferno e o sofrimento por fogo e facas.",
}
trans_11 = {
    "es": "<strong>Traducción:</strong><br>Causa: Mirar a los demás con desprecio.<br>Efecto: Trae enfermedades graves y soledad.",
    "en": "<strong>Translation:</strong><br>Cause: Looking down on others.<br>Effect: Brings severe disease and loneliness.",
    "it": "<strong>Traduzione:</strong><br>Causa: Guardare gli altri dall'alto in basso.<br>Effetto: Porta malattie gravi e solitudine.",
    "zh": "<strong>翻译:</strong><br>原因: 瞧不起他人。<br>结果: 导致严重的疾病和孤独。",
    "ar": "<strong>الترجمة:</strong><br>السبب: النظر بتعالٍ للآخرين.<br>النتيجة: يسبب أمراضًا شديدة وعزلة.",
    "ru": "<strong>Перевод:</strong><br>Причина: Смотреть свысока на других.<br>Следствие: Приводит к тяжелым заболеваниям и одиночеству.",
    "de": "<strong>Übersetzung:</strong><br>Ursache: Auf andere herabsehen.<br>Wirkung: Führt zu schweren Krankheiten und Einsamkeit.",
    "fr": "<strong>Traduction :</strong><br>Cause : Regarder les autres de haut.<br>Effet : Entraîne de graves maladies et la solitude.",
    "ja": "<strong>翻訳:</strong><br>原因：他者を見下す。<br>結果：重い病気と孤独をもたらす。",
    "pt": "<strong>Tradução:</strong><br>Causa: Olhar os outros com desprezo.<br>Efeito: Traz doenças graves e solidão.",
}
trans_12 = {
    "es": "<strong>Traducción:</strong><br>Causa: Tratar mal a los empleados.<br>Efecto: Conduce a un rápido final de las bendiciones y a la pobreza.",
    "en": "<strong>Translation:</strong><br>Cause: Treating employees poorly.<br>Effect: Brings a quick end to blessing and poverty.",
    "it": "<strong>Traduzione:</strong><br>Causa: Trattare male i dipendenti.<br>Effetto: Pone fine alle benedizioni rapidamente portando alla povertà.",
    "zh": "<strong>翻译:</strong><br>原因: 虐待员工。<br>结果: 福气迅速消耗导致贫穷。",
    "ar": "<strong>الترجمة:</strong><br>السبب: سوء معاملة الموظفين.<br>النتيجة: نهاية سريعة للنعم والوقوع في الفقر.",
    "ru": "<strong>Перевод:</strong><br>Причина: Плохое обращение с работниками.<br>Следствие: Быстрая потеря благословений и обнищание.",
    "de": "<strong>Übersetzung:</strong><br>Ursache: Angestellte schlecht behandeln.<br>Wirkung: Führt zu einem schnellen Ende von Segen und zu Armut.",
    "fr": "<strong>Traduction :</strong><br>Cause : Maltraiter les employés.<br>Effet : Met rapidement fin aux bénédictions et conduit à la pauvreté.",
    "ja": "<strong>翻訳:</strong><br>原因：従業員に対する冷酷な扱い。<br>結果：恵みがすぐに尽きて貧困をもたらす。",
    "pt": "<strong>Tradução:</strong><br>Causa: Tratar mal os funcionários.<br>Efeito: Traz um fim rápido para as bênçãos e pobreza.",
}

# The javascript to replace the block
def generate_inspiration_html(vietnamese_html, trans_dict, an_es, an_en):
    # generate title
    title_html = "".join([f'<h3 class="{k}" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: \'Cinzel\', serif;">{v}</h3>\n' for k,v in common_texts["title"].items()])
    desc_html = "".join([f'<p class="{k}" style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto; color: #ccc;">{v}</p>\n' for k,v in common_texts["desc"].items()])
    
    trans_html = "".join([f'<p class="{k}" style="color: #ddd; margin-bottom: 1.5rem;">{v}</p>\n' for k,v in trans_dict.items()])
    
    # We will use Spanish and English analysis for all other langs or auto-translate it later. For now let's just use the original ones to replace the block exactly.
    # Actually, we can translate the analysis! But since it's hardcoded and unique per chapter, let's keep it as is, or we generate it in 10 languages!
    
    html = f"""
            <div class="original-inspiration fade-in" style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid rgba(197, 160, 89, 0.3);">
                {title_html}
                {desc_html}
                <center>
                    <img src="assets/pasaje_original.jpg" alt="Tranh Nhân Quả Original" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 2rem;">
                </center>
                <div class="translation-box" style="background: rgba(0, 0, 0, 0.4); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--gold); max-width: 800px; margin: 0 auto;">
                    {vietnamese_html}
                    {trans_html}
                    <hr style="border-color: rgba(197, 160, 89, 0.2); margin-bottom: 1.5rem;">
                    {an_es}
                    {an_en}
                </div>
            </div>
"""
    return html

import sys
def update_file(filename, trans_dict):
    with open(filename, 'r') as f:
        content = f.read()

    # Find the vietnamese block
    v_match = re.search(r'<p style="color: #fff; font-style: italic; margin-bottom: 1rem; font-family: \'EB Garamond\', serif; font-size: 1.2rem;">.*?</p>', content, re.DOTALL)
    if not v_match:
        return
    vietnamese_html = v_match.group(0)

    a_es_match = re.search(r'<p class="es" style="color: #aaa; margin: 0; line-height: 1\.6;"><strong>Análisis:</strong>.*?</p>', content, re.DOTALL)
    a_en_match = re.search(r'<p class="en" style="color: #aaa; margin: 0; line-height: 1\.6;"><strong>Analysis:</strong>.*?</p>', content, re.DOTALL)

    if not a_es_match or not a_en_match:
        return

    an_es = a_es_match.group(0)
    an_en = a_en_match.group(0)

    new_html = generate_inspiration_html(vietnamese_html, trans_dict, an_es, an_en)

    content = re.sub(r'<div class="original-inspiration fade-in" style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid rgba\(197, 160, 89, 0\.3\);">.*?</div>\s*</div>\s*</main>', new_html + '</div>\n    </main>', content, flags=re.DOTALL)

    with open(filename, 'w') as f:
        f.write(content)

update_file("07_manos_del_mal/web/index.html", trans_7)
update_file("08_pedestal_soberbia/web/index.html", trans_8)
update_file("09_frio_egoismo/web/index.html", trans_9)
update_file("10_infierno_sombras/web/index.html", trans_10)
update_file("11_mirada_desprecio/web/index.html", trans_11)
update_file("12_peso_injusticia/web/index.html", trans_12)

print("Inspirations updated.")
