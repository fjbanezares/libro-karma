import os
import shutil
import re
from PIL import Image
from deep_translator import GoogleTranslator

# Folders to create
new_chapters = [
    "13_amor_y_respeto",
    "14_peso_deudores",
    "15_desperdicio_y_escasez",
    "16_adiccion_y_ceguera",
    "17_orfandad_filial",
    "18_pereza_laboral"
]

# Vietnamese / English text from Tranh Nhân Quả 1
tranh_data = {
    "13_amor_y_respeto": {
        "vn": "Nhân: Thái độ yêu quý tôn trọng mọi người.<br>Quả: Gương mặt khả ái phúc hậu.",
        "en_t": "Cause: Treating others with love, kindness and respect.<br>Effect: Brings a lovely and kind face.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Tratar a los demás con amor, amabilidad y respeto.<br>Efecto: Atrae un rostro hermoso, amable y bondadoso.",
        "title_es": "El Rostro del Amor",
        "story_es": "Es una ley sutil que el interior cincela el exterior. Cuando regamos el mundo con aprecio, consideración y una sonrisa sincera hacia cada vida que cruzamos, nuestra propia alma se ilumina. Ese candor interno acaba aflorando a la superficie, esculpiendo en la próxima encarnación un rostro hermoso y sereno que refleja la pureza del espíritu para siempre.",
        "parable_title": "El Espejo de las Almas",
        "parable_text": "Había un anciano cuyo rostro estaba marcado por suaves arrugas que solo inspiraban paz. Aunque no poseía riquezas, trataba a todos con profundo respeto y ternura. Nadie sabía que, en los telares del destino, esa actitud estaba tejiendo la hermosura de su futura existencia. Porque el universo no crea belleza física como un capricho del azar, sino como un reflejo directo del amor incondicional que irradiamos. Quien siembra dulzura, viste de belleza su propia alma hasta hacerla visible a los ojos."
    },
    "14_peso_deudores": {
        "vn": "Nhân: Thọ nhiều ân nghĩa.<br>Quả: Nặng lòng nhớ thương.",
        "en_t": "Cause: Accepting too many favors from someone.<br>Effect: Have a heavy and longing heart.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Recibir y aceptar demasiados favores de los demás sin corresponder.<br>Efecto: Atrae un corazón pesado, nostálgico y agobiado.",
        "title_es": "La Deuda Invisible",
        "story_es": "Recibir ayuda es humano, pero apoyarse perpetuamente en el sacrificio ajeno sin brindar equilibrio o gratitud genera un anclaje energético. Esa comodidad a costa de otros forja la pesada cadena emocional de un corazón constreñido, donde en lugar de libertad y ligereza, el ser experimenta melancolía, vacío y un anhelo constante imposible de saciar, como pago kármico por el desbalance emocional provocado.",
        "parable_title": "El Equipaje Invisible",
        "parable_text": "Cierto joven no dudaba al exigir sacrificios y favores de quienes lo amaban, creyéndose merecedor absoluto de su entrega. Con el tiempo, aunque había adquirido muchos bienes, sentía una opresión en el pecho que ninguna riqueza lograba aliviar. La balanza invisible exigía equilibrio, mostrándole a través del ahogo nostálgico que la verdadera libertad pesa poco, y que todo consuelo ajeno que consumimos sin dar nada a cambio se transforma irremediablemente en la melancolía que cargaremos mañana."
    },
    "15_desperdicio_y_escasez": {
        "vn": "Nhân: Trước kia phung phí thức ăn.<br>Quả: Bây giờ có lúc nhọc nhằn mưu sinh.",
        "en_t": "Cause: Wasting food.<br>Effect: Brings difficulties in earning a living.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Desperdiciar y tirar la comida.<br>Efecto: Trae extremas dificultades para ganarse la vida y conseguir sustento.",
        "title_es": "El Plato Vacío",
        "story_es": "La abundancia jamás debe ser una excusa para la indiferencia y el desperdicio. Cuando ignoramos el hambre del mundo y despilfarramos los recursos como si carecieran de valor sagrado, reescribimos nuestra conexión con el sustento. Esta arrogancia desencadena en un ciclo posterior la pobreza y el sudor agotador solo para conseguir una porción mínima, enseñando la divina lección de que todo lo que la tierra nos da exige respeto absoluto.",
        "parable_title": "El Granero Agotado",
        "parable_text": "Un hombre derrochaba manjares ostentosamente en banquetes, desechando impunemente todo lo que no satisfacía sus caprichos diarios, ignorando la escasez ajena. Años de abundancia terminaron precipitándolo hacia un presente ajeno y hostil donde ni con mil horas bajo el sol sofocante conseguía calmar la desesperación de su estómago vacío. Tuvo que comer el polvo de su propia escasez para grabar, al fin en su alma desnuda, que quien desprecia irresponsablemente el alimento de hoy llama directamente a los mendigos del propio mañana."
    },
    "16_adiccion_y_ceguera": {
        "vn": "Nhân: Ai thường say sưa nghiện ngập.<br>Quả: Sau này ngu dốt mê mờ.",
        "en_t": "Cause: Being an alcoholic and drug user.<br>Effect: Brings a dumb and foolish man.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Ser adicto al alcohol o a las drogas.<br>Efecto: Conlleva un renacer como alguien sumido en la estupidez y el letargo.",
        "title_es": "La Ceguera Autoimpuesta",
        "story_es": "Rendir voluntariamente el precioso milagro de la lucidez y el discernimiento ante los sedantes letárgicos y adicciones oscuras es uno de los extravíos espirituales más fatales. Sumergir la propia mente repetidamente en brumas embriagadoras genera una huella donde, inexorablemente, la consciencia se atrofia hasta renacer con la severa reducción intelectual y confusión abrumadora que en vida anterior se eligió como escape pasivo y tóxico.",
        "parable_title": "La Llama Apagada",
        "parable_text": "A través de vicios paralizantes, un espíritu brillante ahogaba sus penas decidiendo no encarar su realidad. Cerraba a diario sus propios ojos ante los milagros del mundo optando por anestesia en lugar de coraje. Y al no ejercitar el regalo inmenso de la claridad luminosa mental, la inteligencia lo abandonó como agua escurridiza; despertando luego extraviado permanentemente en una necedad gris que será el lento camino para recuperar gradualmente la sabiduría negada que antes le enaltecía."
    },
    "17_orfandad_filial": {
        "vn": "Nhân: Bất hiếu với cha mẹ.<br>Quả: Mồ côi sớm.",
        "en_t": "Cause: Lacking duties to parents.<br>Effect: Brings an orphan in the next life.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Faltar el respeto y no cumplir los deberes con los padres.<br>Efecto: En la próxima vida se renace como huérfano prematuro.",
        "title_es": "El Cordón Cortado",
        "story_es": "Quienes nos han prestado su sangre para encarnar en este pasaje existencial son el sagrado cordón ineludible que nos vincula a la raíz cósmica. La ingratitud filiar o el abandono frío a los que forjaron nuestra existencia rompe drásticamente esa protección vital natural. Ese desdén arroja invariablemente al individuo responsable hacia la brutalidad de la indefensión máxima y la orfandad en frío abandono para su próxima rueda experiencial.",
        "parable_title": "El Árbol sin Raíces",
        "parable_text": "Un hijo soberbio se marchó riendo, renegando sin asomo de gratitud ni compasión alguna de sus viejos progenitores desfallecientes que en el pasado le habían abrigado hasta su madurez y fuerza plena de su juventud. Pero repudiar esa gracia solo quebró sus hilos dorados existenciales que el universo sopesa en su tejido sin margen a errores; arrojándolo entonces sin reparos al frío abandono orfandad nada más tomar su próximo respiro en penumbra desgarradora hasta entender sagradamente cada gota dolorosa inmensa donde reside precisamente ser cuidado por otro ser."
    },
    "18_pereza_laboral": {
        "vn": "Nhân: Không yêu lao động, không yêu việc làm.<br>Quả: Bị thất nghiệp.",
        "en_t": "Cause: Having no interest in working at your job.<br>Effect: Brings unemployment.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: No tener interés en el trabajo y ser negligente por pereza.<br>Efecto: Provoca carecer de oportunidades, miseria y el desempleo constante.",
        "title_es": "El Peso de la Indolencia",
        "story_es": "El progreso de toda nuestra red infinita en la que existimos demanda esfuerzo enfocado humano. Omitir, engañar y estancarse pasiva o negligentemente a la hora de proporcionar nuestro valor equitativo no lastima a nuestros superiores, drena la balanza del sustento personal divino; resultando posteriormente despojado rigurosamente de todos los medios honorables de labor frente al agobiante cierre perpetuo de puertas hasta transmutar tal deshonra apática en servicio y esfuerzo vital.",
        "parable_title": "El Yunque y la Pereza",
        "parable_text": "Había un criado sano que disimulaba falsas afecciones robando horas diarias ante un trabajo justo renegando en soledad oculta cada uno de sus dones y eludiendo responsabilidades a sus hermanos del taller mientras ellos agotaban su pulso productivo. Rehuir sistemáticamente la ley elemental del aporte justo cortó todos los flujos inmaculados que nutrían sus comodidades garantizadas e invirtió su fortuna obligándole brutalmente años después a sufrir una interminable humillación y puertas cerradas pidiendo a gritos cualquier fatiga agotadora que se cruzaran, devolviéndole de rodillas a comprender su ceguera cómoda anterior el privilegio y honra de su propia labor de ayer."
    }
}

lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

def get_trans(text_es, lang_code, g_code):
    try:
        if lang_code == "en": g_code = "en"
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

def trans_dict(text_es):
    d = {"es": text_es, "en": get_trans(text_es, "en", "en")}
    for code, g_code in lang_map.items():
        d[code] = get_trans(text_es, code, g_code)
    return d

import json
print("Translating massive payload. Be patient.")

# Pre-translate everything
compiled_data = {}
for chap, cdata in tranh_data.items():
    print("Translating " + chap)
    compiled = {}
    compiled["vn"] = cdata["vn"]
    compiled["en_t"] = cdata["en_t"]
    compiled["es_t"] = trans_dict(cdata["es_t"])
    compiled["title"] = trans_dict(cdata["title_es"])
    compiled["story"] = trans_dict(cdata["story_es"])
    compiled["parable_title"] = trans_dict(cdata["parable_title"])
    compiled["parable_text"] = trans_dict(cdata["parable_text"])
    
    # an is the analysis for inspiration block, similar to chapter 1-6
    compiled["analysis"] = trans_dict(f'<strong>Análisis:</strong> {cdata["story_es"]}')

    compiled_data[chap] = compiled

with open("chapters_13_18_data.json", "w", encoding='utf8') as f:
    json.dump(compiled_data, f, ensure_ascii=False)

print("Translations done and saved to JSON.")
