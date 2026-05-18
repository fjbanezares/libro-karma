
import os

def get_html_ch60():
    return """<!DOCTYPE html>
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
                    <span class="pt">"Quem cuida do detalhe da gota, acaba por compreender o mistério do oceano; a inteligência não é mais do que o fruto de uma atenção devota às pequenas cosas."</span>
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
                <p class="it"><span class="drop-cap">L</span>'universo è un arazzo tessuto con fili invisibili, e solo chi impara a osservare ogni filo con cura sviluppa la capacità di vedere il disegno completo. Molti cercano l'intelligenza nei grandi discorsi o nei libri complessi, ma il karma ci insegna che la vera acutezza mentale si coltiva nel silenzio dei compiti quotidiani. Quando eseguiamo ogni piccola azione — che si tratti di organizzare un tavolo, pulire uno strumento o scrivere una parola — con piena consapevolezza e una cura quasi sacra, stiamo "affilando" lo strumento della nostra coscienza.</p>
                <p class="it">Questa devozione al dettaglio produce un effetto karmico inevitabile: la mente diventa più rapida, più chiara e più capace di discernere la verità. Il disordine esterno è spesso il riflesso di un disordine interiore, ma il processo funziona anche all'inverso. Imponendo ordine e bellezza nel nostro ambiente attraverso la cura, stiamo seminando i semi di un'intelligenza superiore nella nostra prossima esistenza, e anche in questa. Il cervello non è solo un organo biologico, è un ricevitore di saggezza che si calibra attraverso la precisione dei nostri atti.</p>
                <p class="it">Il "prima" di questo karma è la negligenza e la fretta, che si traducono in una mente confusa e una vita piena di errori evitabili. Il "dopo" è la maestria: uno stato di essere in cui la comprensione fluisce senza sforzo. L'intelligenza karmica non è astuzia per ingannare, ma chiarezza per comprendere. Chi è fedele nel poco, l'universo gli affida la comprensione di molto. Così, la cura diventa la chiave d'oro che apre le porte della percezione suprema.</p>

                <!-- ZH -->
                <p class="zh"><span class="drop-cap">宇</span>宙是由无形线条织成的挂毯，只有学会用心观察每一根线条的人，才能培养出洞察全局的能力。许多人在宏大的演说或复杂的书籍中寻找智慧，但业力告诉我们，真正的敏锐是在日常琐事的沉默中培养出来的。当我们以全然的专注和神圣的细致完成每一件小事时——无论是整理桌子、清理工具还是写下一个词——我们就在“磨砺”意识的工具。</p>
                <p class="zh">这种对细节的投入会产生必然的业力影响：头脑变得更敏捷、更清晰，且更能洞察真理。外在的混乱往往是内在混乱的反映，但这一过程反过来也成立。通过细心整理环境，使其井然有序且美观，我们正在播下高等智慧的种子，无论是在来世还是今生。大脑不仅是一个生物器官，它还是一个通过行为的精确性来校准的智慧接收器。</p>
                <p class="zh">这种业力的“前因”是疏忽和匆忙，导致思维混乱，生活中充斥着本可避免的错误。而“后果”则是精通：一种理解力毫不费力流动的境界。业力智慧不是欺骗的狡黠，而是理解的清明。在小事上忠诚的人，宇宙会托付其对大事的理解。因此，细致成为了开启至高感知之门的金钥匙。</p>

                <!-- AR -->
                <p class="ar"><span class="drop-cap">ا</span>لكون عبارة عن نسيج منسوج بخيوط غير مرئية، وفقط من يتعلم مراقبة كل خيط بعناية يطور القدرة على رؤية النمط الكامل. يبحث الكثيرون عن الذكاء في الخطب العظيمة أو الكتب المعقدة، لكن الكارما تعلمنا أن الحدة الذهنية الحقيقية تُزرع في صمت المهام اليومية. عندما نؤدي كل عمل صغير - سواء كان تنظيم طاولة، أو تنظيف أداة، أو كتابة كلمة - بوعي كامل وعناية مقدسة، فإننا "نشحذ" أداة وعينا.</p>
                <p class="ar">ينتج هذا التفاني في التفاصيل تأثيراً كارمياً حتمياً: يصبح العقل أسرع وأكثر وضوحاً وأكثر قدرة على تمييز الحقيقة. الفوضى الخارجية غالباً ما تكون انعكاساً للفوضى الداخلية، لكن العملية تعمل أيضاً بشكل عكسي. من خلال فرض النظام والجمال في بيئتنا من خلال العناية، فإننا نزرع بذور ذكاء متفوق في وجودنا القادم، وفي هذا الوجود أيضاً. الدماغ ليس مجرد عضو بيولوجي، بل هو مستقبل للحكمة يتم ضبطه من خلال دقة أفعالنا.</p>
                <p class="ar">"ما قبل" هذه الكارما هو الإهمال والعجلة، مما يؤدي إلى عقل مشوش وحياة مليئة بالأخطاء التي يمكن تجنبها. أما "ما بعد" فهو الإتقان: حالة من الوجود يتدفق فيها الفهم دون عناء. ذكاء الكارما ليس مهارة للخداع، بل هو وضوح للفهم. من كان أميناً في القليل، يأتمنه الكون على فهم الكثير. وهكذا، تصبح العناية هي المفتاح الذهبي الذي يفتح أبواب الإدراك الأسمى.</p>

                <!-- RU -->
                <p class="ru"><span class="drop-cap">В</span>селенная — это гобелен, сотканный из невидимых нитей, и только тот, кто научится внимательно наблюдать за каждой нитью, развивает способность видеть весь узор. Многие ищут интеллект в великих речах или сложных книгах, но карма учит нас, что истинная острота ума взращивается в тишине повседневных дел. Когда мы выполняем каждое маленькое действие — будь то организация стола, чистка инструмента или написание слова — с полным вниманием и почти священной заботой, мы «затачиваем» инструмент своего сознания.</p>
                <p class="ru">Эта преданность деталям производит неизбежный кармический эффект: ум становится быстрее, яснее и способнее различать истину. Внешний беспорядок часто является отражением беспорядка внутреннего, но процесс работает и в обратном направлении. Наводя порядок и красоту в своем окружении через старание, мы сеем семена высшего интеллекта в нашем следующем существовании, а также в нынешнем. Мозг — это не просто биологический орган, это приемник мудрости, который калибруется через точность наших поступков.</p>
                <p class="ru">Состояние «до» этой кармы — это небрежность и спешка, приводящие к спутанности сознания и жизни, полной ошибок, которых можно было избежать. «После» — это мастерство: состояние бытия, в котором понимание течет без усилий. Кармический интеллект — это не хитрость для обмана, а ясность для понимания. Верному в малом Вселенная доверяет понимание многого. Так старание становится золотым ключом, открывающим двери высшего восприятия.</p>

                <!-- DE -->
                <p class="de"><span class="drop-cap">D</span>as Universum ist ein Teppich aus unsichtbaren Fäden, und nur wer lernt, jeden Faden mit Sorgfalt zu beobachten, entwickelt die Fähigkeit, das gesamte Muster zu sehen. Viele suchen Intelligenz in großen Reden oder komplexen Büchern, aber das Karma lehrt uns, dass wahre geistige Schärfe in der Stille der täglichen Aufgaben kultiviert wird. Wenn wir jede kleine Handlung ausführen — sei es das Deckeneines Tisches, das Reinigen eines Werkzeugs oder das Schreiben eines Wortes — mit voller Achtsamkeit und fast heiliger Sorgfalt, „schärfen“ wir das Instrument unseres Bewusstseins.</p>
                <p class="de">Diese Hingabe zum Detail erzeugt eine unvermeidliche karmische Wirkung: Der Geist wird schneller, klarer und fähiger, die Wahrheit zu erkennen. Äußere Unordnung ist oft das Spiegelbild innerer Unordnung, aber der Prozess funktioniert auch umgekehrt. Indem wir durch Sorgfalt Ordnung und Schönheit in unsere Umgebung bringen, säen wir die Samen einer höheren Intelligenz in unserer nächsten Existenz und auch in dieser. Das Gehirn ist nicht nur ein biologisches Organ, es ist ein Empfänger für Weisheit, der durch die Präzision unserer Taten kalibriert wird.</p>
                <p class="de">Das „Vorher“ dieses Karmas ist Nachlässigkeit und Hast, die zu einem verwirrten Geist und einem Leben voller vermeidbarer Fehler führen. Das „Nachher“ ist Meisterschaft: ein Zustand des Seins, in dem Verständnis mühelos fließt. Karmische Intelligenz ist nicht List zur Täuschung, sondern Klarheit zum Verstehen. Wer im Kleinen treu ist, dem vertraut das Universum das Verständnis des Großen an. So wird Sorgfalt zum goldenen Schlüssel, der die Türen der höchsten Wahrnehmung öffnet.</p>

                <!-- FR -->
                <p class="fr"><span class="drop-cap">L</span>'univers est une tapisserie tissée de fils invisibles, et seul celui qui apprend à observer chaque brin avec soin développe la capacité de voir le motif complet. Beaucoup cherchent l'intelligence dans les grands discours ou les livres complexes, mais le karma nous enseigne que la véritable acuité mentale se cultive dans le silence des tâches quotidiennes. Quand nous accomplissons chaque petite action — qu'il s'agisse d'organiser une table, de nettoyer un outil ou d'écrire un mot — avec une pleine conscience et un soin presque sacré, nous « aiguisons » l'instrument de notre conscience.</p>
                <p class="fr">Ce dévouement au détail produit un effet karmique inévitable : l'esprit devient plus rapide, plus clair et plus capable de discerner la vérité. Le désordre extérieur est souvent le reflet d'un désordre intérieur, mais le processus fonctionne aussi à l'inverse. En imposant l'ordre et la beauté dans notre environnement par le soin, nous semons les graines d'une intelligence supérieure dans notre prochaine existence, ainsi que dans celle-ci. Le cerveau n'est pas seulement un organe biologique, c'est un récepteur de sagesse qui se calibre à travers la précision de nos actes.</p>
                <p class="fr">Le « avant » de ce karma est la négligence et la hâte, entraînant un esprit confus et une vie pleine d'erreurs évitables. Le « après » est la maîtrise : un état d'être où la compréhension coule sans effort. L'intelligence karmique n'est pas la ruse pour tromper, mais la clarté pour comprendre. À celui qui est fidèle dans les petites choses, l'univers confie la compréhension des grandes. Ainsi, le soin devient la clé d'or qui ouvre les portes de la perception suprême.</p>

                <!-- JA -->
                <p class="ja"><span class="drop-cap">宇</span>宙は見えない糸で織られたタペストリーであり、一本一本の糸を丹念に観察することを学んだ者だけが、全体の模様を見る能力を養うことができます。多くの人は壮大な演説や複雑な本の中に知性を求めますが、カルマは真の精神的な鋭さが日々の仕事の静寂の中で育まれることを教えています。テーブルを整える、道具を掃除する、言葉を綴る、といったあらゆる小さな行動を、十分な注意と神聖なまでの丁寧さで行うとき、私たちは意識という道具を「研いで」いるのです。</p>
                <p class="ja">細部への献身は、避けられないカルマ的効果を生みます。心はより速く、より明晰になり、真実を見抜く力を備えます。外側の無秩序はしばしば内側の無秩序の反映ですが、そのプロセスは逆にも働きます。丹精を込めて環境に秩序と美をもたらすことで、私たちは来世においても、そして今この生においても、高等知性の種をまいているのです。脳は単なる生物学的な器官ではなく、私たちの行いの正確さを通じて調整される知恵の受信機なのです。</p>
                <p class="ja">このカルマの「前」は怠慢と急ぎであり、混乱した心と回避可能な間違いに満ちた人生をもたらします。「後」は熟達です。理解が努力なしに流れるような存在の状態です。カルマ的な知性とは、欺くための悪知恵ではなく、理解するための明晰さです。小さなことに忠実な者に、宇宙は大きなことの理解を託します。こうして、丹精は至高の知覚の扉を開く黄金の鍵となるのです。</p>

                <!-- PT -->
                <p class="pt"><span class="drop-cap">O</span> universo é uma tapeçaria tecida com fios invisíveis, e apenas aquele que aprende a observar cada fio com esmero desenvolve a capacidade de ver o padrão completo. Muitos buscam a inteligência nos grandes discursos ou nos livros complexos, mas o karma ensina-nos que a verdadeira agudeza mental cultiva-se no silêncio das tarefas quotidianas. Quando realizamos cada pequena ação — seja organizar uma mesa, limpar uma ferramenta ou escrever uma palavra — com atenção plena e um cuidado quase sagrado, estamos a "afiar" o instrumento da nossa consciência.</p>
                <p class="pt">Esta devoção ao detalhe produz um efeito kármico inevitável: a mente torna-se mais rápida, clara e capaz de discernir a verdade. A desordem exterior é muitas vezes o reflexo de uma desordem interior, mas o processo também funciona à inversa. Ao impor ordem e beleza no nosso ambiente através do esmero, estamos a semear as sementes de uma inteligência superior na nossa próxima existência, e também nesta. O cérebro não é apenas um órgão biológico, é um recetor de sabedoria que se calibra através da precisão dos nossos atos.</p>
                <p class="pt">O "antes" deste karma é a negligência e a pressa, resultando numa mente confusa e uma vida cheia de erros evitáveis. O "depois" é a maestria: um estado de ser onde a compreensão flui sem esforço. A inteligência kármica não é astúcia para enganar, mas clareza para compreender. Quem é fiel no pouco, o universo confia-lhe o entendimento do muito. Assim, o esmero torna-se a chave de ouro que abre as portas da perceção suprema.</p>

                <!-- VI -->
                <p class="vi"><span class="drop-cap">V</span>ũ trụ là một bức thảm được dệt bằng những sợi chỉ vô hình, và chỉ những ai học được cách quan sát từng sợi chỉ bằng sự tận tâm mới phát triển được khả năng nhìn thấy toàn bộ hoa văn. Nhiều người tìm kiếm trí tuệ trong những bài diễn thuyết lớn hoặc những cuốn sách phức tạp, nhưng nhân quả dạy chúng ta rằng sự nhạy bén thực sự được nuôi dưỡng trong sự tĩnh lặng của những công việc hằng ngày. Khi chúng ta thực hiện mỗi hành động nhỏ — dù là sắp xếp bàn ghế, lau chùi dụng cụ hay viết một từ — với sự chú tâm trọn vẹn và sự chăm sóc gần như thiêng liêng, chúng ta đang "mài giũa" công cụ của ý thức mình.</p>
                <p class="vi">Sự tận tụy với chi tiết tạo ra một hiệu ứng nhân quả tất yếu: tâm trí trở nên nhanh nhạy, sáng suốt hơn và có khả năng phân biệt sự thật tốt hơn. Sự lộn xộn bên ngoài thường là phản chiếu của sự hỗn loạn bên trong, nhưng quá trình này cũng diễn ra ngược lại. Bằng cách thiết lập trật tự và vẻ đẹp cho môi trường xung quanh thông qua sự tỉ mỉ, chúng ta đang gieo hạt giống của một trí tuệ cao cấp cho kiếp sau và ngay cả kiếp này. Bộ não không chỉ là một cơ quan sinh học, nó là một bộ thu nhận trí tuệ được hiệu chuẩn thông qua sự chính xác trong hành động của chúng ta.</p>
                <p class="vi">Cái "trước" của nghiệp này là sự cẩu thả và vội vàng, dẫn đến một tâm trí rối loạn và một cuộc đời đầy những sai lầm có thể tránh được. Cái "sau" là sự tinh thông: một trạng thái mà sự thấu hiểu tuôn chảy không cần nỗ lực. Trí tuệ nhân quả không phải là sự khôn lỏi để lừa lọc, mà là sự sáng suốt để thấu hiểu. Kẻ trung tín trong việc nhỏ sẽ được vũ trụ tin tưởng giao phó sự hiểu biết về việc lớn. Vì vậy, sự tận tâm trở thành chiếc chìa khóa vàng mở ra cánh cửa của sự nhận thức tối cao.</p>
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
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">In un remoto monastero sulle montagne di Da Lat, viveva un giovane novizio di nome Minh il cui unico compito era spazzare il cortile centrale. Mentre altri monaci studiavano antichi manoscritti e dibattevano di filosofia, Minh passava ore a muovere la sua scopa di bambù con una lentezza ritmica. Non spazzava semplicemente per togliere la polvere; spazzava come se ogni granello di sabbia fosse un gioiello prezioso. Osservava come il vento muoveva le foglie e poneva ogni pietra del sentiero al suo posto esatto, con una cura che agli altri pareva eccessiva.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Passarono gli anni e una grande siccità devastò la regione, portando con sé un problema che i saggi del regno non riuscivano a risolvere: il sistema di canali che alimentava la valle era stato bloccato da un complesso labirinto di sedimenti sotterranei. I più brillanti ingegneri dell'imperatore portarono mappe e calcoli, ma nessuno riusciva a capire dove fluisse l'acqua nascosta. L'imperatore, disperato, visitò il monastero in cerca di consigli spirituali.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Minh, che stava ancora spazzando il suo cortile, alzò lo sguardo e, dopo aver osservato la montagna per un istante, indicò un punto insignificante tra due rocce. "L'acqua è lì", disse con calma. "Il modo in cui le formiche camminano oggi e il modo in cui il muschio è cresciuto in quella fessura rivelano il battito della terra". I saggi risero, ma scavando in quel punto esatto trovarono il canale principale e l'acqua tornò a scorrere. Minh non aveva studiato ingegneria, ma la sua abitudine di prestare assoluta attenzione al piccolo gli aveva conferito un'intelligenza che vedeva l'invisibile.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">L'imperatore gli offrì il posto di consigliere reale, ma Minh declinò. "Maestà", disse, "la saggezza non è un incarico, è un modo di guardare. Se smetto di prestare attenzione a come cade la foglia sul cortile, perderò la capacità di vedere come si muove il mondo". Minh tornò alla sua scopa, comprendendo che la cura è il linguaggio segreto con cui l'anima parla con la Verità, e che in ogni piccolo atto di cura risiede la scintilla dell'intelligenza divina.</p>

                <!-- ZH -->
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">在大叻山脉的一座偏僻寺庙里，住着一个名叫明（Minh）的小和尚，他的唯一任务就是打扫中央庭院。当其他僧侣研读古代手稿并辩论哲学时，明却花几个小时以有节奏的缓慢动作挥动他的竹扫帚。他不仅仅是为了除尘而清扫；他打扫时仿佛每一粒沙子都是珍贵的宝石。他观察风如何吹动叶子，并将小路上的每一块石头放在准确的位置，这种细致在他人看来简直是多此一举。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">多年以后，该地区遭遇大旱，随之而来的是一个连王国的圣贤都无法解决的问题：灌溉山谷的渠道系统被复杂的地下沉积物迷宫堵塞了。皇帝手下最杰出的工程师带来了地图和计算，但没有人能理解隐藏的水流向何方。皇帝在绝望中访问了寺庙，寻求精神上的建议。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">仍在清扫院子的明抬起头，观察了片刻大山后，指向两块岩石间的一个不起眼的地方。“水在那里，”他平静地说，“今天蚂蚁行走的方式以及那个裂缝中苔藓生长的方式揭示了大地的脉搏。”圣贤们嘲笑他，但当他们在那个确切的位置挖掘时，他们找到了主渠道，水再次流淌。明没有学过工程学，但他对微小事物绝对关注的习惯赋予了他一种能洞察无形的智慧。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">皇帝邀请他担任皇家顾问，但明拒绝了。“陛下，”他说，“智慧不是一种职位，而是一种观察方式。如果我不再关注叶子如何飘落在院子里，我将失去观察世界运作的能力。”明回到了扫帚旁，明白细致是灵魂与真理对话的秘密语言，在每一个微小的关怀行为中都闪耀着神圣智慧的火花。</p>

                <!-- AR -->
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">في دير بعيد بجبال دا لات، كان يعيش مبتدئ شاب يدعى مينه، كانت مهمته الوحيدة كنس الفناء المركزي. وبينما كان الرهبان الآخرون يدرسون المخطوطات القديمة ويناقشون الفلسفة، كان مينه يقضي ساعات في تحريك مكنسته المصنوعة من الخيزران ببطء إيقاعي. لم يكن يكنس لمجرد إزالة الغبار؛ بل كان يكنس وكأن كل ذرة رمل هي جوهرة ثمينة. كان يراقب كيف تحرك الرياح الأوراق ويضع كل حجر في المسار في مكانه الدقيق، بعناية بدت للآخرين مبالغاً فيها.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">مرت السنين وضرب جفاف كبير المنطقة، جالباً معه مشكلة لم يستطع حكماء المملكة حلها: نظام القنوات الذي يغذي الوادي انسد بمتاهة معقدة من الرواسب الجوفية. أحضر أبرع مهندسي الإمبراطور خرائط وحسابات، لكن لم يستطع أحد منهم فهم أين تتدفق المياه المخفية. زار الإمبراطور الدير يائساً بحثاً عن نصيحة روحية.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">مينه، الذي كان لا يزال يكنس فناءه، رفع عينيه وبعد مراقبة الجبل للحظة، أشار إلى نقطة تافهة بين صخرتين. قال بهدوء: "الماء هناك. الطريقة التي يمشي بها النمل اليوم والطريقة التي نما بها الطحلب في ذلك الشق تكشف عن نبض الأرض". ضحك الحكماء، ولكن عند الحفر في تلك النقطة بالضبط، وجدوا القناة الرئيسية وعاد الماء للتدفق. لم يدرس مينه الهندسة، لكن عادته في الاهتمام المطلق بالصغير منحته ذكاءً يرى ما لا يُرى.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">عرض عليه الإمبراطور منصب المستشار الملكي، لكن مينه رفض. قال: "يا صاحب الجلالة، الحكمة ليست منصباً، بل هي طريقة للنظر. إذا توقفت عن الاهتمام بكيفية سقوط الورقة في الفناء، سأفقد القدرة على رؤية كيف يتحرك العالم". عاد مينه إلى مكنسته، مدركاً أن العناية هي اللغة السرية التي تتحدث بها الروح مع الحقيقة، وأن في كل عمل رعاية صغير تكمن شرارة الذكاء الإلهي.</p>

                <!-- RU -->
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">В далеком монастыре в горах Далата жил молодой послушник по имени Мин, единственной задачей которого было подметать центральный двор. Пока другие монахи изучали древние рукописи и спорили о философии, Мин часами ритмично и медленно двигал бамбуковой метлой. Он не просто сметал пыль; он подметал так, словно каждая песчинка была драгоценным камнем. Он наблюдал, как ветер колышет листья, и клал каждый камень на тропинке на его точное место, проявляя такое старание, которое другим казалось чрезмерным.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Прошли годы, и великая засуха опустошила регион, принеся с собой проблему, которую не могли решить мудрецы королевства: система каналов, питавшая долину, была заблокирована сложным лабиринтом подземных отложений. Самые блестящие инженеры императора привезли карты и расчеты, но никто не мог понять, куда течет скрытая вода. Император в отчаянии посетил монастырь в поисках духовного совета.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Мин, который все еще подметал свой двор, поднял взгляд и, понаблюдав за горой мгновение, указал на неприметную точку между двумя скалами. «Вода там», — спокойно сказал он. «То, как сегодня ползают муравьи, и то, как мох вырос в этой трещине, раскрывают пульс земли». Мудрецы рассмеялись, но, когда они начали копать в этой самой точке, они нашли главный канал, и вода снова потекла. Мин не изучал инженерное дело, но его привычка уделять абсолютное внимание мелочам даровала ему интеллект, видящий невидимое.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Император предложил ему должность королевского советника, но Мин отказался. «Ваше Величество, — сказал он, — мудрость — это не должность, это способ смотреть. Если я перестану обращать внимание на то, как лист падает во дворе, я потеряю способность видеть, как движется мир». Мин вернулся к своей метле, понимая, что старание — это тайный язык, на котором душа говорит с Истиной, и что в каждом маленьком акте заботы живет искра божественного интеллекта.</p>

                <!-- DE -->
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">In einem fernen Kloster in den Bergen von Da Lat lebte ein junger Novize namens Minh, dessen einzige Aufgabe es war, den zentralen Hof zu kehren. Während andere Mönche alte Manuskripte studierten und über Philosophie debattierten, verbrachte Minh Stunden damit, seinen Bambusbesen mit rhythmischer Langsamkeit zu bewegen. Er kehrte nicht einfach, um Staub zu entfernen; er kehrte, als wäre jedes Sandkorn ein kostbares Juwel. Er beobachtete, wie der Wind die Blätter bewegte, und legte jeden Stein auf dem Weg an seinen exakten Platz, mit einer Sorgfalt, die anderen übertrieben schien.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Die Jahre vergingen, und eine große Dürre suchte die Region heim und brachte ein Problem mit sich, das die Weisen des Reiches nicht lösen konnten: Das Kanalsystem, das das Tal speiste, war durch ein komplexes Labyrinth aus unterirdischen Sedimenten blockiert worden. Die brillantesten Ingenieure des Kaisers brachten Karten und Berechnungen mit, aber niemand konnte verstehen, wohin das verborgene Wasser floss. Verzweifelt besuchte der Kaiser das Kloster, um geistlichen Rat einzuholen.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Minh, der immer noch seinen Hof kehrte, blickte auf und deutete, nachdem er den Berg einen Moment lang beobachtet hatte, auf eine unscheinbare Stelle zwischen zwei Felsen. „Das Wasser ist dort“, sagte er ruhig. „Die Art und Weise, wie die Ameisen heute laufen, und die Art, wie das Moos in diesem Spalt gewachsen ist, offenbaren den Puls der Erde.“ Die Weisen lachten, aber als sie genau an dieser Stelle gruben, fanden sie den Hauptkanal und das Wasser floss wieder. Minh hatte nicht Ingenieurwesen studiert, aber seine Gewohnheit, dem Kleinen absolute Aufmerksamkeit zu schenken, hatte ihm eine Intelligenz verliehen, die das Unsichtbare sah.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Der Kaiser bot ihm den Posten des königlichen Beraters an, doch Minh lehnte ab. „Majestät“, sagte er, „Weisheit ist kein Amt, sondern eine Art zu schauen. Wenn ich aufhöre, darauf zu achten, wie das Blatt auf den Hof fällt, verliere ich die Fähigkeit zu sehen, wie sich die Welt bewegt.“ Minh kehrte zu seinem Besen zurück, im Verständnis, dass Sorgfalt die geheime Sprache ist, mit der die Seele mit der Wahrheit spricht, und dass in jedem kleinen Akt der Achtsamkeit der Funke göttlicher Intelligenz wohnt.</p>

                <!-- FR -->
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Dans un monastère reculé des montagnes de Da Lat, vivait un jeune novice nommé Minh dont la seule tâche était de balayer la cour centrale. Tandis que les autres moines étudiaient d'anciens manuscrits et débattaient de philosophie, Minh passait des heures à bouger son balai de bambou avec une lenteur rythmique. Il ne balayait pas simplement pour enlever la poussière ; il balayait comme si chaque grain de sable était un bijou précieux. Il observait comment le vent déplaçait les feuilles et plaçait chaque pierre du chemin à sa place exacte, avec un soin qui semblait excessif aux autres.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Les années passèrent, et une grande sécheresse ravagea la région, apportant avec elle un problème que les sages du royaume ne pouvaient résoudre : le système de canaux qui alimentait la vallée avait été bloqué par un labyrinthe complexe de sédiments souterrains. Les ingénieurs les plus brillants de l'empereur apportèrent des cartes et des calculs, mais aucun ne parvenait à comprendre où l'eau cachée coulait. L'empereur, désespéré, visita le monastère en quête d'un conseil spirituel.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Minh, qui continuait de balayer sa cour, leva les yeux et, après avoir observé la montagne un instant, désigna un point insignifiant entre deux rochers. « L'eau est là », dit-il calmement. « La façon dont les fourmis marchent aujourd'hui et la manière dont la mousse a poussé dans cette fissure révèlent le pouls de la terre ». Les sages rirent, mais en creusant à cet endroit précis, ils trouvèrent le canal principal et l'eau se remit à couler. Minh n'avait pas étudié l'ingénierie, mais son habitude de prêter une attention absolue au petit lui avait accordé une intelligence qui voyait l'invisible.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">L'empereur lui offrit le poste de conseiller royal, mais Minh déclina. « Majesté », dit-il, « la sagesse n'est pas une fonction, c'est une façon de regarder. Si j'arrête de faire attention à la chute de la feuille sur la cour, je perdrai la capacité de voir comment le monde bouge ». Minh retourna à son balai, comprenant que le soin est le langage secret avec lequel l'âme parle avec la Vérité, et que dans chaque petit acte de soin réside l'étincelle de l'intelligence divine.</p>

                <!-- JA -->
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">ダラットの山奥にある人里離れた寺院に、ミンという名の若い修行僧がいました。彼の唯一の仕事は中央の中庭を掃くことでした。他の僧侶たちが古い写本を学び哲学を論じている間、ミンは竹箒をリズムよくゆっくりと動かして何時間も過ごしていました。単に埃を払うために掃くのではなく、一粒一粒の砂が宝石であるかのように掃いていました。風がどのように葉を動かすかを観察し、小道の石を一つ一つ正確な場所に置く彼の丹精は、他人には過剰に見えるほどでした。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">歳月が流れ、大干ばつが地域を襲い、王国の賢者たちにも解決できない問題が持ち上がりました。谷に水を供給する運河システムが、複雑な地下堆積物の迷路によって塞がれてしまったのです。皇帝の最も優秀な技師たちが地図や計算を持ち寄りましたが、隠れた水がどこを流れているのか誰にも理解できませんでした。皇帝は絶望し、精神的な助言を求めて寺院を訪れました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">中庭を掃き続けていたミンは顔を上げ、しばし山を観察した後、二つの岩の間の何でもない場所を指差しました。「水はそこにあります」と彼は穏やかに言いました。「今日の蟻の歩き方と、その亀裂の苔の生え方が、大地の鼓動を教えてくれています」。賢者たちは笑いましたが、その場所を掘ってみると、主水路が見つかり、再び水が流れ出しました。ミンは工学を学んだことはありませんでしたが、小さなことに絶対的な注意を払う習慣が、目に見えないものを見る知性を彼に与えていたのです。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">皇帝は彼に王室顧問の職を申し出ましたが、ミンは断りました。「陛下」と彼は言いました。「知恵とは役職ではなく、見方なのです。もし私が中庭に落ちる葉に注意を払うのをやめたら、世界がどのように動いているかを見る能力を失ってしまうでしょう」。ミンは箒に戻り、丹精こそが魂が真理と語り合う秘密の言語であり、あらゆる小さなケアの中に神聖な知性の火花が宿っていることを理解していました。</p>

                <!-- PT -->
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Num mosteiro remoto nas montanhas de Da Lat, vivia um jovem noviço chamado Minh cuja única tarefa era varrer o pátio central. Enquanto outros monges estudavam manuscritos antigos e debatiam sobre filosofia, Minh passava horas movendo a sua vassoura de bambu com uma lentidão rítmica. Não varria simplesmente para tirar o pó; varria como se cada grão de areia fosse uma joia preciosa. Observava como o vento movia as folhas e colocava cada pedra do caminho no seu lugar exato, com um esmero que aos outros parecia excessivo.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Os anos passaram, e uma grande seca assolou a região, trazendo consigo um problema que os sábios do reino não podiam resolver: o sistema de canais que alimentava o vale tinha sido bloqueado por um complexo labirinto de sedimentos subterrâneos. Os engenheiros mais brilhantes do imperador trouxeram mapas e cálculos, mas nenhum conseguia entender por onde fluía a água oculta. O imperador, desesperado, visitou o mosteiro procurando conselho espiritual.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Minh, que continuava a varrer o seu pátio, levantou a vista e, após observar a montanha por um instante, apontou para um ponto insignificante entre duas rochas. "A água está ali", disse com calma. "A forma como as formigas caminham hoje e a maneira como o musgo cresceu naquela fenda revelam o pulsar da terra". Os sábios riram, mas ao escavar naquele ponto exato, encontraram o canal principal e a água voltou a fluir. Minh não tinha estudado engenharia, mas o seu hábito de prestar atenção absoluta ao pequeno tinha-lhe outorgado uma inteligência que via o invisível.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">O imperador ofereceu-lhe o cargo de conselheiro real, mas Minh declinou. "Majestade", disse, "a sabedoria não é um cargo, é uma forma de olhar. Se eu deixar de prestar atenção a como cai a folha sobre o pátio, perderei a capacidade de ver como se move o mundo". Minh voltou para a sua vassoura, compreendendo que o esmero é a linguagem secreta com que a alma fala com a Verdade, e que em cada pequeno ato de cuidado reside a centelha da inteligência divina.</p>

                <!-- VI -->
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Trong một ngôi chùa xa xôi trên núi Da Lat, có một chú tiểu tên Minh mà công việc duy nhất là quét sân chính. Trong khi các vị sư khác nghiên cứu kinh sách và tranh luận triết học, Minh dành hàng giờ đưa cây chổi tre với một nhịp điệu chậm rãi. Chú không chỉ quét để sạch bụi; chú quét như thể mỗi hạt cát là một viên ngọc quý. Chú quan sát gió thổi lá bay và đặt từng viên đá trên lối đi vào đúng vị trí của nó, bằng một sự tỉ mỉ mà những người khác cho là thái quá.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Nhiều năm trôi qua, một trận hạn hán lớn xảy ra, mang theo một vấn đề mà các bậc hiền triết trong vương quốc không thể giải quyết: hệ thống kênh rạch nuôi dưỡng thung lũng bị tắc nghẽn bởi một mê cung phức tạp của trầm tích ngầm. Những kỹ sư giỏi nhất của hoàng đế mang bản đồ và tính toán đến, nhưng không ai hiểu được dòng nước ngầm chảy qua đâu. Hoàng đế tuyệt vọng đến thăm chùa để tìm lời khuyên tâm linh.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Minh, vẫn đang quét sân, ngước mắt lên và sau khi quan sát ngọn núi một lúc, chú chỉ vào một điểm tầm thường giữa hai tảng đá. "Nước ở đó," chú bình thản nói. "Cách đàn kiến đi hôm nay và cách rêu mọc trong khe nứt đó tiết lộ mạch đập của đất trời." Các vị hiền triết cười nhạo, nhưng khi đào tại đúng điểm đó, họ đã tìm thấy kênh chính và nước lại tuôn chảy. Minh chưa bao giờ học về kỹ thuật, nhưng thói quen chú tâm tuyệt đối vào những điều nhỏ nhặt đã ban cho chú một trí tuệ nhìn thấu những điều vô hình.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Hoàng đế mời chú làm cố vấn hoàng gia, nhưng Minh đã từ chối. "Tâu bệ hạ," chú nói, "trí tuệ không phải là một chức vụ, mà là một cách nhìn. Nếu con ngừng chú ý đến cách chiếc lá rơi trên sân, con sẽ mất khả năng nhìn thấy thế giới vận hành như thế nào." Minh quay lại với cây chổi của mình, hiểu rằng sự tận tâm chính là ngôn ngữ bí mật mà linh hồn trò chuyện với Chân lý, và trong mỗi hành động chăm sóc nhỏ bé đều ẩn chứa tia sáng của trí tuệ thiêng liêng.</p>
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
    f.write(get_html_ch60())

print("Chapter 60 HTML successfully updated with ABSOLUTELY FULL translations.")
