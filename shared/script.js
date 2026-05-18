/* ═══════════════════════════════════════════════════════
   KARMA CHAPTERS — Single source of truth for sidebar
   Add new chapters here and ALL pages update automatically.
   ═══════════════════════════════════════════════════════ */
const KARMA_CHAPTERS = [
    { icon: '☰', folder: null, href: 'index.html',
      es:'Biblioteca del Karma', en:'Karma Library', it:'Biblioteca del Karma', zh:'业力图书馆',
      ar:'مكتبة الكرمة', ru:'Библиотека Кармы', de:'Karma-Bibliothek', fr:'Bibliothèque Karma',
      ja:'カルマ ライブラリー', pt:'Biblioteca do Carma', vi:'Thư viện nghiệp chướng' },
    { icon: '0', folder: '00_introduccion',
      es:'El Despertar', en:'The Awakening', it:'Il Risveglio', zh:'觉醒',
      ar:'الصحوة', ru:'Пробуждение', de:'Das Erwachen', fr:"L'Éveil",
      ja:'目覚め', pt:'O Despertar', vi:'Sự thức tỉnh' },
    { icon: '1', folder: '01_esfuerzo_desinteresado',
      es:'Fuerza Física', en:'Physical Strength', it:'Forza Fisica', zh:'体力',
      ar:'القوة البدنية', ru:'Физическая сила', de:'Physische Kraft', fr:'Force Physique',
      ja:'体力', pt:'Força Física', vi:'Thể lực' },
    { icon: '2', folder: '02_fidelidad_y_familia',
      es:'Espejos Rotos', en:'Broken Mirrors', it:'Specchi Rotti', zh:'破镜',
      ar:'مرايا مكسورة', ru:'Разбитые зеркала', de:'Zerbrochene Spiegel', fr:'Miroirs Brisés',
      ja:'割れた鏡', pt:'Espelhos Quebrados', vi:'Gương vỡ' },
    { icon: '3', folder: '03_generosidad_y_prosperidad',
      es:'Siembra Silenciosa', en:'Silent Sowing', it:'Semina Silenziosa', zh:'默默播种',
      ar:'بذر صامت', ru:'Тихий посев', de:'Stilles Säen', fr:'Semis Silencieux',
      ja:'静かな種まき', pt:'Semeadeira Silenciosa', vi:'Gieo hạt thầm lặng' },
    { icon: '4', folder: '04_respeto_por_la_vida',
      es:'Hilo de la Vida', en:'Thread of Life', it:'Filo della Vita', zh:'生命之线',
      ar:'خيط الحياة', ru:'Нить жизни', de:'Faden des Lebens', fr:'Fil de la Vie',
      ja:'命の糸', pt:'Fio da Vida', vi:'Sợi chỉ cuộc sống' },
    { icon: '5', folder: '05_pureza_mental',
      es:'Sombras Mentales', en:'Mental Shadows', it:'Ombre Mentali', zh:'心理阴影',
      ar:'ظلال عقلية', ru:'Ментальные тени', de:'Mentale Schatten', fr:'Ombres Mentales',
      ja:'精神の影', pt:'Sombras Mentais', vi:'Bóng tối tâm trí' },
    { icon: '6', folder: '06_sobriedad_y_claridad',
      es:'Veneno Dulce', en:'Sweet Poison', it:'Dolce Veleno', zh:'甜蜜的毒药',
      ar:'ثعبان الروح', ru:'Сладкий яд', de:'Süßes Gift', fr:'Doux Poison',
      ja:'甘い毒', pt:'Veneno Doce', vi:'Thuốc độc ngọt ngào' },
    { icon: '7', folder: '07_manos_del_mal',
      es:'Manos del Mal', en:'Hands of Evil', it:'Mani del Male', zh:'邪恶之手',
      ar:'أيدي الشر', ru:'Руки зла', de:'Hände des Bösen', fr:'Mains du Mal',
      ja:'悪の手', pt:'Mãos do Mal', vi:'Bàn tay của tội ác' },
    { icon: '8', folder: '08_pedestal_soberbia',
      es:'Soberbia', en:'Pride', it:'Superbia', zh:'傲慢',
      ar:'كبرياء', ru:'Гордыня', de:'Hochmut', fr:'Orgueil',
      ja:'傲慢', pt:'Soberba', vi:'Kiêu ngạo' },
    { icon: '9', folder: '09_frio_egoismo',
      es:'Egoísmo', en:'Greed', it:'Egoismo', zh:'自私',
      ar:'أنانية', ru:'Эгоизм', de:'Egoismus', fr:'Égoïsme',
      ja:'利己主義', pt:'Egoísmo', vi:'Ích kỷ' },
    { icon: '10', folder: '10_infierno_sombras',
      es:'Infierno', en:'Hell', it:'Inferno', zh:'地狱',
      ar:'جحيم', ru:'Ад', de:'Hölle', fr:'Enfer',
      ja:'地獄', pt:'Inferno', vi:'Địa ngục' },
    { icon: '11', folder: '11_mirada_desprecio',
      es:'Desprecio', en:'Contempt', it:'Disprezzo', zh:'蔑视',
      ar:'احتقار', ru:'Презрение', de:'Verachtung', fr:'Mépris',
      ja:'軽蔑', pt:'Desprezo', vi:'Sự khinh miệt' },
    { icon: '12', folder: '12_peso_injusticia',
      es:'Injusticia', en:'Injustice', it:'Ingiustizia', zh:'不公',
      ar:'ظلم', ru:'Несправедливость', de:'Ungerechtigkeit', fr:'Injustice',
      ja:'不正', pt:'Injustiça', vi:'Sự bất công' },
    { icon: '13', folder: '13_amor_y_respeto',
      es:'El Rostro del Amor', en:'The Face of Love', it:"Il volto dell'amore", zh:'爱的面容',
      ar:'وجه الحب', ru:'Лицо любви', de:'Das Gesicht der Liebe', fr:"Le visage de l'amour",
      ja:'愛の顔', pt:'A Face do Amor', vi:'Khuôn mặt của tình yêu' },
    { icon: '14', folder: '14_peso_deudores',
      es:'La Deuda Invisible', en:'The Invisible Debt', it:'Il debito invisibile', zh:'隐形债务',
      ar:'الديون غير المرئية', ru:'Невидимый долг', de:'Die unsichtbare Schuld', fr:'La dette invisible',
      ja:'見えない借金', pt:'A dívida invisível', vi:'Nợ vô hình' },
    { icon: '15', folder: '15_desperdicio_y_escasez',
      es:'El Plato Vacío', en:'The Empty Plate', it:'Il piatto vuoto', zh:'空盘子',
      ar:'اللوحة الفارغة', ru:'Пустая тарелка', de:'Der leere Teller', fr:"L'assiette vide",
      ja:'空の皿', pt:'O Prato Vazio', vi:'Chiếc đĩa trống' },
    { icon: '16', folder: '16_adiccion_y_ceguera',
      es:'La Ceguera Autoimpuesta', en:'Self-Imposed Blindness', it:'Cecità autoimposta', zh:'自我失明',
      ar:'العمى المفروض ذاتيا', ru:'Добровольная слепота', de:'Selbst auferlegte Blindheit', fr:'Cécité auto-imposée',
      ja:'自ら選んだ失明', pt:'Cegueira autoimposta', vi:'Mù quáng tự chuốc lấy' },
    { icon: '17', folder: '17_orfandad_filial',
      es:'El Cordón Cortado', en:'The Cut Cord', it:'Il cordone tagliato', zh:'被割断的绳子',
      ar:'الحبل المقطوع', ru:'Разрезанный шнур', de:'Die durchtrennte Schnur', fr:'Le cordon coupé',
      ja:'カットされたコード', pt:'O cordão cortado', vi:'Sợi dây bị cắt' },
    { icon: '18', folder: '18_pereza_laboral',
      es:'El Peso de la Indolencia', en:'The Weight of Indolence', it:"Il peso dell'indolenza", zh:'懒惰的重量',
      ar:'وزن الكسل', ru:'Тяжесть праздности', de:'Das Gewicht der Trägheit', fr:"Le poids de l'indolence",
      ja:'怠惰の重み', pt:'O peso da indolência', vi:'Sức nặng của sự lười biếng' },
    { icon: '19', folder: '19_destruccion_senderos',
      es:'La Senda Destruida', en:'The Destroyed Path', it:'Il Sentiero Distrutto', zh:'被毁的道路',
      ar:'الطريق المدمر', ru:'Разрушенный путь', de:'Der Zerstörte Pfad', fr:'Le Sentier Détruit',
      ja:'破壊された道', pt:'A Senda Destruída', vi:'Con Đường Bị Phá Hủy' },
    { icon: '20', folder: '20_construccion_puentes',
      es:'El Puente de la Prosperidad', en:'The Bridge of Prosperity', it:'Il Ponte della Prosperità', zh:'繁荣之桥',
      ar:'جسر الازدهار', ru:'Мост процветания', de:'Die Brücke des Wohlstands', fr:'Le Pont de la Prospérité',
      ja:'繁栄の橋', pt:'A Ponte da Prosperidade', vi:'Cây Cầu Thịnh Vượng' },
    { icon: '21', folder: '21_exhibicion_cuerpo',
      es:'El Fuego del Exhibicionismo', en:'The Fire of Exhibitionism', it:'Il Fuoco dell\'Esibizionismo', zh:'裸露之火',
      ar:'نار الاستعراض', ru:'Огонь эксгибиционизма', de:'Das Feuer des Exhibitionismus', fr:'Le Feu de l\'Exhibitionnisme',
      ja:'露出の炎', pt:'O Fogo do Exibicionismo', vi:'Ngọn Lửa Phô Bày' },
    { icon: '22', folder: '22_pesca_excesiva',
      es:'La Red Vacía', en:'The Empty Net', it:'La Rete Vuota', zh:'空网',
      ar:'الشبكة الفارغة', ru:'Пустая сеть', de:'Das Leere Netz', fr:'Le Filet Vide',
      ja:'空の網', pt:'A Rede Vazia', vi:'Lưới Trống' },
    { icon: '23', folder: '23_adiccion_juego',
      es:'Los Dados del Vacío', en:'The Dice of the Void', it:'I dadi del vuoto', zh:'虚空之骰',
      ar:'نرد الفراغ', ru:'Кости пустоты', de:'Die Würfel der Leere', fr:'Les Dés du Vide',
      ja:'虚無のサイコロ', pt:'Os Dados do Vazio', vi:'Xúc Xắc Hư Không' },
    { icon: '24', folder: '24_derroche_sin_caridad',
      es:'La Riqueza de Humo', en:'The Smoke Wealth', it:'La ricchezza di fumo', zh:'烟雾之财',
      ar:'ثروة الدخان', ru:'Дымное богатство', de:'Der Rauchreichtum', fr:'La Richesse de Fumée',
      ja:'煙の富', pt:'A Riqueza de Fumaça', vi:'Sự Giàu Có Khói Bụi' },
    { icon: '25', folder: '25_firmeza_justicia',
      es:'Firmeza ante el Mal', en:'Firmness against Evil', it:'Fermezza contro il Male', zh:'对恶的坚定',
      ar:'الحزم في مواجهة الشر', ru:'Твёрдость перед злом', de:'Standhaftigkeit gegen das Böse', fr:'La fermeté face au mal',
      ja:'悪に対する毅然とした態度', pt:'Firmeza contra o Mal', vi:'Sự cứng rắn trước cái ác' },
    { icon: '26', folder: '26_responsabilidad_nacional',
      es:'Bien Nacional', en:'National Good', it:'Bene Nazionale', zh:'国家利益',
      ar:'الخير الوطني', ru:'Национальное благо', de:'Nationales Wohl', fr:'Bien National',
      ja:'国家의 利益', pt:'Bem Nacional', vi:'Lợi ích quốc gia' },
    { icon: '27', folder: '27_compartir_conocimiento',
      es:'Saber Compartido', en:'Shared Knowledge', it:'Sapere Condiviso', zh:'共享知识',
      ar:'المعرفة المشتركة', ru:'Общие знания', de:'Shared Knowledge', fr:'Savoir Partagé',
      ja:'共有された知識', pt:'Saber Compartilhado', vi:'Tri thức sẻ chia' },
    { icon: '28', folder: '28_represion_talento',
      es:'Represión de Talento', en:'Suppressing Talent', it:'Repressione del Talento', zh:'压制人才',
      ar:'قمع الموهبة', ru:'Подавление таланта', de:'Talentunterdrückung', fr:'Répression du Talent',
      ja:'才能の抑圧', pt:'Repressão de Talento', vi:'Trù dập người tài' },
    { icon: '29', folder: '29_cuidado_ancianos',
      es:'Cuidado y Compasión', en:'Care and Compassion', it:'Cura e Compassione', zh:'关怀与慈悲',
      ar:'الرعاية والرحمة', ru:'Забота и сострадание', de:'Pflege und Mitgefühl', fr:'Soin et Compassion',
      ja:'思いやりと世話', pt:'Cuidado e Compaixão', vi:'Chăm sóc hiếu nghĩa' },
    { icon: '30', folder: '30_generosidad_escasez',
      es:'Generosidad en Escasez', en:'Giving in Scarcity', it:'Generosità in Scarsità', zh:'匮乏中的慷慨',
      ar:'العطاء في العوز', ru:'Щедрость в нужде', de:'Großzügigkeit im Mangel', fr:'Générosité en Pénurie',
      ja:'欠乏の中の寛大さ', pt:'Generosidade na Escassez', vi:'Sẻ chia trong nghèo khó' },
    { icon: '31', folder: '31_consentimiento_destructivo',
      es:'Veneno del Consentimiento', en:'Poison of Indulgence', it:'Veleno del Consenso', zh:'放纵的毒药',
      ar:'سم التدليل', ru:'Яд изнеженности', de:'Gift der Überindulgenz', fr:'Poison de l\'Indulgence',
      ja:'甘やかしの毒', pt:'Veneno do Consentimento', vi:'Độc tố nuông chiều' },
    { icon: '32', folder: '32_apoyo_educacion',
      es:'Cimentar la Sabiduría', en:'Foundation of Wisdom', it:'Fondamenta della Sapienza', zh:'智慧的基石',
      ar:'تأسيس الحكمة', ru:'Фундамент мудрости', de:'Fundament der Weisheit', fr:'Fondation de la sagesse',
      ja:'知恵の基盤', pt:'Cimentar a Sabedoria', vi:'Gieo mầm trí tuệ' },
    { icon: '33', folder: '33_proteccion_hogar',
      es:'Santidad del Refugio', en:'Sanctity of Refuge', it:'Santità del Rifugio', zh:'避难所的神圣',
      ar:'قدسية المأوى', ru:'Святость крова', de:'Heiligkeit der Zuflucht', fr:'Sainteté du refuge',
      ja:'避難所の神聖さ', pt:'Santidade do Refúgio', vi:'Tôn trọng mái ấm' },
    { icon: '34', folder: '34_iluminacion_publica',
      es:'La Luz que Guía a Otros', en:'The Light that Guides Others', it:'La Luce che Guida gli Altri', zh:'引导他人的光',
      ar:'النور الذي يهدي الآخرين', ru:'Свет, направляющий других', de:'Das Licht, das andere führt', fr:'La lumière qui guide les autres',
      ja:'他者を導く光', pt:'A Luz que Guia os Outros', vi:'Ánh sáng khai tâm' },
    { icon: '35', folder: '35_ayuda_victimas_desastres',
      es:'El Refugio de la Compasión', en:'The Shelter of Compassion', it:'Il Rifugio della Compassione', zh:'慈悲的庇护所',
      ar:'ملاذ الرحمة', ru:'Приют сострадания', de:'Die Zuflucht des Mitgefühls', fr:'Le refuge de la compassion',
      ja:'慈悲の避難所', pt:'O Refúgio da Compaixão', vi:'Nơi trú ẩn từ bi' },
    { icon: '36', folder: '36_ganancias_ilicitas',
      es:'Fruto Amargo', en:'Bitter Fruit', it:'Frutto Amaro', zh:'贪婪苦果',
      ar:'ثمار الطمع', ru:'Горький плод', de:'Bittere Frucht', fr:'Fruit Amer',
      ja:'貪欲の果実', pt:'Fruto Amargo', vi:'Quả đắng tham lam' },
    { icon: '37', folder: '37_vida_larga_vitalidad',
      es:'Aliento de Vida', en:'Breath of Life', it:'Respiro di Vita', zh:'生命气息',
      ar:'نفس الحياة', ru:'Дыхание жизни', de:'Atem des Lebens', fr:'Souffle de Vie',
      ja:'命の息吹', pt:'Sopro da Vida', vi:'Hơi thở sự sống' },
    { icon: '38', folder: '38_aprecio_exito_ajeno',
      es:'Aprecio al Éxito', en:'Appreciation', it:'Apprezzamento', zh:'赞赏成功',
      ar:'تقدير النجاح', ru:'Признание успеха', de:'Wertschätzung', fr:'Appréciation',
      ja:'成功の賞賛', pt:'Apreço ao Sucesso', vi:'Tán thán thành công' },
    { icon: '39', folder: '39_finanzas_sabias_exito',
      es:'Finanzas Sabias', en:'Wise Finance', it:'Finanze Sagge', zh:'智慧金融',
      ar:'التمويل الحكيم', ru:'Мудрые финансы', de:'Weise Finanzen', fr:'Finances Sages',
      ja:'賢明な財務', pt:'Finanças Sábias', vi:'Tài chính thông tuệ' },
    { icon: '40', folder: '40_apoyo_obras_buenas',
      es:'Cosecha de Hijos', en:'Harvest of Children', it:'Raccolto dei Figli', zh:'子孙的收获',
      ar:'حصاد الأبناء', ru:'Урожай детей', de:'Ernte der Kinder', fr:'Récolte des Enfants',
      ja:'子孫の収穫', pt:'Colheita dos Filhos', vi:'Mùa gặt con cháu' },
    { icon: '41', folder: '41_derroche_agua_desierto',
      es:'Sed del Alma', en:'Prodigal Thirst', it:'Sete dell\'Anima', zh:'挥霍的干渴',
      ar:'عطش الروح', ru:'Жажда души', de:'Durst der Seele', fr:'Soif de l\'Âme',
      ja:'魂の渇き', pt:'Sede da Alma', vi:'Khát của linh hồn' },
    { icon: '42', folder: '42_derroche_electricidad',
      es:'Oscuridad Heredada', en:'Inherited Darkness', it:'Oscurità Ereditata', zh:'继承的黑暗',
      ar:'الظلام الموروث', ru:'Наследуемая тьма', de:'Geerbte Dunkelheit', fr:'Obscurité Héritée',
      ja:'受け継がれる闇', pt:'Escuridão Herdada', vi:'Bóng tối thừa kế' },
    { icon: '43', folder: '43_esfuerzo_triple_prosperidad',
      es:'Obrero del Destino', en:'Laborer of Destiny', it:'Operaio del Destino', zh:'命运的工匠',
      ar:'عامل القدر', ru:'Труженик судьбы', de:'Arbeiter des Schicksals', fr:'Ouvrier du Destin',
      ja:'運命の職人', pt:'Obreiro do Destino', vi:'Thợ của số phận' },
    { icon: '44', folder: '44_deforestacion_vida_corta',
      es:'Anillos de la Muerte', en:'Rings of Death', it:'Anelli della Morte', zh:'死亡之年轮',
      ar:'حلقات الموت', ru:'Кольца смерти', de:'Ringe des Todes', fr:'Anneaux de la Mort',
      ja:'死の年輪', pt:'Anéis da Morte', vi:'Vòng năm cái chết' },
    { icon: '45', folder: '45_desprecio_habilidades_necedad',
      es:'Juez Juzgado', en:'Judge Judged', it:'Giudice Giudicato', zh:'被审判者',
      ar:'القاضي المحكوم', ru:'Осуждённый судья', de:'Gerichteter Richter', fr:'Juge Jugé',
      ja:'裁かれた審判者', pt:'Juiz Julgado', vi:'Giám khảo bị xét' },
    { icon: '46', folder: '46_predicar_moral_felicidad',
      es:'Sembrador de Conciencias', en:'Sower of Consciences', it:'Seminatore di Coscienze', zh:'良知播种者',
      ar:'زارع الضمائر', ru:'Сеятель совести', de:'Säer des Gewissens', fr:'Semeur de Consciences',
      ja:'良心の種蒔き人', pt:'Semeador de Consciências', vi:'Người gieo lương tri' },
    { icon: '47', folder: '47_generosidad_compasiva_fama',
      es:'Fama que Nadie Buscó', en:'Fame No One Sought', it:'Fama che Nessuno Cercò', zh:'无人追逐的声名',
      ar:'شهرة لم يسعَ إليها', ru:'Слава, которой не искали', de:'Ruhm den niemand suchte', fr:'Gloire que Personne ne Chercha',
      ja:'誰も求めなかった名声', pt:'Fama que Ninguém Procurou', vi:'Danh tiếng không ai tìm' },
    { icon: '48', folder: '48_contaminar_agua_vida_toxica',
      es:'El Río que Recuerda', en:'The River that Remembers', it:'Il Fiume che Ricorda', zh:'记忆之河',
      ar:'النهر الذي يتذكر', ru:'Река, которая помнит', de:'Der Fluss, der sich erinnert', fr:'Le Fleuve qui se Souvient',
      ja:'記憶する川', pt:'O Rio que Recorda', vi:'Dòng Sông Nhớ Mãi' },
    { icon: '49', folder: '49_diligencia_infantil_oportunidades',
      es:'La Escoba y la Cosecha', en:'The Broom and the Harvest', it:'La Scopa e il Raccolto', zh:'扫帚与收获',
      ar:'المكنسة والحصاد', ru:'Метла и жатва', de:'Der Besen und die Ernte', fr:'Le Balai et la Récolte',
      ja:'箒と収穫', pt:'A Vassoura e a Colheita', vi:'Cây Chổi và Mùa Gặt' },
    { icon: '50', folder: '50_no_amar_humanidad_bestia',
      es:'El Exilio de la Especie', en:'The Exile from the Species', it:'L\'Esilio dalla Specie', zh:'物种的放逐',
      ar:'النفي من الجنس البشري', ru:'Изгнание из рода', de:'Die Verbannung aus der Art', fr:'L\'Exil de l\'Espèce',
      ja:'種からの追放', pt:'O Exílio da Espécie', vi:'Lưu Đày Khỏi Loài Người' },
    { icon: '51', folder: '51_engañar_ingenuos_ser_engañado',
      es:'La Telaraña Dorada', en:'The Golden Web', it:'La Ragnatela d\'Oro', zh:'金色蛛网',
      ar:'شبكة العنكبوت الذهبية', ru:'Золотая паутина', de:'Das Goldene Netz', fr:'La Toile d\'Or',
      ja:'黄金の蜘蛛の巣', pt:'A Teia Dourada', vi:'Mạng Nhện Vàng' },
    { icon: '52', folder: '52_defender_inocentes_vida_segura',
      es:'El Escudo Invisible', en:'The Invisible Shield', it:'Lo Scudo Invisibile', zh:'无形的盾',
      ar:'الدرع الخفي', ru:'Невидимый щит', de:'Der Unsichtbare Schild', fr:'Le Bouclier Invisible',
      ja:'見えない盾', pt:'O Escudo Invisível', vi:'Lá Chắn Vô Hình' },
    { icon: '53', folder: '53_desperdiciar_tiempo_juegos_no_renacer',
      es:'El Reloj de Arena Vacío', en:'The Empty Hourglass', it:'La Clessidra Vuota', zh:'空空的沙漏',
      ar:'الساعة الرملية الفارغة', ru:'Пустые песочные часы', de:'Die Leere Sanduhr', fr:'Le Sablier Vide',
      ja:'空の砂時計', pt:'A Ampulheta Vazia', vi:'Đồng Hồ Cát Rỗng' },
    { icon: '54', folder: '54_causar_preocupacion_insomnio_mental',
      es:'Las Noches sin Luna', en:'The Moonless Nights', it:'Le Notti senza Luna', zh:'无月之夜',
      ar:'الليالي بلا قمر', ru:'Безлунные ночи', de:'Die Mondlosen Nächte', fr:'Les Nuits sans Lune',
      ja:'月のない夜', pt:'As Noites sem Lua', vi:'Những Đêm Không Trăng' },
    { icon: '55', folder: '55_arrepentirse_ofrenda_rico_miserable',
      es:'El Oro que No Alimenta', en:'The Gold That Does Not Nourish', it:"L'Oro che Non Nutre", zh:'不能果腹的黄金',
      ar:'الذهب الذي لا يُشبع', ru:'Золото, которое не кормит', de:'Das Gold, das Nicht Nährt', fr:"L'Or qui Ne Nourrit Pas",
      ja:'満たされぬ黄金', pt:'O Ouro que Não Alimenta', vi:'Vàng Mà Không No' },
    { icon: '56', folder: '56_perturbar_paz_ajena_mente_inquieta',
      es:'La Tinta que No Escribe', en:"The Ink That Won't Write", it:"L'Inchiostro che Non Scrive", zh:'无法落笔的墨水',
      ar:'الحبر الذي لا يكتب', ru:'Чернила, которые не пишут', de:'Die Tinte, die Nicht Schreibt', fr:"L'Encre qui N'Écrit Pas",
      ja:'書けぬ墨', pt:'A Tinta que Não Escreve', vi:'Nét Mực Không Thành' },
    { icon: '57', folder: '57_ignorar_persona_necesitada_ciego',
      es:'El Velo de la Indiferencia', en:'The Veil of Indifference', it:"Il Velo dell'Indifferenza", zh:'冷漠之帷',
      ar:'حجاب اللامبالاة', ru:'Завеса безразличия', de:'Der Schleier der Gleichgültigkeit', fr:"Le Voile de l'Indifférence",
      ja:'無関心のベール', pt:'O Véu da Indiferença', vi:'Bức Màn Vô Cảm' },
    { icon: '58', folder: '58_hacer_bien_sin_cultivo_espiritual',
      es:'La Prosperidad sin Espíritu', en:'Prosperity without Spirit', it:'Prosperità senza Spirito', zh:'缺乏灵性的繁荣',
      ar:'الازدهار بدون روح', ru:'Процветание без духа', de:'Wohlstand ohne Geist', fr:'La Prospérité sans Esprit',
      ja:'精神なき繁栄', pt:'A Prosperidade sem Espírito', vi:'Sự Thịnh Vượng Thiếu Linh Hồn' },
    { icon: '59', folder: '59_vivir_con_honestidad_sabiduria',
      es:'La Transparencia del Alma', en:'The Transparency of the Soul', it:"La Trasparenza dell'Anima", zh:'灵魂的透明度',
      ar:'شفافية الروح', ru:'Прозрачность души', de:'Die Transparenz der Seele', fr:"La Transparence de l'Âme",
      ja:'魂 de 透明性', pt:'A Transparência da Alma', vi:'Sự Trong Suốt Của Tâm Hồn' },
    { icon: '60', folder: '60_esmero_pequenas_cosas_inteligencia',
      es:'El Arte de la Precisión Mental', en:'The Art of Mental Precision', it:"L'Arte della Precisione Mentale", zh:'心理精密度的艺术',
      ar:'فن الدقة العقلية', ru:'Искусство ментальной точности', de:'Die Kunst der mentalen Präzision', fr:"L'Art de la Précision Mentale",
      ja:'精神的精度の芸術', pt:'A Arte da Precisione Mentale', vi:'Nghệ Thuật Của Sự Tinh Tế' },
    { icon: '61', folder: '61_respeto_sagrado_miseria',
      es:'La Profanación de lo Invisible', en:'The Profanation of the Invisible', it:"La Profanazione dell'Invisibile", zh:'亵渎无形',
      ar:'تدنيس غير المرئي', ru:'Осквернение невидимого', de:'Die Entweihung des Unsichtbaren', fr:"La Profanation de l'Invisible",
      ja:'見えざるものの冒涜', pt:'A Profanação do Invisível', vi:'Sự Xúc Phạm Đấng Linh Thiêng' },
    { icon: '62', folder: '62_dar_con_burla_desprecio',
      es:'El Veneno de la Limosna Arrogante', en:'The Poison of Arrogant Alms', it:"Il Veleno dell'Elemosina Arrogante", zh:'傲慢施舍之毒',
      ar:'سم الصدقة المتكبرة', ru:'Яд высокомерной милостыни', de:'Das Gift des hochmütigen Almosens', fr:"Le Poison de l'Aumône Arrogante",
      ja:'傲慢な施しの毒', pt:'O Veneno da Esmola Arrogante', vi:'Chất Độc Của Sự Bố Thí Kiêu Ngạo' },
    { icon: '63', folder: '63_silencio_injusticia',
      es:'El Silencio Cómplice', en:'Complacent Silence', it:'Silenzio Complice', zh:'沉默的帮凶',
      ar:'الصمت المتواطئ', ru:'Молчаливое соучастие', de:'Komplizenhaftes Schweigen', fr:'Silence Complice',
      ja:'黙認という共犯', pt:'Silêncio Cúmplice', vi:'Sự Im Lặng Đồng Lõa' },
    { icon: '64', folder: '64_espiritualidad_vacia',
      es:'La Espiritualidad Vacía', en:'Empty Spirituality', it:'Spiritualità Vuota', zh:'空洞的灵性',
      ar:'الروحانية الفارغة', ru:'Пустая духовность', de:'Leere Spiritualität', fr:'Spiritualité Vide',
      ja:'空虚な精神性', pt:'Espiritualidade Vazia', vi:'Sự Tu Tập Thiếu Phước Báu' },
    { icon: '65', folder: '65_riqueza_siembra_escasez',
      es:'La Riqueza Sembrada en la Escasez', en:'Wealth Sown in Scarcity', it:'La Ricchezza Seminata nella Scarsità', zh:'匮乏中播下的财富',
      ar:'الثروة المزروعة في الشح', ru:'Богатство, посеянное в нужде', de:'Reichtum, gesät im Mangel', fr:'La Richesse Semée dans la Pénurie',
      ja:'欠乏の中に蒔かれた富', pt:'A Riqueza Semeada na Escassez', vi:'Sự Giàu Có Gieo Trong Cảnh Nghèo Khó' },
    { icon: '66', folder: '66_tolerancia_error_ajeno',
      es:'El Espejo de la Tolerancia Ciega', en:'The Mirror of Blind Tolerance', it:'Lo Specchio della Tolleranza Cieca', zh:'盲目纵容之镜',
      ar:'مرآة التسامح الأعمى', ru:'Зеркало слепой терпимости', de:'Der Spiegel der blinden Toleranz', fr:'Le Miroir de la Tolérance Aveugle',
      ja:'盲目な寛容の鏡', pt:'O Espelho da Tolerância Cega', vi:'Tấm Gương Của Sự Dung Túng Mù Quáng' },
];

