import os
import re
from deep_translator import GoogleTranslator

# Target languages
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

stories = {
    "01_esfuerzo_desinteresado": """En el plano donde el pasado y el futuro respiran a la vez, el campesino de las montañas y el joven musculoso en la ciudad moderna son el mismo eco de un latido universal. Al entregar sus manos para aliviar la carga de su aldea, aquel constructor trazó en la roca las coordenadas de su propia invencibilidad celular de manera retroactiva. La piedra que partía bajo el sol ardiente le estaba forjando unos hombros indestructibles no para otra vida paralela, sino para que él mismo, hoy, bajo el asfalto de la gran metrópoli, tuviese la potencia de apartar el hierro antes de que apagara una vida. Ese muchacho que levanta el amasijo de metal con una fuerza asombrosa no debe su vigor a la casualidad, sino a las gotas de sudor que su propia alma derramó construyendo un mañana que otros transitan. La generosidad del ayer es el músculo que hoy detiene la muerte, enseñando que cada gota de energía donada regresa para convertirte en el héroe que el mundo —y tú mismo— necesitaba.""",
    
    "02_fidelidad_y_familia": """Cuando el espejo se quiebra, no es una mera casualidad del destino, sino el grito de fragmentos de un alma que sembró la desunión. Más allá del espejismo del tiempo, el hombre seductor que destruye hogares y abandona a quienes creyeron en él es, secretamente y sin darse cuenta, el artífice de la soledad que le ahoga en el presente. Cada mirada esquiva, cada promesa rota en el pasado reverbera de forma cuántica en el vacío que hoy siente en su mesa, como si estuviera traicionando su propia oportunidad de amar. Pero este sufrimiento no es un castigo, es una corrección dolorosa; al vivir rodeado por el eco de voces ausentes que él mismo silenció, su espíritu aprende, a la fuerza, la sacralidad imperiosa del vínculo. Quizás, al derramar la primera lágrima genuina por el amor que se le niega, comience a pegar lentamente los pedazos de ese espejo, descubriendo que la verdadera familia nunca estuvo afuera, sino en la lealtad inquebrantable de un corazón reconstruido.""",
    
    "03_generosidad_y_prosperidad": """En el telar del universo, dar no es restar a la despensa, es multiplicar el campo cuántico de posibilidades. Cuando observamos a aquella mujer que entrega su pan con las manos manchadas de humildad, en un acto imperceptible para la historia humana, estamos viendo a la misma figura que, en otro escenario, distribuye inmensas riquezas. Porque en el eterno ahora del alma, su cuenta corriente no se infló por el azar comercial, sino porque la semilla de aquel mendrugo rompió el suelo del tiempo y el espacio hasta convertirse en un granero inagotable. Ella creía alimentar a un extraño, pero la física moral, en su precisión milimétrica, sabía que se estaba nutriendo a sí misma. Esta abundancia de hoy es una recompensa, sí, pero también es la consecuencia gravitacional ineludible forjada por un espíritu que, al final de su largo viaje espiritual, jamás dejó de ser la campesina de manos polvorientas cuyo capital más inmenso siempre fue la compasión.""",
    
    "04_respeto_por_la_vida": """No hay una distancia real entre el cuchillo que se levanta en el matadero con gélida indiferencia y el escudo que tiembla temeroso en el campo de batalla frente al estruendo de la guerra. En ese instante fugaz donde el respeto por el pulso ajeno se pierde, el universo anota una deuda de terror y debilidades. Quien arrebató el aliento divino mirando a sus víctimas desde la falsa superioridad del acero, se encuentra ahora a sí mismo encarnado en un cuerpo cuya fragilidad se estremece con el silbido del metal circundante. Ese soldado convaleciente, experimentando milímetro a milímetro la angustia de una vida pendiendo de un hilo, no es otra cosa que el verdugo aprendiendo a ser piel desnuda ante el peligro. Resulta paradójico entender que, a través de tremenda agonía, el alma reconecta finalmente con el valor sagrado de todo lo vivo; solo experimentando en propia carne la impotencia y el miedo, podrá aquel espíritu de hielo fundirse para renacer como honroso protector de la vida a la que antes asfixiaba.""",
    
    "05_pureza_mental": """La tinta oscura que emborrona lo sublime y envilece la luz en la mente del prójimo jamás se queda estática en el papel; en el gran campo unificado, esa ponzoña psíquica busca incansablemente su origen para instalarse y tomar la forma de espectros desorientadores. Quien vertió vulgaridades y desesperanza para contaminar la pureza ajena hoy está atrapado en una sala abrumado por miedos irracionales, esquizofrenias mudas, y tormentos mentales paralizantes. Las sombras soncondensación de las mentes felices que ayudó a enfermar. Es la propia contaminación hecha carne, susurrándole, asfixiando su paz mental, enseñándole a golpes la santidad de un pensamiento lúcido a través del oscuro laberinto del extravío temporal. Y aun en esa tiniebla perpetua, asoma la gracia de una curación cósmica: cuando la agonía de mil noches de tormenta mental le empuje a cultivar genuinamente la semilla de pura armonía en su frente, acabará emergiendo con la maestría absoluta y sagrada para limpiar cualquier mente afligida del universo entero.""",
    
    "06_sobriedad_y_claridad": """Ese tabernero que llenó las copas, disolviendo en el licor venenoso las horas valiosas y la sobriedad de viajeros desvalidos en busca de un olvido fugaz, se sorprende hoy siendo incapaz de gozar del dulzor de un leve descanso o una inspiración mental fecunda. Sus ojos afiebrados vagan inútilmente la paz del sueño y la agudeza que en el ayer le robó a sus congéneres, sumergiéndolo en el amargo letargo intelectual. En las matemáticas del alma, de ningún modo cayó condenado de forma arbitraria al castigo del insomnio y a la sequía mental; lo cierto es que sobrelleva él mismo, miligramo a miligramo, las resacas prolongadas y deudas de inteligencia mermada de sus incontables clientes como sí encajasen sus propias neuronas juntas al tragar los frascos vacíos destapados. Obligado a cargar con el vacío narcótico, sentirá en sí mismo un impulso arrollador hacia la lucidez. Entonces el vacío dejará de atormentarlo; en aquel atolladero asfixiante renacerá su avidez sincera por estar milimétricamente consciente en todos los segundos cósmicos de su próxima eternidad.""",
    
    "07_manos_del_mal": """Cuando el puño humano, prodigio de flexibilidad y creación divina, se endurece solo para el asalto, la rapiña y el daño visceral, vulnera y repudia todo aquello sobre lo que está edificado. Resulta perturbador contemplar la alegoría descrita por la escena en Da Nang y comprender que, en el pliegue impalpable del universo cuántico, aquel guerrero rudo y cruel que destrozó, es íntimamente la imagen misma de la criatura impotente arrastrándose a ras de la tierra —una serpiente sin ramas ni caricias a los que extenderse— sofocada frente a la negación abrupta de influir benéficamente el mundo físico frente a la escasez. Pero la gran maquinaria del destino no se mueve por amargura punitiva; le anuló los apéndices superiores por pedagogía y necesidad extrema del universo sobre el respeto de lo útil. Aprenderá tan de raíz la insondable belleza que se escondía en una sencilla herramienta biológica para confortar la vida ajena, que el hambre rabiosa de poseer dedos y palma brotará, transformándolo, cuando se levante con las manos renacientes más suaves de la creación dispuestas jamás y benditas al amor y el afecto sublime.""",
    
    "09_frio_egoismo": """El ser devorado con avidez por el frío del tesoro cerrado que no presta remiendo ni migas a los parias del camino padece una doble miopía: desconoce la abundancia de lo compartido y la gran paradoja del plano superior que todo lo espejea de retorno. Al dejar tiritar de inanición a sus pares encadenando el exceso en cuevas doradas, él mismo empuja al abismo desprendiendo el refugio que albergaría al alma en el presente superpuesto. Aquel lúgubre menesteroso destrozado por la privación, al que hoy evitan en los recovecos marginales de la vía sin amparo civil, es precisamente él mismo engullendo dolor en carne propia por la arrogancia del egoísmo estancado en ese tiempo dilatado y remoto de las aceras sin abrigo. Él se arruinó a futuro secando los vientres rotos de sus hermanos hambrientos de ayer. Es el mismo mendigo. Así, cuando el fuego desgarrador de la soledad le humille a la rodilla por un mísero pedazo en las noches desnudas, el avaricioso curará irreversiblemente su terrible patología posesiva y se prometerá renacer en un ser humano colmado y deshilado solo por el corazón encendido de generosidad que el mundo adolecía con creces.""",
    
    "10_infierno_sombras": """La justicia espiritual jamás recluta a un torturador sombrío; más bien solo le franquea a cada ser el candado candente del sombrío y violento laberinto inflamable que estructuró de forma perversa. Las pavorosas hojas de plata y las llamas rojas que describen vívidamente en las creencias orientales, no operan en una latitud de ira celeste, tan solo representan y concentran literal la onda de aflicción, odio atroz y muertes imperecederas vertidas de los desalmados verdugos durante la existencia aletargada. El despojo impune y el asesinato desgarrador tan solo forjan un vestido agobiante e hirviendo de una vibración pesadísima, la cual invariablemente le abrasará asfixiando a base de resonancia al artífice asesino. El clamor en el infierno que resuena punzante en piel fundida es el reflejo equivalente a los horrores que los inocentes padecieron al enfrentarlo. Pero aun envuelto en tales flagelos apocalípticos de inmenso aprendizaje extremo, subyace una anestesia extirpando del sujeto esa amnesia cruel; ya que solo mediante ese choque de horrendo calor desmantelará la insensibilidad de un monstruo hasta ser cincelado de piedad rotunda. Reducirá asombrosamente su instinto funesto, y cuando se recupere entre rescoldos, revalorizará cada destello de coexistencia con un fervor que los ángeles envidiarían para no agravar nunca jamás una hoja verde de este bosque de las estrellas.""",
    
    "11_mirada_desprecio": """El desdén cortante e insultante con el cual fustigaba la existencia menesterosa desde la plataforma falaz de lo invencible jamás se desvanece de manera liviana en la bruma de lo invisible; se escurre sobre los engranajes cósmicos perforando el porvenir solitario y biológico del mismo verdugo de egos. Quien alzó su mentón humillando y asimilando que él poseía atributos irreductibles mientras el resto se marchitaba exiliándolo a ser estigmatizado socialmente y vilipendiado como un desecho inerme ante él, no asimiló aquella interconexión cuántica rotunda de almas. Tal rechazo implacable elaboró el sombrío destierro crónico recostando a su dueño frente a la agonía asilada sobre cobijas heladas de una enfermedad desgarradora. Es su enfermedad incurable —un cuerpo destrozado a solas— la obra y el escenario sin distracciones montado minuciosamente por él en aquel asco previo infundado e insufrible, en el afán por empujarlo ahora sin discursos elitistas a ser verdaderamente vulnerable buscando compasión sobre esa piel rechazada antes. Sabiéndose dependiente extremo, la llaga viva reventará en sollozos purificando la ceguera y despojará de raíz cualquier vanagloriosa postura material para que, liberado en el abrazo sin casta sobre su propia desgracia en comunión, encuentre un puente empático superior de divinidad sanadora donde todos cohabitamos heridos con idéntica luz bendita.""",
    
    "12_peso_injusticia": """Ese patrón férreo y cegado de rentabilidades codiciosas que estiró las bases prósperas bajo el sudor silenciado de un sinfín de peones forzados a recibir pagas de humillación e indiferencia es un soberbio y fugaz constructor parado en un foso falso ajeno e invadido al destino desproporcionando irremediablemente por cada hora robada el delicado fiel de nuestra colosal balanza interconexa vibratoria. Se cree libre en un feudo impune, pero de soslayo en los espejos temporales aplastados dentro de un callejón y empobrecido de recursos vitales y sin respiro se avecinan sus manos de suplicas tras perder precipitadamente todo cuanto afianzó por injusticia arrebatando de golpe sus comodidades espurias. El hambre y la miseria inunda el piso derrumbado para forzar este despertar contundente exigiendo a sus huesos someterse íntegramente a lo más bajo que aplastaba mediante impiedad, haciéndole recorrer toda aquella cadena atroz en la figura desnuda pordiosera agrietada. Y solo allí desde las sombras heladas y penurias laborales continuas, cuando reasuma a puro sacrificio y sudor no ajeno la valía honrada del sustento y empatice milagrosamente el tormento humano para dar en lugar de expoliar sin remordimientos la decencia vital de otra existencia libre compartiendo equidad para el cosmos entero, redima al universo infinito sus actos erigiendo de nuevo la gloria indestructible bajo los mandatos inquebrantables dorados que sostienen los lazos que nunca vencen sobre bondad y generosidades del verdadero éxito incorruptible de los astros majestuosos."""
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

def build_block(d_t):
    html = f"""<div class="story-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem;">
                <h3 class="es" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">Un Reflejo Cuántico</h3>
                <h3 class="en" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">A Quantum Reflection</h3>
                <h3 class="it" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">Un Riflesso Quantico</h3>
                <h3 class="zh" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">量子反射</h3>
                <h3 class="ar" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">انعكاس كمي</h3>
                <h3 class="ru" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">Квантовое отражение</h3>
                <h3 class="de" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">Eine Quantenreflexion</h3>
                <h3 class="fr" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">Une Réflexion Quantique</h3>
                <h3 class="ja" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">量子反射</h3>
                <h3 class="pt" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 1.5rem;">Um Reflexo Quântico</h3>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify;">"{d_t['es']}"</p>"""
    for code in ["en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]:
        html += f'\n                <p class="{code}" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify;">"{d_t[code]}"</p>'
    html += "\n            </div>"
    return html

def inject(chapter, blk):
    filepath = f"{chapter}/web/index.html"
    if not os.path.exists(filepath): return
    with open(filepath, "r") as f:
        content = f.read()
    
    # We want to insert this block just before the `<div class="moral fade-in">`
    # Or before `<div class="original-inspiration fade-in"` if it exists, otherwise before `.moral`.
    # Let's insert it before `<div class="moral`
    
    new_content = re.sub(r'(\s*<div class="moral fade-in">)', r'\n            ' + blk + r'\1', content)
    
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Injected moving story in {chapter}")
    else:
        print(f"Could not inject into {chapter}")

for chapter, text in stories.items():
    print(f"Translating story for {chapter}...")
    trans_d = {"es": text}
    trans_d.update(translate_es(text))
    blk = build_block(trans_d)
    inject(chapter, blk)
