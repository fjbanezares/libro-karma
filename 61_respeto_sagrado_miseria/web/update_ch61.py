
import os

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capítulo LXI: El Libro del Karma</title>
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
            <img src="assets/hero.jpg" alt="Karma LXI" id="hero-img">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <div class="chapter-num">
                    <span class="es">CAPÍTULO LXI</span><span class="en">CHAPTER LXI</span><span class="it">CAPITOLO LXI</span><span class="zh">第六十一章</span><span class="ar">الفصل الحادي والستون</span><span class="ru">ГЛАВА LXI</span><span class="de">KAPITEL LXI</span><span class="fr">CHAPITRE LXI</span><span class="ja">第61章</span><span class="pt">CAPÍTULO LXI</span><span class="vi">CHƯƠNG LXI</span>
                </div>
                <h1 class="chapter-title">
                    <span class="es">La Profanación de lo Invisible</span>
                    <span class="en">The Profanation of the Invisible</span>
                    <span class="it">La Profanazione dell'Invisibile</span>
                    <span class="zh">亵渎无形</span>
                    <span class="ar">تدنيس غير المرئي</span>
                    <span class="ru">Осквернение невидимого</span>
                    <span class="de">Die Entweihung des Unsichtbaren</span>
                    <span class="fr">La Profanation de l'Invisible</span>
                    <span class="ja">見えざるものの冒涜</span>
                    <span class="pt">A Profanação do Invisível</span>
                    <span class="vi">Sự Xúc Phạm Đấng Linh Thiêng</span>
                </h1>
                <p class="subtitle">
                    <span class="es">"No es la piedra lo que sangra cuando la tratas con desdén, sino el hilo de oro que unía tu espíritu al cielo."</span>
                    <span class="en">"It is not the stone that bleeds when you treat it with disdain, but the golden thread that united your spirit to heaven."</span>
                    <span class="it">"Non è la pietra a sanguinare quando la tratti con disdegno, ma il filo d'oro che univa il tuo spirito al cielo."</span>
                    <span class="zh">“当你蔑视它时，流血的不是石头，而是将你的灵魂与上天相连的金线。”</span>
                    <span class="ar">"ليس الحجر هو الذي ينزف عندما تعامله بازدراء، بل الخيط الذهبي الذي كان يربط روحك بالسماء."</span>
                    <span class="ru">«Не камень истекает кровью, когда ты относишься к нему с презрением, а та золотая нить, что связывала твой дух с небесами».</span>
                    <span class="de">„Es ist nicht der Stein, der blutet, wenn du ihn mit Verachtung behandelst, sondern der goldene Faden, der deinen Geist mit dem Himmel verband.“</span>
                    <span class="fr">« Ce n'est pas la pierre qui saigne quand tu la traites avec dédain, mais le fil d'or qui unissait ton esprit au ciel. »</span>
                    <span class="ja">「あなたが軽蔑をもって接したとき、血を流すのは石ではなく、あなたの魂を天国と結びつけていた黄金の糸なのです。」</span>
                    <span class="pt">"Não é a pedra que sangra quando a tratas com desdém, mas o fio de ouro que unia o teu espírito ao céu."</span>
                    <span class="vi">"Không phải đá sẽ rỉ máu khi bạn đối xử với nó bằng sự khinh miệt, mà chính là sợi chỉ vàng đã gắn kết linh hồn bạn với thiên thượng."</span>
                </p>
                <div class="scroll-indicator"></div>
            </div>
        </section>

        <div class="story-container">
            <!-- ═══ EXPLICACIÓN KÁRMICA ═══ -->
            <div class="story-block fade-in">
                <!-- ES -->
                <p class="es"><span class="drop-cap">L</span>o sagrado no es una cuestión de religión, sino de reverencia ante el misterio de la vida. Cuando un ser humano toma un símbolo de la divinidad —una imagen que representa la aspiración más alta de paz y sabiduría— y la rebaja al nivel de un adorno banal o, peor aún, la utiliza con falta de respeto en ambientes de vicio o frivolidad, está cometiendo un acto de suicidio espiritual. No se puede habitar en la luz mientras se oscurece la lámpara que la proyecta. El karma de la profanación no es un castigo externo, sino el vaciamiento interno de la propia gracia.</p>
                <p class="es">La ley de causa y efecto nos dice que al tratar lo sagrado con desdén, estamos declarando que no hay nada más allá de nuestra comodidad inmediata. Esa declaración se convierte en nuestra realidad: la vida pierde su "aura" de protección y significado. Quien usa la imagen de un santo para decorar su desidia, pronto descubrirá que en sus momentos de verdadera necesidad, no encuentra consuelo en ninguna parte. La belleza y la paz huyen de aquel que no sabe honrar su fuente. La miseria que sigue a este acto es la soledad de un alma que ha cortado sus propias raíces celestiales.</p>
                <p class="es">El "antes" de este karma es una vida llena de objetos lujosos pero vacíos de espíritu, donde lo sagrado se exhibe pero no se vive. El "después" es el desierto: una existencia donde la tragedia parece no tener fin porque hemos perdido la brújula de la reverencia. Para sanar este karma, debemos aprender a mirar con los ojos del corazón, reconociendo que cada símbolo es una puerta que solo se abre ante la humildad. Solo aquel que sabe postrarse ante lo que es más grande que él mismo, recupera la dignidad de estar de pie ante el mundo.</p>

                <!-- EN -->
                <p class="en"><span class="drop-cap">T</span>he sacred is not a matter of religion, but of reverence before the mystery of life. When a human being takes a symbol of divinity—an image representing the highest aspiration of peace and wisdom—and lowers it to the level of a banal ornament or, worse yet, uses it disrespectfully in environments of vice or frivolity, they are committing an act of spiritual suicide. One cannot dwell in the light while darkening the lamp that projects it. The karma of profanation is not an external punishment, but the internal emptying of one's own grace.</p>
                <p class="en">The law of cause and effect tells us that by treating the sacred with disdain, we are declaring that there is nothing beyond our immediate comfort. That declaration becomes our reality: life loses its "aura" of protection and meaning. He who uses the image of a saint to decorate his negligence will soon discover that in his moments of true need, he finds comfort nowhere. Beauty and peace flee from those who do not know how to honor their source. The misery that follows this act is the loneliness of a soul that has cut its own celestial roots.</p>
                <p class="en">The "before" of this karma is a life full of luxurious objects but empty of spirit, where the sacred is displayed but not lived. The "after" is the desert: an existence where tragedy seems endless because we have lost the compass of reverence. To heal this karma, we must learn to look with the eyes of the heart, recognizing that every symbol is a door that only opens before humility. Only he who knows how to bow before what is greater than himself regains the dignity of standing upright before the world.</p>

                <!-- IT -->
                <p class="it"><span class="drop-cap">I</span>l sacro non è una questione di religione, ma di riverenza verso il mistero della vita. Quando un essere umano usa un simbolo della divinità come banale ornamento o con mancanza di rispetto, compie un atto di suicidio spirituale. Non si può abitare nella luce mentre si oscura la lampada che la proietta. Il karma della profanazione è lo svuotamento interno della propria grazia.</p>
                <p class="it">La legge di causa ed effetto ci dice che trattando il sacro con sdegno, perdiamo l'aura di protezione e significato. Chi usa l'immagine di un santo per decorare la propria indolenza, nei momenti di bisogno non troverà conforto. La miseria che segue è la solitudine di un'anima che ha reciso le proprie radici celesti.</p>
                <p class="it">Il "prima" di questo karma è una vita piena di oggetti lussuosi ma vuoti di spirito. Il "dopo" è il deserto: un'esistenza dove la tragedia sembra infinita. Per guarire, dobbiamo imparare a guardare con gli occhi del cuore, riconoscendo che ogni simbolo è una porta che si apre solo davanti all'umiltà.</p>

                <!-- ZH -->
                <p class="zh"><span class="drop-cap">神</span>圣并非宗教问题，而是对生命奥秘的敬畏。当人将神圣象征贬低为平庸的装饰，或在轻浮的环境中无礼使用时，便是在进行精神自杀。在熄灭投射光芒的灯火时，人无法居住在光中。亵渎的业力并非外在惩罚，而是自身恩典的内在枯竭。</p>
                <p class="zh">因果定律告诉我们，轻视神圣意味着宣称除了眼前舒适外别无他物。生命因此失去保护感与意义。将圣像用于装点懒散的人，在真正需要时将无处寻找慰藉。随之而来的痛苦，是切断了自身上天根基后的灵魂孤独。</p>
                <p class="zh">这种业力的“前因”是拥有奢华却精神空虚的对象。而“后果”则是荒漠：由于失去敬畏的指南针，悲剧似乎永无止境。要治愈这种业力，必须学会用心灵之眼观察，承认每个象征都是唯有在谦卑面前才会开启的门。</p>

                <!-- AR -->
                <p class="ar"><span class="drop-cap">ا</span>لمقدس ليس مسألة دين، بل هو توقير أمام سر الحياة. عندما يحول الإنسان رمزاً للإلهية إلى زينة تافهة أو يستخدمه بازدراء، فإنه يرتكب انتحاراً روحياً. لا يمكن للمرء أن يسكن في النور بينما يظلم المصباح الذي يشعه. كارما التدنيس هي إفراغ داخلي للنعمة الشخصية.</p>
                <p class="ar">يخبرنا قانون السبب والنتيجة أن معاملة المقدس بازدراء تجعل الحياة تفقد هالتها من الحماية والمعنى. من يستخدم صورة قديس لتزيين تكاسله، لن يجد عزاءً في أوقات حاجته الحقيقية. البؤس الذي يتبع ذلك هو وحدة الروح التي قطعت جذورها السماوية.</p>
                <p class="ar">"ما قبل" هذه الكارما هي حياة مليئة بالأشياء الفاخرة ولكنها خالية من الروح. أما "ما بعد" فهو الصحراء: وجود تبدو فيه المأساة بلا نهاية. لشفاء هذه الكارما، يجب أن نتعلم النظر بعيون القلب، مدركين أن كل رمز هو باب لا يُفتح إلا أمام التواضع.</p>

                <!-- RU -->
                <p class="ru"><span class="drop-cap">С</span>вященное — это не вопрос религии, а вопрос почтения перед тайной жизни. Когда человек низводит символ божественности до уровня банального украшения или использует его неуважительно, он совершает акт духовного самоубийства. Нельзя пребывать в свете, гася лампу, которая его излучает. Карма осквернения — это внутреннее опустошение собственной благодати.</p>
                <p class="ru">Закон причины и следствия говорит нам, что, относясь к священному с пренебрежением, мы лишаем жизнь защиты и смысла. Тот, кто использует святой образ для украшения своего безделья, в минуты нужды не найдет утешения. Страдание, следующее за этим — одиночество души, обрубившей свои небесные корни.</p>
                <p class="ru">Состояние «до» этой кармы — жизнь, полная роскошных, но пустых вещей. «После» — пустыня: существование, где трагедия кажется бесконечной. Чтобы исцелиться, мы должны научиться смотреть глазами сердца, признавая, что каждый символ — это дверь, которая открывается только перед смирением.</p>

                <!-- DE -->
                <p class="de"><span class="drop-cap">D</span>as Heilige ist keine Frage der Religion, sondern der Ehrfurcht vor dem Geheimnis des Lebens. Wenn ein Mensch ein Symbol des Göttlichen zu einem banalen Schmuckstück degradiert oder es respektlos verwendet, begeht er einen spirituellen Selbstmord. Man kann nicht im Licht verweilen, während man die Lampe verdunkelt. Das Karma der Entweihung ist die innere Entleerung der eigenen Gnade.</p>
                <p class="de">Das Gesetz von Ursache und Wirkung sagt uns, dass wir durch die Verachtung des Heiligen den Schutz und Sinn des Lebens verlieren. Wer das Bild eines Heiligen zur Dekoration seiner Trägheit nutzt, wird in Zeiten der Not keinen Trost finden. Das Elend, das folgt, ist die Einsamkeit einer Seele, die ihre eigenen himmlischen Wurzeln gekappt hat.</p>
                <p class="de">Das „Vorher“ dieses Karmas ist ein Leben voller luxuriöser, aber geistig leerer Objekte. Das „Nachher“ ist die Wüste: eine Existenz, in der die Tragödie endlos scheint. Um dieses Karma zu heilen, müssen wir lernen, mit den Augen des Herzens zu sehen и anzuerkennen, dass jedes Symbol eine Tür ist, die sich nur vor der Demut öffnet.</p>

                <!-- FR -->
                <p class="fr"><span class="drop-cap">L</span>e sacré n'est pas une question de religion, mais de révérence devant le mystère de la vie. Quand un être humain rabaisse un symbole de la divinité au niveau d'un ornement banal ou l'utilise sans respect, il commet un acte de suicide spirituel. On ne peut habiter dans la lumière tout en obscurcissant la lampe qui la projette. Le karma de la profanation est le vidage interne de sa propre grâce.</p>
                <p class="fr">La loi de cause à effet nous dit qu'en traitant le sacré avec dédain, la vie perd son aura de protection et de sens. Celui qui utilise l'image d'un saint pour décorer son oisiveté ne trouvera aucun réconfort au moment du besoin. La misère qui suit est la solitude d'une âme qui a coupé ses propres racines célestes.</p>
                <p class="fr">Le « avant » de ce karma est une vie pleine d'objets luxueux mais vides d'esprit. Le « après » est le désert : une existence où la tragédie semble sans fin. Pour guérir, nous devons apprendre à regarder avec les yeux du cœur, en reconnaissant que chaque symbole est une porte qui ne s'ouvre que devant l'humilité.</p>

                <!-- JA -->
                <p class="ja"><span class="drop-cap">聖</span>なるものは宗教の問題ではなく、生命の神秘に対する畏敬の念の問題です。人間が神性の象徴を平凡な装飾品に貶めたり、不敬に使用したりするとき、それは精神的な自殺行為を犯していることになります。光を放つランプを暗くしながら、光の中に住むことはできません。冒涜のカルマは、自らの恩寵が内側から空虚になることです。</p>
                <p class="ja">因果応報の法則は、聖なるものを軽蔑することで、人生が保護と意味のオーラを失うことを教えています。聖人の像を怠惰の装飾に使う者は、真に助けが必要な時にどこにも慰めを見いだせません。その後に続く悲惨さは、自らの天の根を断ち切った魂の孤独です。</p>
                <p class="ja">このカルマの「前」は、豪華だが精神の抜けた物に囲まれた人生です。「後」は砂漠です。畏敬の念という羅針盤を失ったため、悲劇が終わりのないように思える存在の状態です。癒やすためには、心の目で見ること、そして象徴は謙虚さの前にのみ開かれる扉であることを認めることを学ばなければなりません。</p>

                <!-- PT -->
                <p class="pt"><span class="drop-cap">O</span> sagrado não é uma questão de religião, mas de reverência perante o mistério da vida. Quando um ser humano rebaixa um símbolo da divindade ao nível de um adorno banal ou o utiliza com falta de respeito, está a cometer um ato de suicídio espiritual. Não se pode habitar na luz enquanto se obscurece a lâmpada que a projeta. O karma da profanação é o esvaziamento interno da própria graça.</p>
                <p class="pt">A lei da causa e efeito diz-nos que, ao tratar o sagrado com desdém, a vida perde a sua aura de proteção e significado. Quem usa a imagem de um santo para decorar a sua desídia, não encontrará consolo nos momentos de necessidade. A miséria que se segue é a solidão de uma alma que cortou as suas próprias raízes celestiais.</p>
                <p class="pt">O "antes" deste karma é uma vida cheia de objetos luxuosos, mas vazios de espírito. O "depois" é o deserto: uma existência onde a tragédia parece sem fim. Para curar, devemos aprender a olhar com os olhos do coração, reconhecendo que cada símbolo é uma porta que só se abre perante a humildade.</p>

                <!-- VI -->
                <p class="vi"><span class="drop-cap">S</span>ự thiêng liêng không phải là vấn đề tôn giáo, mà là sự tôn kính trước sự huyền bí của sự sống. Khi một con người hạ thấp biểu tượng của thần thánh xuống mức trang trí tầm thường hoặc sử dụng thiếu tôn trọng, họ đang thực hiện một hành vi tự sát về tâm linh. Không ai có thể sống trong ánh sáng trong khi lại làm mờ ngọn đèn chiếu sáng nó. Nghiệp quả của sự xúc phạm là sự trống rỗng nội tâm của chính ân điển mình.</p>
                <p class="vi">Luật nhân quả cho thấy rằng bằng cách coi thường sự thiêng liêng, cuộc sống sẽ mất đi hào quang bảo vệ và ý nghĩa. Kẻ dùng hình ảnh thánh nhân để trang trí cho sự lười biếng của mình sẽ chẳng tìm thấy niềm an ủi lúc cần thiết. Sự khốn cùng theo sau là sự cô độc của một linh hồn đã tự cắt đứt gốc rễ thiên thượng của chính mình.</p>
                <p class="vi">Cái "trước" của nghiệp này là một cuộc sống đầy những vật phẩm xa hoa nhưng trống rỗng tâm linh. Cái "sau" là sa mạc: một sự tồn tại mà bi kịch dường như vô tận vì đã mất đi la bàn của sự tôn kính. Để chữa lành, chúng ta phải học cách nhìn bằng con mắt của trái tim, nhận ra rằng mỗi biểu tượng là một cánh cửa chỉ mở ra trước sự khiêm nhường.</p>
            </div>

            <!-- ═══ PARÁBOLA ═══ -->
            <div class="story-block parable-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">
                <h3 class="es" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">El Mercader y la Lámpara Eterna</h3>
                <h3 class="en" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">The Merchant and the Eternal Lamp</h3>
                <h3 class="it" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Il Mercante e la Lampada Eterna</h3>
                <h3 class="zh" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">商人与永恒之灯</h3>
                <h3 class="ar" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">التاجر والمصباح الأبدي</h3>
                <h3 class="ru" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Торговец и вечная лампа</h3>
                <h3 class="de" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Der Kaufmann und die ewige Lampe</h3>
                <h3 class="fr" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Le Marchand et la Lampe Éternelle</h3>
                <h3 class="ja" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">商人と永遠のランプ</h3>
                <h3 class="pt" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">O Mercador e a Lâmpada Eterna</h3>
                <h3 class="vi" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Thương Nhân Và Ngọn Đèn Vĩnh Cửu</h3>

                <!-- ES -->
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Había una vez un mercader llamado Silas que poseía una colección de estatuas sagradas de incalculable valor. Silas no era un hombre de fe; para él, los Budas de jade y los Cristos de oro eran solo trofeos que demostraban su éxito. En sus banquetes, Silas solía colocar sombreros ridículos sobre las cabezas de las estatuas o usarlas para sostener las copas de sus invitados, riendo mientras profanaba aquello que miles de personas veneraban con lágrimas en los ojos.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Un día, Silas adquirió una pequeña lámpara de aceite que, según se decía, procedía del altar de un santo olvidado. La lámpara emitía una luz dorada y suave que nunca se apagaba. Sin embargo, Silas, queriendo impresionar a una cortesana, decidió usar el aceite sagrado de la lámpara para perfumar su vino. En el instante en que el aceite tocó el cristal, la lámpara se rompió en mil pedazos y la luz se desvaneció, dejando la sala en una oscuridad absoluta y gélida.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">A partir de esa noche, la fortuna de Silas se desmoronó. Sus barcos se hundieron en mares tranquilos y sus amigos desaparecieron como el humo. Lo más trágico fue que Silas empezó a sentir un frío interno que nada podía calmar. Vagó por el mundo como un mendigo, con los pies sangrantes, buscando un templo donde refugiarse, pero cada vez que se acercaba a un altar, sentía que las imágenes le daban la espalda. No era odio divino; era que Silas había perdido la facultad de reconocer lo sagrado, y por lo tanto, el universo ya no podía ofrecerle su protección.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Silas murió en la soledad de un desierto, comprendiendo demasiado tarde que cuando se juega con lo eterno, es el propio tiempo lo que se nos escapa. Había tenido el cielo en sus manos y lo había usado para adornar su soberbia. Su Ikigai, su propósito olvidado, le susurró en el último aliento: "No se puede pedir luz cuando se ha disfrutado apagando el sol". Su historia quedó grabada en las arenas como un aviso de que el respeto no es una norma, sino la piel con la que el alma siente el amor de Dios.</p>

                <!-- EN -->
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Once there was a merchant named Silas who possessed a collection of sacred statues of incalculable value. Silas was not a man of faith; for him, the jade Buddhas and golden Christs were only trophies that proved his success. At his banquets, Silas used to place ridiculous hats on the heads of the statues or use them to hold his guests' glasses, laughing while desecrating that which thousands of people venerated with tears in their eyes.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">One day, Silas acquired a small oil lamp that was said to have come from the altar of a forgotten saint. The lamp emitted a soft, golden light that never went out. However, Silas, wanting to impress a courtesan, decided to use the sacred oil from the lamp to scent his wine. The moment the oil touched the glass, the lamp broke into a thousand pieces and the light faded, leaving the room in absolute and freezing darkness.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">From that night on, Silas's fortune crumbled. His ships sank in calm seas and his friends vanished like smoke. Most tragically, Silas began to feel an internal cold that nothing could soothe. He wandered the world as a beggar, with bleeding feet, seeking a temple where he could take refuge, but every time he approached an altar, he felt the images turned their backs on him. It was not divine hatred; it was that Silas had lost the faculty to recognize the sacred, and therefore, the universe could no longer offer him its protection.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Silas died in the loneliness of a desert, understanding too late that when one plays with the eternal, it is time itself that escapes us. He had held heaven in his hands and used it to adorn his pride. His Ikigai, his forgotten purpose, whispered to him in his last breath: "One cannot ask for light when one has enjoyed extinguishing the sun." His story remained engraved in the sands as a warning that respect is not a rule, but the skin with which the soul feels God's love.</p>

                <!-- IT -->
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">C'era una volta un mercante di nome Silas che possedeva statue sacre di inestimabile valore. Per lui erano solo trofei. Ai suoi banchetti, Silas metteva cappelli ridicoli sulle statue o le usava per reggere i bicchieri dei suoi ospiti, ridendo di ciò che gli altri veneravano.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Un giorno decise di usare l'olio sacro di una lampada eterna per profumare il suo vino. Nell'istante in cui l'olio toccò il vetro, la lampada si ruppe e la luce svanì, lasciando la sala in un'oscurità gelida. Da quella notte, la fortuna di Silas crollò.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vagò come un mendicante, cercando rifugio in un tempio, ma ogni volta le immagini sembravano dargli le spalle. Aveva perso la facoltà di riconoscere il sacro. Silas morì nel deserto, capendo troppo tardi che quando si gioca con l'eterno, è il tempo stesso a sfuggirci.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Il suo scopo gli sussurrò nell'ultimo respiro: "Non si può chiedere luce quando si è goduto a spegnere il sole". La sua storia insegna che il rispetto è la pelle con cui l'anima sente l'amore di Dio.</p>

                <!-- ZH -->
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">从前有一个叫西拉的商人，拥有一批价值连城的圣像。对他而言，这些只是炫耀成功的战利品。在宴会上，西拉常在圣像头上戴上滑稽的帽子，或用它们支撑客人的酒杯，嘲笑他人的虔诚。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">一天，他决定用永恒之灯里的圣油来熏香他的酒。油触碰到杯子的瞬间，灯碎成了千万片，光芒消失，房间陷入冰冷的黑暗。从那晚起，西拉的财富土崩瓦解。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">他像乞丐一样流浪，寻找寺庙避难，但每当他靠近祭坛，圣像仿佛都背过身去。他失去了辨识神圣的能力。西拉死在荒漠中，太晚才明白，当人玩弄永恒时，逃走的正是时间本身。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">他在弥留之际听到心声：“当你以熄灭太阳为乐时，就不能祈求光芒。”他的故事告诫世人，敬畏不是规则，而是灵魂感受神之爱的皮肤。</p>

                <!-- AR -->
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">كان يا مكان، كان هناك تاجر يدعى سيلاس يمتلك مجموعة من التماثيل المقدسة لا تقدر بثمن. بالنسبة له، لم تكن سوى كؤوس تثبت نجاحه. في مآدبه، كان سيلاس يضع قبعات مضحكة على رؤوس التماثيل، ضاحكاً بينما يدنس ما يقدسه الآخرون.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">ذات يوم، قرر استخدام الزيت المقدس من مصباح أبدي لتعطير خمره. في اللحظة التي لمس فيها الزيت الكأس، انكسر المصباح واختفى النور، تاركاً القاعة في ظلام دامس وبرد قارس. ومنذ تلك الليلة، انهارت ثروة سيلاس.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">هام كمتسول، باحثاً عن معبد، لكنه شعر أن الصور تدير ظهرها له. لقد فقد القدرة على التعرف على المقدس. مات سيلاس في الصحراء، مدركاً بعد فوات الأوان أنه عندما نلعب بالأبدي، فإن الوقت هو ما يهرب منا.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">همس له غرضه في أنفاسه الأخيرة: "لا يمكن للمرء أن يطلب النور عندما يستمتع بإطفاء الشمس". قصته باقية كتحذير بأن الاحترام هو الجلد الذي تشعر به الروح بمحبة الله.</p>

                <!-- RU -->
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Жил-был торговец по имени Сайлас, владевший коллекцией бесценных священных статуй. Для него они были лишь трофеями. На пирах Сайлас надевал на статуи шутовские колпаки или использовал их как подставки для кубков, смеясь над тем, что другие почитали со слезами на глазах.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Однажды он решил использовать священное масло из вечной лампады, чтобы ароматизировать вино. Как только масло коснулось бокала, лампа разлетелась на куски, и свет исчез, оставив зал в ледяной тьме. С той ночи удача Сайласа рухнула.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Он бродил как нищий, ища убежища в храмах, но всякий раз лики святых словно отворачивались от него. Он утратил способность узнавать священное. Сайлас умер в пустыне, слишком поздно поняв: когда играешь с вечностью, ускользает само время.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">«Нельзя просить света, если ты наслаждался, гася солнце», — прошептал ему голос в последний миг. Его история учит: почтение — это кожа, которой душа чувствует любовь Бога.</p>

                <!-- DE -->
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Es war einmal ein Kaufmann namens Silas, der wertvolle heilige Statuen besaß. Für ihn waren sie nur Trophäen. Bei seinen Banketten setzte Silas den Statuen lächerliche Hüte auf oder benutzte sie als Glashalter, während er über das lachte, was andere verehrten.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Eines Tages benutzte er das heilige Öl einer ewigen Lampe, um seinen Wein zu parfümieren. In dem Moment, als das Öl das Glas berührte, zerbrach die Lampe und das Licht erlosch in eisiger Dunkelheit. Von dieser Nacht an zerfiel Silas' Vermögen.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Er wanderte als Bettler umher, doch in jedem Tempel schienen sich die Heiligenbilder von ihm abzuwenden. Er hatte die Fähigkeit verloren, das Heilige zu erkennen. Silas starb in der Wüste und begriff zu spät: Wer mit dem Ewigen spielt, verliert die Zeit selbst.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">„Man kann nicht um Licht bitten, wenn man es genossen hat, die Sonne zu löschen“, flüsterte ihm sein Zweck im letzten Atemzug zu. Seine Geschichte lehrt, dass Respekt die Haut ist, mit der die Seele Gottes Liebe spürt.</p>

                <!-- FR -->
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Il était une fois un marchand nommé Silas qui possédait des statues sacrées de valeur inestimable. Pour lui, ce n'étaient que des trophées. Lors de ses banquets, Silas coiffait les statues de chapeaux ridicules ou les utilisait pour tenir les verres de ses invités, riant de ce que les autres vénéraient.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Un jour, il utilisa l'huile sacrée d'une lampe éternelle pour parfumer son vin. À l'instant où l'huile toucha le verre, la lampe se brisa et la lumière s'évanouit dans une obscurité glaciale. Dès cette nuit-là, la fortune de Silas s'effondra.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Il erra comme un mendiant, cherchant refuge dans un temple, mais chaque fois les images semblaient lui tourner le dos. Silas mourut dans le désert, comprenant trop tard que lorsqu'on joue avec l'éternel, c'est le temps lui-même qui nous échappe.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">« On ne peut demander la lumière quand on a pris plaisir à éteindre le soleil », lui murmura son but dans un dernier souffle. Son histoire enseigne que le respect est la peau avec laquelle l'âme ressent l'amour de Dieu.</p>

                <!-- JA -->
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">昔、サイラスという商人が、計り知れない価値のある聖像のコレクションを持っていました。彼にとって、それらは成功の証としてのトロフィーに過ぎませんでした。宴会の席で、サイラスは聖像の頭に滑稽な帽子を被せたり、客のグラスを持たせたりして、人々が涙を流して崇拝するものを嘲笑っていました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">ある日、彼は「永遠のランプ」の聖なる油を使ってワインに香りをつけようとしました。油がグラスに触れた瞬間、ランプは砕け散り、光は消え、部屋は冷たい闇に包まれました。その夜から、サイラスの富は崩れ去りました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">彼は物乞いとなって世界を彷徨い、寺院に救いを求めましたが、祭壇に近づくたびに、聖像たちは彼に背を向けているように感じました。彼は聖なるものを認識する能力を失ってしまったのです。サイラスは砂漠で孤独に死に、永遠なるものを弄ぶとき、逃げていくのは時間そのものであることを悟りました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">「太陽を消すことを楽しんでいた者が、光を求めることはできない」と、最期の息の中で彼の使命が囁きました。彼の物語は、畏敬の念こそが魂が神の愛を感じるための皮膚であることを教えています。</p>

                <!-- PT -->
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Era uma vez un mercador chamado Silas que possuía estátuas sagradas de valor incalculável. Para ele, eram apenas troféus. Nos seus banquetes, Silas colocava chapéus ridículos nas estátuas ou usava-as para segurar os copos dos convidados, rindo daquilo que outros veneravam com lágrimas.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Um dia usou o óleo sagrado de uma lâmpada eterna para perfumar o seu vinho. No instante em que o óleo tocou o vidro, a lâmpada quebrou-se e a luz desapareceu numa escuridão gélida. A partir dessa noite, a fortuna de Silas desmoronou.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vagou como um mendigo, procurando refúgio num templo, mas as imagens pareciam dar-lhe as costas. Tinha perdido a faculdade de reconhecer o sagrado. Silas morreu no deserto, compreendendo tarde demais que quando se joga com o eterno, é o próprio tempo que nos escapa.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">"Não se pode pedir luz quando se desfrutou a apagar o sol", sussurrou-lhe o seu propósito no último suspiro. A sua história ensina que o respeito é a pele com que a alma sente o amor de Deus.</p>

                <!-- VI -->
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Ngày xửa ngày xưa, có một thương nhân tên là Silas sở hữu một bộ sưu tập các bức tượng thánh vô giá. Đối với ông, chúng chỉ là những chiến lợi phẩm thể hiện sự thành đạt. Trong các bữa tiệc, Silas thường đặt những chiếc mũ nực cười lên đầu các bức tượng hoặc dùng chúng để đỡ ly rượu của thực khách, cười nhạo những gì mà hàng ngàn người tôn kính.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Một ngày nọ, ông quyết định dùng dầu thánh từ một ngọn đèn vĩnh cửu để ướp hương cho rượu của mình. Ngay khoảnh khắc dầu chạm vào ly, ngọn đèn vỡ tan thành ngàn mảnh và ánh sáng biến mất, để lại căn phòng trong bóng tối băng giá. Từ đêm đó, vận may của Silas sụp đổ.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Ông lang thang như một kẻ ăn xin, tìm kiếm một ngôi đền để nương náu, nhưng mỗi khi ông đến gần bệ thờ, ông cảm thấy các bức tượng như quay lưng lại với mình. Silas chết trong sự cô độc giữa sa mạc, hiểu ra quá muộn rằng khi người ta đùa giỡn với những điều vĩnh cửu, thì chính thời gian sẽ vuột mất.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Lẽ sống đã thì thầm với ông trong hơi thở cuối cùng: "Không thể cầu xin ánh sáng khi người ta đã từng thích thú với việc dập tắt mặt trời". Câu chuyện của ông là một lời cảnh báo rằng sự tôn kính chính là làn da để linh hồn cảm nhận được tình yêu của Thiên Chúa.</p>
            </div>

            <!-- ═══ ART ═══ -->
            <div class="final-art fade-in" style="text-align: center; margin-top: 4rem; margin-bottom: 2rem;">
                <img src="assets/art.jpg" alt="Obra de Arte Karma LXI" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            </div>

            <!-- ═══ MORAL ═══ -->
            <div class="moral fade-in">
                <span class="es">Quien trata lo sagrado como un adorno, termina por encontrar que su propia vida carece de cimiento; la reverencia es el alimento del alma.</span>
                <span class="en">He who treats the sacred as an ornament ends up finding that his own life lacks a foundation; reverence is the food of the soul.</span>
                <span class="it">Chi tratta il sacro come un ornamento, finisce per trovare la propria vita priva di fondamenta; la riverenza è l'alimento dell'anima.</span>
                <span class="zh">将神圣视为装饰的人，最终会发现自己的生活缺乏根基；敬畏是灵魂的食粮。</span>
                <span class="ar">من يعامل المقدس كزينة، ينتهي به الأمر ليجد أن حياته تفتقر إلى أساس؛ التوقير هو غذاء الروح.</span>
                <span class="ru">Тот, кто относится к священному как к украшению, в итоге обнаруживает, что его собственной жизни не хватает фундамента; почтение — это пища для души.</span>
                <span class="de">Wer das Heilige wie einen Schmuck behandelt, muss feststellen, dass seinem eigenen Leben das Fundament fehlt; Ehrfurcht ist die Nahrung der Seele.</span>
                <span class="fr">Celui qui traite le sacré comme un ornement finit par découvrir que sa propre vie manque de fondement ; la révérence est l'aliment de l'âme.</span>
                <span class="ja">聖なるものを装飾品として扱う者は、自らの人生に基盤がないことに気づくことになります。畏敬の念は魂の糧なのです。</span>
                <span class="pt">Quem trata o sagrado como um adorno, acaba por descobrir que a sua própria vida carece de alicerces; a reverência é o alimento da alma.</span>
                <span class="vi">Kẻ coi thường sự thiêng liêng như một vật trang trí, rốt cuộc sẽ thấy cuộc đời mình thiếu đi nền tảng; sự tôn kính chính là thức ăn của linh hồn.</span>
            </div>

            <center class="fade-in" style="margin-top: 4rem;">
                <img src="assets/hero.jpg" alt="Karma LXI Full" style="max-width: 600px; width: 100%; border-radius: 8px; border: 1px solid rgba(197,160,89,0.3); box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
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
                        <strong>🇻🇳 Tiếng Việt:</strong><br>Nhân: Dùng Tôn ảnh, Thánh tượng để trang trí, trang sức.<br>Quả: Cuộc đời rơi vào khốn cùng bi đát.
                    </p>
                    <p style="color: #ddd; margin-bottom: 1.5rem;"><strong>🇬🇧 English:</strong><br>Cause: Using images of saints for adornment.<br>Effect: Brings a very miserable life.</p>
                    <p class="es" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197,160,89,0.1); padding: 1rem; border-left: 3px solid var(--gold);"><strong>Traducción Recreada:</strong><br>Causa: Utilizar imágenes o estatuas sagradas con fines puramente decorativos, frívolos o como adornos personales sin el debido respeto.<br>Efecto: La vida se sumerge progresivamente en una miseria trágica y una profunda infelicidad espiritual.</p>
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

with open("/Users/fjbanezares/libro del karma/61_respeto_sagrado_miseria/web/index.html", "w") as f:
    f.write(html_content)

print("Chapter 61 HTML successfully updated with all 11 languages.")