const LANGS = ['es','en','it','zh','ar','ru','de','fr','ja','pt','vi'];

/**
 * Builds sidebar nav dynamically from KARMA_CHAPTERS.
 * Detects base path (../../ or ./) from the page's own <script src>.
 */
function buildSidebar() {
    const nav = document.querySelector('.sidebar-nav');
    if (!nav || nav.children.length > 0) return; // already populated or no placeholder

    // Detect base path: chapters live at ../../, library index at ./
    const scriptSrc = document.querySelector('script[src*="shared/script.js"]');
    let base = '../../';
    if (scriptSrc) {
        const src = scriptSrc.getAttribute('src');
        base = src.replace('shared/script.js', '');
    }

    let html = '';
    KARMA_CHAPTERS.forEach(ch => {
        const href = ch.folder ? `${base}${ch.folder}/web/index.html` : `${base}${ch.href}`;
        const spans = LANGS.map(l => `<span class="${l}">${ch[l]}</span>`).join('');
        html += `<div class="nav-item"><a href="${href}" class="nav-link"><i>${ch.icon}</i>${spans}</a></div>\n`;
    });
    nav.innerHTML = html;
}

document.addEventListener('DOMContentLoaded', () => {
    buildSidebar();
    initLayout();
    initLanguage();
    initScroll();
});

