
import os

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capítulo LX: El Libro del Karma</title>
    <link rel="stylesheet" href="../../shared/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
</head>

<body class="lang-es">
    <div class="scroll-progress"></div>
    <div class="sidebar-overlay"></div>

    <aside class="sidebar">
        <div class="sidebar-header">
            <a href="../../index.html" class="logo-link"><div class="sidebar-logo">KARMA</div></a>
            <button class="toggle-btn">☰</button>
        </div>
        <nav class="sidebar-nav"></nav>
        <div class="sidebar-footer">© Karma 2026</div>
    </aside>

    <main class="main-content">
        <div class="top-header-controls">
            <a href="../../index.html" class="library-quick-link"></a>
            <div class="lang-selector-elegant">
                <button class="lang-current-trigger"><span class="flag">🇪🇸</span> <span class="es">Castellano</span></button>
                <div class="lang-dropdown-menu">
                    <div class="lang-opt" data-lang="es" onclick="setLanguage('es')"><span class="flag">🇪🇸</span> Castellano</div>
                    <div class="lang-opt" data-lang="en" onclick="setLanguage('en')"><span class="flag">🇬🇧</span> English</div>
                    <div class="lang-opt" data-lang="it" onclick="setLanguage('it')"><span class="flag">🇮🇹</span> Italiano</div>
                    <div class="lang-opt" data-lang="zh" onclick="setLanguage('zh')"><span class="flag">🇨🇳</span> 中文</div>
                    <div class="lang-opt" data-lang="ar" onclick="setLanguage('ar')"><span class="flag">🇦🇪</span> العربية</div>
                    <div class="lang-opt" data-lang="ru" onclick="setLanguage('ru')"><span class="flag">🇷🇺</span> Русский</div>
                    <div class="lang-opt" data-lang="de" onclick="setLanguage('de')"><span class="flag">🇩🇪</span> Deutsch</div>
                    <div class="lang-opt" data-lang="fr" onclick="setLanguage('fr')"><span class="flag">🇫🇷</span> Français</div>
                    <div class="lang-opt" data-lang="ja" onclick="setLanguage('ja')"><span class="flag">🇯🇵</span> 日本語</div>
                    <div class="lang-opt" data-lang="pt" onclick="setLanguage('pt')"><span class="flag">🇵🇹</span> Português</div>
                    <div class="lang-opt" data-lang="vi" onclick="setLanguage('vi')"><span class="flag">🇻🇳</span> Tiếng Việt</div>
                </div>
            </div>
            <a class="top-linktree-subtle" href="../../linktree.html">LINKTREE</a>
        </div>

        <header class="mobile-header">
            <button class="toggle-btn">☰</button>
            <div class="sidebar-logo">KARMA</div>
        </header>

        <section class="hero-section">
            <img src="assets/hero.jpg" alt="Karma LX" id="hero-img">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <div class="chapter-num">
                    <span class="es">CAPÍTULO LX</span><span class="en">CHAPTER LX</span><span class="it">CAPITOLO LX</span><span class="zh">第六十章</span><span class="ar">الفصل الستون</span><span class="ru">ГЛАВА LX</span><span class="de">KAPITEL LX</span><span class="fr">CHAPITRE LX</span><span class="ja">第60章</span><span class="pt">CAPÍTULO LX</span><span class="vi">CHƯƠNG LX</span>
                </div>
                <h1 class="chapter-title">
                    <span class="es">El Arte de la Precisión Mental</span>
                    <span class="en">The Art of Mental Precision</span>
                    <span class="it">L'Arte della Precisione Mentale</span>
                    <span class="zh">心理精密度的艺术</span>
                    <span class="ar">فن الدقة العقلية</span>
                    <span class="ru">Искусство ментальной точности</span>
                    <span class="de">Die Kunst der mentalen Präzision</span>
                    <span class="fr">L'Art de la Précision Mentale</span>
                    <span class="ja">精神的精度の芸術</span>
                    <span class="pt">A Arte da Precisão Mental</span>
                    <span class="vi">Nghệ Thuật Của Sự Tinh Tế</span>
                </h1>
                <p class="subtitle">
                    <span class="es">"Quien cuida el detalle de la gota, termina por comprender el misterio del océano; la inteligencia no es más que el fruto de una atención devota a las pequeñas cosas."</span>
                    <span class="en">"He who cares for the detail of the drop ends up understanding the mystery of the ocean; intelligence is but the fruit of a devoted attention to small things."</span>
                    <span class="it">"Chi cura il dettaglio della goccia, finisce per comprendere il mistero dell'oceano; l'intelligenza è il frutto di un'attenzione devota alle piccole cose."</span>
                    <span class="zh">“注重水滴细节的人，最终会理解海洋的奥秘；智慧不过是对细微事物投入专注后的果实。”</span>
                    <span class="ar">"من يهتم بتفاصيل القطرة ينتهي به المطاف بفهم سر المحيط؛ الذكاء ليس سوى ثمرة الاهتمام المخلص بالأشياء الصغيرة."</span>
                    <span class="ru">«Тот, кто заботится о деталях капли, в конце концов познает тайну океана; интеллект — это не что иное, как плод преданного внимания к мелочам».</span>
                    <span class="de">„Wer auf das Detail des Tropfens achtet, versteht am Ende das Geheimnis des Ozeans; Intelligenz ist nichts anderes als die Frucht einer hingebungsvollen Aufmerksamkeit für die kleinen Dinge.“</span>
                    <span class="fr">« Celui qui soigne le détail de la goutte finit par comprendre le mystère de l'océan ; l'intelligence n'est que le fruit d'une attention dévouée aux petites choses. »</span>
                    <span class="ja">「一滴のしずくの細部にこだわる者は、やがて大海の神秘を理解する。知性とは、小さな事柄への献身的な注意の賜物にほかならない。」</span>
                    <span class="pt">"Quem cuida do detalhe da gota, acaba por compreender o mistério do oceano; a inteligência não é mais do que o fruto de uma atenção devota às pequenas coisas."</span>
                    <span class="vi">"Kẻ biết chăm chút cho từng chi tiết của giọt nước rốt cuộc sẽ thấu hiểu được sự huyền bí của đại dương; trí tuệ chẳng qua là thành quả của sự chú tâm tận tụy vào những điều nhỏ bé."</span>
                </p>
                <div class="scroll-indicator"></div>
            </div>
        </section>

        <div class="story-container">
            <!-- ═══ EXPLICACIÓN KÁRMICA ═══ -->
            <div class="story-block fade-in">
                <!-- ES -->
                <p class="es"><span class="drop-cap">E</span>l universo es un tapiz tejido con hilos invisibles, y solo aquel que aprende a observar cada hebra con esmero desarrolla la capacidad de ver el patrón completo. Muchos buscan la inteligencia en los grandes discursos o en los libros complejos, pero el karma nos enseña que la verdadera agudeza mental se cultiva en el silencio de las tareas cotidianas. Cuando realizamos cada pequeña acción —ya sea organizar una mesa, limpiar una herramienta o escribir una palabra— con una atención plena y un cuidado casi sagrado, estamos "afilando" el instrumento de nuestra conciencia.</p>
                <p class="es">Esta devoción al detalle produce un efecto kármico inevitable: la mente se vuelve más rápida, más clara y más capaz de discernir la verdad. El desorden exterior es a menudo el reflejo de un desorden interior, pero el proceso también funciona a la inversa. Al imponer orden y belleza en nuestro entorno mediante el esmero, estamos sembrando las semillas de una inteligencia superior en nuestra próxima existencia, y también en esta. El cerebro no es solo un órgano biológico, es un receptor de sabiduría que se calibra a través de la precisión de nuestros actos.</p>
                <p class="es">El "antes" de este karma es la negligencia y la prisa, que resultan en una mente confusa y una vida llena de errores evitables. El "después" es la maestría: un estado de ser donde la comprensión fluye sin esfuerzo. La inteligencia kármica no es astucia para engañar, sino claridad para comprender. Quien es fiel en lo poco, el universo le confía el entendimiento de lo mucho. Así, el esmero se convierte en la llave de oro que abre las puertas de la percepción suprema.</p>

                <!-- EN -->
                <p class="en"><span class="drop-cap">T</span>he universe is a tapestry woven with invisible threads, and only he who learns to observe each strand with care develops the ability to see the complete pattern. Many seek intelligence in great speeches or complex books, but karma teaches us that true mental sharpness is cultivated in the silence of daily tasks. When we perform every small action—whether organizing a table, cleaning a tool, or writing a word—with full mindfulness and almost sacred care, we are "sharpening" the instrument of our consciousness.</p>
                <p class="en">This devotion to detail produces an inevitable karmic effect: the mind becomes faster, clearer, and more capable of discerning the truth. External disorder is often the reflection of internal disorder, but the process also works in reverse. By imposing order and beauty on our environment through care, we are sowing the seeds of a superior intelligence in our next existence, and in this one as well. The brain is not just a biological organ; it is a receiver of wisdom that is calibrated through the precision of our acts.</p>
                <p class="en">The "before" of this karma is negligence and haste, which result in a confused mind and a life full of avoidable errors. The "after" is mastery: a state of being where understanding flows effortlessly. Karmic intelligence is not cunning to deceive, but clarity to understand. He who is faithful in small things, the universe entrusts with the understanding of great things. Thus, care becomes the golden key that opens the doors of supreme perception.</p>

                <!-- IT -->
                <p class="it"><span class="drop-cap">L</span>'universo è un arazzo tessuto con fili invisibili, e solo chi impara a osservare ogni filo con cura sviluppa la capacità di vedere il disegno completo. Molti cercano l'intelligenza nei grandi discorsi, ma il karma ci insegna che la vera acutezza mentale si coltiva nel silenzio dei compiti quotidiani. Quando eseguiamo ogni piccola azione con piena consapevolezza, stiamo "affilando" lo strumento della nostra coscienza.</p>
                <p class="it">Questa devozione al dettaglio produce un effetto karmico inevitabile: la mente diventa più rapida e chiara. Il disordine esterno è spesso il riflesso di un disordine interiore. Imponendo ordine e bellezza nel nostro ambiente attraverso la cura, seminiamo i semi di un'intelligenza superiore. Il cervello è un ricevitore di saggezza che si calibra attraverso la precisione dei nostri atti.</p>
                <p class="it">Il "prima" di questo karma è la negligenza, che si traduce in una mente confusa. Il "dopo" è la maestria: uno stato di essere in cui la comprensione fluisce senza sforzo. L'intelligenza karmica è chiarezza per comprendere. Chi è fedele nel poco, l'universo gli affida la comprensione di molto. Così, la cura diventa la chiave d'oro che apre le porte della percezione suprema.</p>

                <!-- ZH -->
                <p class="zh"><span class="drop-cap">宇</span>宙是由无形线条织成的挂毯，只有学会用心观察每一根线条的人，才能培养出洞察全局的能力。许多人在宏大的演说中寻找智慧，但业力告诉我们，真正的敏锐是在日常琐事的沉默中培养出来的。当我们以全然的专注和神圣的细致完成每一件小事时，我们就在“磨砺”意识的工具。</p>
                <p class="zh">这种对细节的投入会产生必然的业力影响：头脑变得更敏捷、更清晰。外在的混乱往往是内在混乱的反映。通过细心整理环境，我们正在播下高等智慧的种子。大脑不仅是一个生物器官，它还是一个通过行为的精确性来校准的智慧接收器。</p>
                <p class="zh">这种业力的“前因”是疏忽和匆忙，导致思维混乱。而“后果”则是精通：一种理解力毫不费力流动的境界。业力智慧不是欺骗的狡黠，而是理解的清明。在小事上忠诚的人，宇宙会托付其对大事的理解。因此，细致成为了开启至高感知之门的金钥匙。</p>

                <!-- AR -->
                <p class="ar"><span class="drop-cap">ا</span>لكون عبارة عن نسيج منسوج بخيوط غير مرئية، وفقط من يتعلم مراقبة كل خيط بعناية يطور القدرة على رؤية النمط الكامل. يبحث الكثيرون عن الذكاء في الخطب العظيمة، لكن الكارما تعلمنا أن الحدة الذهنية الحقيقية تُزرع في صمت المهام اليومية. عندما نؤدي كل عمل صغير بوعي كامل وعناية مقدسة، فإننا "نشحذ" أداة وعينا.</p>
                <p class="ar">ينتج هذا التفاني في التفاصيل تأثيراً كارمياً حتمياً: يصبح العقل أسرع وأكثر وضوحاً. الفوضى الخارجية غالباً ما تكون انعكاساً للفوضى الداخلية. من خلال فرض النظام والجمال في بيئتنا من خلال العناية، فإننا نزرع بذور ذكاء متفوق. الدماغ هو مستقبل للحكمة يتم ضبطه من خلال دقة أفعالنا.</p>
                <p class="ar">"ما قبل" هذه الكارما هو الإهمال والعجلة، مما يؤدي إلى عقل مشوش. أما "ما بعد" فهو الإتقان: حالة من الوجود يتدفق فيها الفهم دون عناء. ذكاء الكارما هو الوضوح للفهم. من كان أميناً في القليل، يأتمنه الكون على فهم الكثير. وهكذا، تصبح العناية هي المفتاح الذهبي الذي يفتح أبواب الإدراك الأسمى.</p>

                <!-- RU -->
                <p class="ru"><span class="drop-cap">В</span>селенная — это гобелен, сотканный из невидимых нитей, и только тот, кто научится внимательно наблюдать за каждой нитью, развивает способность видеть весь узор. Многие ищут интеллект в великих речах, но карма учит нас, что истинная острота ума взращивается в тишине повседневных дел. Когда мы выполняем каждое маленькое действие с полным вниманием, мы «затачиваем» инструмент своего сознания.</p>
                <p class="ru">Эта преданность деталям производит неизбежный кармический эффект: ум становится быстрее и яснее. Внешний беспорядок часто является отражением беспорядка внутреннего. Наводя порядок в своем окружении через старание, мы сеем семена высшего интеллекта. Мозг — это приемник мудрости, который калибруется через точность наших поступков.</p>
                <p class="ru">Состояние «до» этой кармы — это небрежность и спешка, приводящие к спутанности сознания. «После» — это мастерство: состояние бытия, в котором понимание течет без усилий. Кармический интеллект — это ясность для понимания. Верному в малом Вселенная доверяет понимание многого. Так старание становится золотым ключом, открывающим двери высшего восприятия.</p>

                <!-- DE -->
                <p class="de"><span class="drop-cap">D</span>as Universum ist ein Teppich aus unsichtbaren Fäden, und nur wer lernt, jeden Faden mit Sorgfalt zu beobachten, entwickelt die Fähigkeit, das gesamte Muster zu sehen. Viele suchen Intelligenz in großen Reden, aber das Karma lehrt uns, dass wahre geistige Schärfe in der Stille der täglichen Aufgaben kultiviert wird. Wenn wir jede kleine Handlung mit voller Achtsamkeit ausführen, „schärfen“ wir das Instrument unseres Bewusstseins.</p>
                <p class="de">Diese Hingabe zum Detail erzeugt eine unvermeidliche karmische Wirkung: Der Geist wird schneller und klarer. Äußere Unordnung ist oft das Spiegelbild innerer Unordnung. Indem wir durch Sorgfalt Ordnung und Schönheit in unsere Umgebung bringen, säen wir die Samen einer höheren Intelligenz. Das Gehirn ist ein Empfänger für Weisheit, der durch die Präzision unserer Taten kalibriert wird.</p>
                <p class="de">Das „Vorher“ dieses Karmas ist Nachlässigkeit und Hast, die zu einem verwirrten Geist führen. Das „Nachher“ ist Meisterschaft: ein Zustand des Seins, in dem Verständnis mühelos fließt. Karmische Intelligenz ist Klarheit zum Verstehen. Wer im Kleinen treu ist, dem vertraut das Universum das Verständnis des Großen an. So wird Sorgfalt zum goldenen Schlüssel der Wahrnehmung.</p>

                <!-- FR -->
                <p class="fr"><span class="drop-cap">L</span>'univers est une tapisserie tissée de fils invisibles, et seul celui qui apprend à observer chaque brin avec soin développe la capacité de voir le motif complet. Beaucoup cherchent l'intelligence dans les grands discours, mais le karma nous enseigne que la véritable acuité mentale se cultive dans le silence des tâches quotidiennes. Quand nous accomplissons chaque petite action avec une pleine conscience, nous « aiguisons » l'instrument de notre conscience.</p>
                <p class="fr">Ce dévouement au détail produit un effet karmique inévitable : l'esprit devient plus rapide et plus clair. Le désordre extérieur est souvent le reflet d'un désordre intérieur. En imposant l'ordre et la beauté dans notre environnement par le soin, nous semons les graines d'une intelligence supérieure. Le cerveau est un récepteur de sagesse qui se calibre à travers la précision de nos actes.</p>
                <p class="fr">Le « avant » de ce karma est la négligence et la hâte, entraînant un esprit confus. Le « après » est la maîtrise : un état d'être où la compréhension coule sans effort. L'intelligence karmique est la clarté pour comprendre. À celui qui est fidèle dans les petites choses, l'univers confie la compréhension des grandes. Ainsi, le soin devient la clé d'or de la perception suprême.</p>

                <!-- JA -->
                <p class="ja"><span class="drop-cap">宇</span>宙は見えない糸で織られたタペストリーであり、一本一本の糸を丹念に観察することを学んだ者だけが、全体の模様を見る能力を養うことができます。多くの人は壮大な演説の中に知性を求めますが、カルマは真の精神的な鋭さが日々の仕事の静寂の中で育まれることを教えています。あらゆる小さな行動を十分な注意を払って行うとき、私たちは意識という道具を「研いで」いるのです。</p>
                <p class="ja">細部への献身は、避けられないカルマ的効果を生みます。心はより速く、より明晰になります。外側の無秩序は、しばしば内側の無秩序の反映です。丹精を込めて環境に秩序と美をもたらすことで、私たちは次の生、そして今この生においても高等知性の種をまいているのです。脳は単なる生物学的な器官ではなく、私たちの行いの正確さを通じて調整される知恵の受信機なのです。</p>
                <p class="ja">このカルマの「前」は怠慢と急ぎであり、混乱した心をもたらします。「後」は熟達です。理解が努力なしに流れるような存在の状態です。カルマ的な知性とは、欺くための悪知恵ではなく、理解するための明晰さです。小さなことに忠実な者に、宇宙は大きなことの理解を託します。こうして、丹精は至高の知覚の扉を開く黄金の鍵となるのです。</p>

                <!-- PT -->
                <p class="pt"><span class="drop-cap">O</span> universo é uma tapeçaria tecida com fios invisíveis, e apenas aquele que aprende a observar cada fio com esmero desenvolve a capacidade de ver o padrão completo. Muitos buscam a inteligência nos grandes discursos, mas o karma ensina-nos que a verdadeira agudeza mental cultiva-se no silêncio das tarefas quotidianas. Quando realizamos cada pequena ação com atenção plena, estamos a "afiar" o instrumento da nossa consciência.</p>
                <p class="pt">Esta devoção ao detalhe produz um efeito kármico inevitável: a mente torna-se mais rápida e clara. A desordem exterior é muitas vezes o reflexo de uma desordem interior. Ao impor ordem e beleza no nosso ambiente através do esmero, estamos a semear as sementes de uma inteligência superior. O cérebro é um recetor de sabedoria que se calibra através da precisão dos nossos atos.</p>
                <p class="pt">O "antes" deste karma é a negligência e a pressa, resultando numa mente confusa. O "depois" é a maestria: um estado de ser onde a compreensão flui sem esforço. A inteligência kármica é clareza para compreender. Quem é fiel no pouco, o universo confia-lhe o entendimento do muito. Assim, o esmero torna-se a chave de ouro que abre as portas da perceção suprema.</p>

                <!-- VI -->
                <p class="vi"><span class="drop-cap">V</span>ũ trụ là một bức thảm được dệt bằng những sợi chỉ vô hình, và chỉ những ai học được cách quan sát từng sợi chỉ bằng sự tận tâm mới phát triển được khả năng nhìn thấy toàn bộ hoa văn. Nhiều người tìm kiếm trí tuệ trong những bài diễn thuyết lớn, nhưng nhân quả dạy chúng ta rằng sự nhạy bén thực sự được nuôi dưỡng trong sự tĩnh lặng của những công việc hằng ngày. Khi chúng ta thực hiện mỗi hành động nhỏ với sự chú tâm trọn vẹn, chúng ta đang "mài giũa" công cụ của ý thức mình.</p>
                <p class="vi">Sự tận tụy với chi tiết tạo ra một hiệu ứng nhân quả tất yếu: tâm trí trở nên nhanh nhạy và sáng suốt hơn. Sự lộn xộn bên ngoài thường là phản chiếu của sự hỗn loạn bên trong. Bằng cách thiết lập trật tự và vẻ đẹp cho môi trường xung quanh thông qua sự tỉ mỉ, chúng ta đang gieo hạt giống của một trí tuệ cao cấp. Bộ não không chỉ là một cơ quan sinh học, nó là một bộ thu nhận trí tuệ được hiệu chuẩn thông qua sự chính xác trong hành động của chúng ta.</p>
                <p class="vi">Cái "trước" của nghiệp này là sự cẩu thả và vội vàng, dẫn đến một tâm trí rối loạn. Cái "sau" là sự tinh thông: một trạng thái mà sự thấu hiểu tuôn chảy không cần nỗ lực. Trí tuệ nhân quả không phải là sự khôn lỏi để lừa lọc, mà là sự sáng suốt để thấu hiểu. Kẻ trung tín trong việc nhỏ sẽ được vũ trụ tin tưởng giao phó sự hiểu biết về việc lớn. Vì vậy, sự tận tâm trở thành chiếc chìa khóa vàng mở ra cánh cửa của sự nhận thức tối cao.</p>
            </div>

            <!-- ═══ PARÁBOLA ═══ -->
            <div class="story-block parable-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">
                <h3 class="es" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">El Barrendero de Estrellas</h3>
                <h3 class="en" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">The Sweeper of Stars</h3>
                <h3 class="it" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Lo Spazzino di Stelle</h3>
                <h3 class="zh" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">星辰扫除者</h3>
                <h3 class="ar" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">كانس النجوم</h3>
                <h3 class="ru" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Уборщик звезд</h3>
                <h3 class="de" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Der Sternenkehrer</h3>
                <h3 class="fr" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Le Balayeur d'Étoiles</h3>
                <h3 class="ja" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">星を掃く者</h3>
                <h3 class="pt" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">O Varredor de Estrelas</h3>
                <h3 class="vi" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Người Quét Sao</h3>

                <!-- ES -->
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">En un remoto monasterio de las montañas de Da Lat, vivía un joven novicio llamado Minh cuya única tarea era barrer el patio central. Mientras otros monjes estudiaban manuscritos antiguos y debatían sobre filosofía, Minh pasaba horas moviendo su escoba de bambú con una lentitud rítmica. No barría simplemente para quitar el polvo; barría como si cada grano de arena fuera una joya preciosa. Observaba cómo el viento movía las hojas y colocaba cada piedra del camino en su lugar exacto, con un esmero que a los demás les parecía excesivo.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Pasaron los años, y una gran sequía asoló la región, trayendo consigo un problema que los sabios del reino no podían resolver: el sistema de canales que alimentaba el valle se había bloqueado por un complejo laberinto de sedimentos subterráneos. Los ingenieros más brillantes del emperador trajeron mapas y cálculos, pero ninguno lograba entender por dónde fluía el agua oculta. El emperador, desesperado, visitó el monasterio buscando consejo espiritual.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Minh, que seguía barriendo su patio, levantó la vista y, tras observar la montaña por un instante, señaló un punto insignificante entre dos rocas. "El agua está allí", dijo con calma. "La forma en que las hormigas caminan hoy y la manera en que el musgo ha crecido en esa grieta revelan el pulso de la tierra". Los sabios se rieron, pero al excavar en ese punto exacto, encontraron el canal principal y el agua volvió a fluir. Minh no había estudiado ingeniería, pero su hábito de prestar atención absoluta a lo pequeño le había otorgado una inteligencia que veía lo invisible.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">El emperador le ofreció el puesto de consejero real, pero Minh declinó. "Majestad", dijo, "la sabiduría no es un cargo, es una forma de mirar. Si dejo de prestar atención a cómo cae la hoja sobre el patio, perderé la capacidad de ver cómo se mueve el mundo". Minh regresó a su escoba, comprendiendo que el esmero es el lenguaje secreto con el que el alma habla con la Verdad, y que en cada pequeño acto de cuidado reside la chispa de la inteligencia divina.</p>

                <!-- EN -->
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">In a remote monastery in the mountains of Da Lat, lived a young novice named Minh whose only task was to sweep the central courtyard. While other monks studied ancient manuscripts and debated philosophy, Minh spent hours moving his bamboo broom with a rhythmic slowness. He didn't simply sweep to remove dust; he swept as if every grain of sand were a precious jewel. He watched how the wind moved the leaves and placed every stone on the path in its exact place, with a care that seemed excessive to others.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Years passed, and a great drought devastated the region, bringing with it a problem that the kingdom's sages could not solve: the canal system that fed the valley had been blocked by a complex labyrinth of underground sediments. The Emperor's most brilliant engineers brought maps and calculations, but none could understand where the hidden water flowed. The Emperor, desperate, visited the monastery seeking spiritual advice.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Minh, who was still sweeping his courtyard, looked up and, after observing the mountain for a moment, pointed to an insignificant spot between two rocks. "The water is there," he said calmly. "The way the ants walk today and the way the moss has grown in that crack reveal the pulse of the earth." The sages laughed, but upon digging at that exact spot, they found the main channel and the water flowed again. Minh had not studied engineering, but his habit of paying absolute attention to small things had granted him an intelligence that saw the invisible.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">The Emperor offered him the position of royal advisor, but Minh declined. "Majesty," he said, "wisdom is not a position; it is a way of looking. If I stop paying attention to how the leaf falls on the courtyard, I will lose the ability to see how the world moves." Minh returned to his broom, understanding that care is the secret language with which the soul speaks with Truth, and that in every small act of care resides the spark of divine intelligence.</p>

                <!-- IT -->
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">In un remoto monastero, il giovane Minh aveva il solo compito di spazzare il cortile. Mentre altri studiavano, Minh muoveva la scopa con lentezza ritmica. Non spazzava solo per togliere la polvere; lo faceva come se ogni granello di sabbia fosse un gioiello. Osservava il vento e metteva ogni pietra al suo posto esatto.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Anni dopo, una siccità colpì la regione. Gli ingegneri non riuscivano a trovare l'acqua sotterranea. L'imperatore visitò il monastero disperato. Minh alzò lo sguardo e indicò un punto tra due rocce. "L'acqua è lì", disse. "Il modo in care camminano le formiche rivela il polso della terra".</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Scavando in quel punto, trovarono l'acqua. Minh non aveva studiato ingegneria, ma la sua abitudine di prestare attenzione alle piccole cose gli aveva dato un'intelligenza che vedeva l'invisibile. L'imperatore gli offrì di diventare consigliere, ma Minh rifiutò.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">"Maestà", disse, "la saggezza è un modo di guardare. Se smetto di prestare attenzione a come cade la foglia, perderò la capacità di vedere come si muove il mondo". Minh tornò alla sua scopa, capendo che la cura è il linguaggio segreto dell'anima.</p>

                <!-- ZH -->
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">在山林深处的一座寺庙里，小和尚明的工作只是打扫院子。当其他僧人研读古籍时，明却有节奏地挥动竹帚。他不仅仅是在扫尘；他扫地时仿佛每一粒沙都是珍贵的宝石。他观察风如何吹动叶子，将每一块石头放在准确的位置。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">多年后，该地区遭遇大旱。工程师们无法找到地下水源。绝望的皇帝访问了寺庙。明抬起头，指向两块岩石间的一个不起眼的地方。“水在那里，”他平静地说，“蚂蚁行走的路径和裂缝中苔藓的生长揭示了土地的脉搏。”</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">在那里挖掘后，泉水喷涌而出。明没有学过工程学，但他对微小事物的绝对关注让他拥有了洞察无形的智慧。皇帝邀请他担任顾问，但明拒绝了。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">“陛下，”他说，“智慧是一种观察方式。如果我不再关注叶子如何飘落，我将失去观察世界运作的能力。”明回到了扫帚旁，明白细致是灵魂与真理对话的秘密语言。</p>

                <!-- AR -->
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">في دير بعيد، كان لدى المبتدئ الشاب مينه مهمة واحدة: كنس الفناء. بينما كان الرهبان الآخرون يدرسون المخطوطات، كان مينه يحرك مكنسته ببطء إيقاعي. لم يكن يكنس لمجرد إزالة الغبار؛ بل كان يكنس وكأن كل ذرة رمل هي جوهرة ثمينة. كان يراقب الريح وهي تحرك الأوراق ويضع كل حجر في مكانه الدقيق.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">مرت السنين وضرب جفاف كبير المنطقة. لم يستطع المهندسون العثور على المياه الجوفية. زار الإمبراطور الدير يائساً. رفع مينه عينيه وأشار إلى نقطة بين صخرتين. قال بهدوء: "الماء هناك. الطريقة التي يمشى بها النمل ونمو الطحالب يكشفان عن نبض الأرض".</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">عند الحفر هناك، وجدوا الماء. لم يدرس مينه الهندسة، لكن عادته في الاهتمام بكل ما هو صغير منحته ذكاءً يرى ما لا يُرى. عرض عليه الإمبراطور منصب مستشار، لكن مينه رفض.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">قال: "يا صاحب الجلالة، الحكمة هي طريقة للنظر. إذا توقفت عن الاهتمام بكيفية سقوط الورقة، سأفقد القدرة على رؤية كيف يتحرك العالم". عاد مينه إلى مكنسته، مدركاً أن العناية هي اللغة السرية للروح.</p>

                <!-- RU -->
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">В далеком монастыре жил послушник Мин, чьей единственной задачей было подметать двор. Пока другие монахи изучали древние свитки, Мин часами ритмично двигал метлой. Он не просто сметал пыль; он подметал так, словно каждая песчинка была драгоценным камнем. Он наблюдал за ветром и клал каждый камень на свое точное место.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Прошли годы, и регион поразила великая засуха. Инженеры не могли найти подземные воды. Отчаявшийся император посетил монастырь. Мин поднял взгляд и указал на точку между скалами. «Вода там», — спокойно сказал он. «То, как сегодня ползают муравьи, раскрывает пульс земли».</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">В этом месте нашли воду. Мин не изучал науки, но привычка уделять внимание мелочам даровала ему интеллект, видящий невидимое. Император предложил ему стать советником, но Мин отказался.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">«Ваше Величество, — сказал он, — мудрость — это способ смотреть. Если я перестану замечать, как падает лист, я потеряю способность видеть, как движется мир». Мин вернулся к своей метле, понимая, что старание — это тайный язык души.</p>

                <!-- DE -->
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">In einem fernen Kloster hatte der junge Novize Minh nur eine Aufgabe: den Hof zu kehren. Während andere Mönche Manuskripte studierten, bewegte Minh seinen Besen mit rhythmischer Langsamkeit. Er kehrte nicht nur, um Staub zu entfernen; er kehrte, als wäre jedes Sandkorn ein Juwel. Er beobachtete den Wind und legte jeden Stein an seinen exakten Platz.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Jahre vergingen, und eine Dürre suchte das Land heim. Ingenieure fanden kein Wasser. Der verzweifelte Kaiser besuchte das Kloster. Minh blickte auf und deutete auf eine Stelle zwischen zwei Felsen. „Dort ist das Wasser“, sagte er ruhig. „Die Art, wie die Ameisen heute laufen, offenbart den Puls der Erde.“</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">An genau dieser Stelle fanden sie Wasser. Minh hatte nicht studiert, aber seine Aufmerksamkeit für das Kleine gab ihm eine Intelligenz, die das Unsichtbare sah. Der Kaiser bot ihm an, Berater zu werden, doch Minh lehnte ab.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">„Majestät“, sagte er, „Weisheit ist eine Art zu schauen. Wenn ich aufhöre, darauf zu achten, wie das Blatt fällt, verliere ich die Fähigkeit zu sehen, wie sich die Welt bewegt.“ Minh kehrte zu seinem Besen zurück, im Wissen, dass Sorgfalt die geheime Sprache der Seele ist.</p>

                <!-- FR -->
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Dans un monastère reculé, le jeune Minh n'avait qu'une tâche : balayer la cour. Tandis que les autres étudiaient, Minh bougeait son balai avec une lenteur rythmique. Il ne balayait pas seulement pour enlever la poussière ; il balayait comme si chaque grain de sable était un bijou précieux. Il observait le vent et plaçait chaque pierre à sa place exacte.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Des années plus tard, une sécheresse frappa la région. Les ingénieurs ne trouvaient pas d'eau. L'empereur visita le monastère désespéré. Minh leva les yeux et désigna un point entre deux rochers. « L'eau est là », dit-il calmement. « La façon dont les fourmis marchent révèle le pouls de la terre ».</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">En creusant là, ils trouvèrent l'eau. Minh n'avait pas étudié l'ingénierie, mais son attention aux petites choses lui avait donné une intelligence qui voyait l'invisible. L'empereur lui offrit de devenir conseiller, mais Minh refusa.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">« Majesté », dit-il, « la sagesse est une façon de regarder. Si j'arrête de faire attention à la chute de la feuille, je perdrai la capacité de voir comment le monde bouge ». Minh retourna à son balai, comprenant que le soin est le langage secret de l'âme.</p>

                <!-- JA -->
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">遠く離れた寺院に、ミンという名の若い修行僧がいました。彼の唯一の仕事は中庭を掃くことでした。他の僧侶たちが経典を学んでいる間、ミンは竹箒をリズムよくゆっくりと動かしていました。単に埃を払うために掃くのではなく、一粒一粒の砂が宝石であるかのように掃いていました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">数年後、大干ばつが地域を襲いました。技師たちは地下水を見つけることができませんでした。絶望した皇帝が寺院を訪れました。ミンは顔を上げ、岩の間の何でもない場所を指差しました。「水はそこにあります。蟻の歩き方と亀裂の苔が、大地の脈動を教えてくれています」。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">そこを掘ると、水が溢れ出しました。ミンは工学を学んだことはありませんでしたが、微小なことに絶対的な注意を払う習慣が、目に見えないものを見る知性を彼に与えていたのです。皇帝は彼を顧問に誘いましたが、ミンは断りました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">「陛下」と彼は言いました。「知恵とは役職ではなく、見方なのです。もし私が中庭に落ちる葉に注意を払うのをやめたら、世界がどのように動いているかを見る能力を失ってしまうでしょう」。ミンは箒に戻り、丹精こそが魂が真理と語り合う秘密の言語であることを理解しました。</p>

                <!-- PT -->
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Num mosteiro remoto, o jovem Minh tinha apenas uma tarefa: varrer o pátio. Enquanto outros estudavam, Minh movia a sua vassoura com lentidão rítmica. Não varria apenas para tirar o pó; varria como se cada grão de areia fosse uma joia. Observava o vento e colocava cada pedra no seu lugar exato.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Anos depois, uma seca assolou a região. Os engenheiros não encontravam água. O imperador visitou o mosteiro desesperado. Minh olhou para cima e apontou para um ponto entre duas rochas. "A água está ali", disse calmamente. "A forma como as formigas caminham revela o pulsar da terra".</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Ao escavar ali, encontraram a água. Minh não tinha estudado engenharia, mas a sua atenção aos detalhes deu-lhe uma inteligência que via o invisível. O imperador ofereceu-lhe o cargo de conselheiro, mas Minh recusou.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">"Majestade", disse ele, "a sabedoria é uma forma de olhar. Se eu deixar de prestar atenção a como a folha cai, perderei a capacidade de ver como o mundo se move". Minh voltou à sua vassoura, compreendendo que o esmero é a linguagem secreta da alma.</p>

                <!-- VI -->
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Trong một ngôi chùa xa xôi trên núi, có một chú tiểu tên Minh mà công việc duy nhất là quét sân. Trong khi các vị sư khác nghiên cứu kinh sách, Minh dành hàng giờ đưa cây chổi tre với một nhịp điệu chậm rãi. Chú không chỉ quét để sạch bụi; chú quét như thể mỗi hạt cát là một viên ngọc quý. Chú quan sát gió thổi lá bay và đặt từng viên đá trên lối đi vào đúng vị trí của nó.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Nhiều năm trôi qua, một trận hạn hán lớn xảy ra. Các kỹ sư của hoàng đế mang bản đồ và tính toán đến, nhưng không ai hiểu được dòng nước ngầm chảy qua đâu. Hoàng đế tuyệt vọng đến thăm chùa. Minh đang quét sân, ngước mắt lên và chỉ vào một điểm giữa hai tảng đá. "Nước ở đó," chú bình thản nói. "Cách đàn kiến đi hôm nay và cách rêu mọc trong khe nứt đó tiết lộ mạch đập của đất trời."</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Khi đào tại đúng điểm đó, họ đã tìm thấy nguồn nước ngầm. Minh chưa bao giờ học về kỹ thuật, nhưng thói quen chú tâm tuyệt đối vào những điều nhỏ nhặt đã ban cho chú một trí tuệ nhìn thấu những điều vô hình. Hoàng đế mời chú làm cố vấn hoàng gia, nhưng Minh đã từ chối.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">"Tâu bệ hạ," chú nói, "trí tuệ không phải là một chức vụ, mà là một cách nhìn. Nếu con ngừng chú ý đến cách chiếc lá rơi trên sân, con sẽ mất khả năng nhìn thấy thế giới vận hành như thế nào." Minh quay lại với cây chổi của mình, hiểu rằng sự tận tâm chính là ngôn ngữ bí mật mà linh hồn trò chuyện với Chân lý.</p>
            </div>

            <!-- ═══ ART ═══ -->
            <div class="final-art fade-in" style="text-align: center; margin-top: 4rem; margin-bottom: 2rem;">
                <img src="assets/art.jpg" alt="Obra de Arte Karma LX" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            </div>

            <!-- ═══ MORAL ═══ -->
            <div class="moral fade-in">
                <span class="es">El esmero es el gimnasio del genio; cuida lo pequeño y el universo te revelará lo grande.</span>
                <span class="en">Care is the gymnasium of genius; look after the small things and the universe will reveal the great things to you.</span>
                <span class="it">La cura è la palestra del genio; cura le piccole cose e l'universo ti rivelerà le grandi.</span>
                <span class="zh">细致是天才的健身房；照顾好小事，宇宙就会向你展示大事。</span>
                <span class="ar">العناية هي صالة ألعاب العبقرية؛ اهتم بالصغير وسيكشف لك الكون عن الكبير.</span>
                <span class="ru">Старание — это гимнастический зал для гения; заботься о малом, и Вселенная откроет тебе великое.</span>
                <span class="de">Sorgfalt ist die Turnhalle des Genies; kümmere dich um das Kleine, und das Universum wird dir das Große offenbaren.</span>
                <span class="fr">Le soin est le gymnase du génie ; soigne les petites choses et l'univers te révélera les grandes.</span>
                <span class="ja">丹精は天才の鍛錬の場です。小さなことを大切にすれば、宇宙は大きなことを明らかにしてくれます。</span>
                <span class="pt">O esmero é o ginásio do génio; cuida do pequeno e o universo revelar-te-á o grande.</span>
                <span class="vi">Sự tận tâm là phòng tập của thiên tài; hãy chăm sóc những điều nhỏ bé và vũ trụ sẽ hé lộ cho bạn những điều lớn lao.</span>
            </div>

            <center class="fade-in" style="margin-top: 4rem;">
                <img src="assets/hero.jpg" alt="Karma LX Full" style="max-width: 600px; width: 100%; border-radius: 8px; border: 1px solid rgba(197,160,89,0.3); box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
            </center>

            <!-- ═══ INSPIRACIÓN ORIGINAL ═══ -->
            <div class="original-inspiration fade-in" style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid rgba(197,160,89,0.3);">
                <h3 class="es" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: 'Cinzel', serif;">La Inspiración Original</h3>
                <h3 class="en" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: 'Cinzel', serif;">The Original Inspiration</h3>

                <center>
                    <img src="assets/pasaje_original.png" alt="Tranh Nhân Quả Original" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 2rem;">
                </center>

                <div class="translation-box" style="background: rgba(0,0,0,0.4); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--gold); max-width: 800px; margin: 0 auto;">
                    <p class="vi" style="color: #fff; font-style: italic; margin-bottom: 2rem; font-family: 'EB Garamond', serif; font-size: 1.2rem;">
                        <strong>🇻🇳 Tiếng Việt:</strong><br>Nhân: Cẩn thận trong từng việc làm nhỏ nhặt.<br>Quả: Thông minh lên dần dần.
                    </p>
                    <p style="color: #ddd; margin-bottom: 1.5rem;"><strong>🇬🇧 English:</strong><br>Cause: Doing everything with extra care.<br>Effect: Brings a smarter and smarter brain.</p>
                    <p class="es" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197,160,89,0.1); padding: 1rem; border-left: 3px solid var(--gold);"><strong>Traducción Recreada:</strong><br>Causa: Realizar cada tarea, por pequeña que sea, con máximo cuidado, esmero y atención plena.<br>Efecto: Desarrollo progresivo de una inteligencia brillante y una mente perspicaz.</p>
                </div>
            </div>

            <div class="linktree-subtle fade-in" style="margin-top: 6rem; padding: 3rem 0; border-top: 1px solid rgba(197,160,89,0.2); text-align: center;">
                <p class="es" style="color: #999; font-style: italic; margin-bottom: 1.5rem;">Si quieres conocer más sobre el proyecto o colaborar, accede a nuestro <a href="../../linktree.html" style="color: var(--gold); text-decoration: none; border-bottom: 1px dotted var(--gold);">Linktree</a>.</p>
            </div>
        </div>
    </main>

    <script src="../../shared/script.js"></script>
</body>
</html>
"""

with open("/Users/fjbanezares/libro del karma/60_esmero_pequenas_cosas_inteligencia/web/index.html", "w") as f:
    f.write(html_content)

print("Chapter 60 HTML successfully updated with all 11 languages.")