function initLayout() {
    const body = document.body;
    const toggleBtns = document.querySelectorAll('.toggle-btn');
    const overlay = document.querySelector('.sidebar-overlay');
    const langTrigger = document.querySelector('.lang-current-trigger');
    const langMenu = document.querySelector('.lang-dropdown-menu');

    // Desktop/Sidebar collapse state
    const isCollapsed = localStorage.getItem('karmaSidebarCollapsed') === 'true';
    if (window.innerWidth > 1024 && isCollapsed) {
        body.classList.add('sidebar-collapsed');
    }

    // Toggle menu logic
    toggleBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (window.innerWidth <= 1024) {
                body.classList.toggle('sidebar-open');
            } else {
                body.classList.toggle('sidebar-collapsed');
                localStorage.setItem('karmaSidebarCollapsed', body.classList.contains('sidebar-collapsed'));
            }
        });
    });

    // Language Dropdown logic
    if (langTrigger && langMenu) {
        langTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            langMenu.classList.toggle('show');
        });
    }

    // Close language menu on document click
    document.addEventListener('click', () => {
        if (langMenu) langMenu.classList.remove('show');
    });

    // Sidebar Close logic: ONLY via overlay or toggle button in mobile
    // (Removed the global document listener that closed sidebar-open on any click)

    // Sidebar overlay click
    if (overlay) {
        overlay.addEventListener('click', () => {
            body.classList.remove('sidebar-open');
        });
    }

    // Highlight current page
    updateActiveNavLink();
}

function updateActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        link.classList.remove('active');
        const linkHref = link.getAttribute('href');
        if (!linkHref) return;

        // Simplify: if the link is in the current path, it's active
        // Get the folder name from the link (e.g. "09_frio_egoismo")
        const linkParts = linkHref.split('/');
        const folder = linkParts.find(p => p.match(/^\d{2}_/));

        if (folder && currentPath.includes(folder)) {
            link.classList.add('active');
        } else if ((linkHref.includes('index.html') || linkHref === '/') &&
            (currentPath.endsWith('/') || currentPath.endsWith('index.html')) &&
            !currentPath.includes('_')) {
            link.classList.add('active');
        }
    });

    // Auto-scroll sidebar to show the active chapter (centered)
    requestAnimationFrame(() => {
        const activeLink = document.querySelector('.sidebar-nav .nav-link.active');
        if (activeLink) {
            activeLink.scrollIntoView({ block: 'center', behavior: 'instant' });
        }
    });
}

function initLanguage() {
    const urlParams = new URLSearchParams(window.location.search);
    let lang = urlParams.get('lang') || localStorage.getItem('karmaLang') || 'es';
    setLanguage(lang);
}

function setLanguage(lang) {
    document.body.className = document.body.className.replace(/lang-(es|en|it|zh|ar|ru|de|fr|ja|pt|vi)/g, '') + ` lang-${lang}`;
    localStorage.setItem('karmaLang', lang);

    // Update UI Indicators
    const langInfo = {
        'es': { flag: '🇪🇸', label: 'Castellano' },
        'en': { flag: '🇬🇧', label: 'English' },
        'it': { flag: '🇮🇹', label: 'Italiano' },
        'zh': { flag: '🇨🇳', label: '中文' },
        'ar': { flag: '🇦🇪', label: 'العربية' },
        'ru': { flag: '🇷🇺', label: 'Русский' },
        'de': { flag: '🇩🇪', label: 'Deutsch' },
        'fr': { flag: '🇫🇷', label: 'Français' },
        'ja': { flag: '🇯🇵', label: '日本語' },
        'pt': { flag: '🇵🇹', label: 'Português' },
        'vi': { flag: '🇻🇳', label: 'Tiếng Việt' }
    };

    const currentTrigger = document.querySelector('.lang-current-trigger');
    if (currentTrigger && langInfo[lang]) {
        currentTrigger.innerHTML = `<span class="flag">${langInfo[lang].flag}</span> <span>${langInfo[lang].label}</span>`;
    }

    // Update Dropdown Items Active State
    document.querySelectorAll('.lang-opt').forEach(opt => {
        const bl = opt.getAttribute('data-lang');
        opt.classList.toggle('active', bl === lang);
    });

    // Update dynamic dropcaps for all languages
    document.querySelectorAll('.active-dropcap').forEach(el => el.classList.remove('active-dropcap'));
    document.querySelectorAll('.story-block').forEach(block => {
        // Find the first paragraph matching the current language in this block
        const firstPara = block.querySelector(`p.${lang}`);
        if (firstPara) {
            firstPara.classList.add('active-dropcap');
        }
    });

    // Persist language on all navigation links
    const links = document.querySelectorAll('.nav-link, .logo-link, .chapter-card');
    links.forEach(link => {
        try {
            const href = link.getAttribute('href');
            if (!href || href.startsWith('#') || href.startsWith('mailto:')) return;

            const url = new URL(href, window.location.href);
            url.searchParams.set('lang', lang);

            // Use setAttribute to keep relative paths intact
            const base = href.split('?')[0];
            link.setAttribute('href', base + url.search);
        } catch (e) { }
    });
}

function initScroll() {
    const progress = document.querySelector('.scroll-progress');
    const heroImg = document.getElementById('hero-img');
    const fadeElements = document.querySelectorAll('.fade-in');

    const handleScroll = () => {
        const scrolled = window.scrollY;

        // Parallax Effect
        if (heroImg) {
            heroImg.style.transform = `scale(${1 + scrolled * 0.0004}) translateY(${scrolled * 0.1}px)`;
            heroImg.style.opacity = 1 - (scrolled / window.innerHeight);
        }

        // Win Progress line
        const winH = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const width = (scrolled / winH) * 100;
        if (progress) progress.style.width = width + "%";

        // Scroll Fade-in reveal
        fadeElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight * 0.85) {
                el.classList.add('is-visible');
            }
        });
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll();
}
