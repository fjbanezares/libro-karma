
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
                    <span class="pt">"Não é a pedra que sangra quando a tratas con desdém, mas o fio de ouro que unia o teu espírito ao céu."</span>
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
                <p class="it"><span class="drop-cap">I</span>l sacro non è una questione di religione, ma di riverenza davanti al mistero della vita. Quando un essere umano prende un simbolo della divinità — un'immagine che rappresenta l'aspirazione più alta alla pace e alla saggezza — e lo abbassa al livello di un banale ornamento o, peggio ancora, lo usa con mancanza di rispetto in ambienti di vizio o frivolezza, sta commettendo un atto di suicidio spirituale. Non si può abitare nella luce mentre si oscura la lampada che la proietta. Il karma della profanazione non è una punizione esterna, ma lo svuotamento interno della propria grazia.</p>
                <p class="it">La legge di causa ed effetto ci dice che trattando il sacro con disprezzo, stiamo dichiarando che non c'è nulla oltre la nostra comodità immediata. Tale dichiarazione diventa la nostra realtà: la vita perde la sua "aura" di protezione e significato. Chi usa l'immagine di un santo per decorare la propria accidia, scoprirà presto che nei suoi momenti di vera necessità non troverà conforto da nessuna parte. La bellezza e la pace fuggono da colui che non sa onorare la loro fonte. La miseria che segue questo atto è la solitudine di un'anima che ha reciso le proprie radici celesti.</p>
                <p class="it">Il "prima" di questo karma è una vita piena di oggetti lussuosi ma vuoti di spirito, dove il sacro è esposto ma non vissuto. Il "dopo" è il deserto: un'esistenza dove la tragedia sembra non avere fine perché abbiamo perso la bussola della riverenza. Per guarire questo karma, dobbiamo imparare a guardare con gli occhi del cuore, riconoscendo che ogni simbolo è una porta che si apre solo davanti all'umiltà. Solo colui che sa prostrarsi davanti a ciò che è più grande di se stesso recupera la dignità di stare in piedi davanti al mondo.</p>

                <!-- ZH -->
                <p class="zh"><span class="drop-cap">神</span>圣并非宗教问题，而是对生命奥秘的敬畏。当人类将神圣的象征——代表着对和平与智慧最高追求的图像——贬低为平庸的装饰，或者更糟糕的是，在恶习或轻浮的环境中无礼地使用它时，便是在进行一场精神上的自杀。当人们熄灭投射光芒的灯火时，便无法居住在光中。亵渎的业力并非外在的惩罚，而是自身恩典的内在枯竭。</p>
                <p class="zh">因果定律告诉我们，当我们轻蔑地对待神圣事物时，我们是在宣告除了眼前的舒适之外别无他物。这一宣告变成了我们的现实：生命失去了其保护和意义的“光环”。将圣像用于装点其懒散生活的人，很快就会发现在其真正需要帮助的时刻，随处都找不到慰藉。美与和平会逃离那些不懂得尊崇其源头的人。这一行为随之而来的痛苦，是切断了自身上天根基后的灵魂孤独。</p>
                <p class="zh">这种业力的“前因”是充斥着奢华却精神空虚的对象的生活，神圣虽被展示却未被践行。而“后果”则是荒漠：由于失去了敬畏的指南针，悲剧似乎永无止境。为了治愈这种业力，我们必须学会用心灵之眼观察，承认每个象征都是一扇门，唯有在谦卑面前才会开启。唯有懂得在比自己更伟大的事物面前俯伏的人，才能重新获得顶天立地于世间的尊严。</p>

                <!-- AR -->
                <p class="ar"><span class="drop-cap">ا</span>لمقدس ليس مسألة دين، بل هو توقير أمام سر الحياة. عندما يأخذ الإنسان رمزاً للإلهية - صورة تمثل أسمى تطلعات السلام والحكمة - وينزلها إلى مستوى الزينة التافهة، أو والأسوأ من ذلك، يستخدمها باستهتار في بيئات الرذيلة أو العبث، فإنه يرتكب فعلاً من أفعال الانتحار الروحي. لا يمكن للمرء أن يسكن في النور بينما يظلم المصباح الذي يشعه. كارما التدنيس ليست عقاباً خارجياً، بل هي إفراغ داخلي للنعمة الشخصية.</p>
                <p class="ar">يخبرنا قانون السبب والنتيجة أننا عندما نعامل المقدس بازدراء، فإننا نعلن أنه لا يوجد شيء وراء راحتنا المباشرة. ويصبح هذا الإعلان هو واقعنا: تفقد الحياة "هالتها" من الحماية والمعنى. من يستخدم صورة قديس لتزيين تكاسله، سيكتشف قريباً أنه في لحظات حاجته الحقيقية، لن يجد عزاءً في أي مكان. يهرب الجمال والسلام ممن لا يعرف كيف يكرم مصدرهما. البؤس الذي يتبع هذا الفعل هو وحدة الروح التي قطعت جذورها السماوية.</p>
                <p class="ar">"ما قبل" هذه الكارما هي حياة مليئة بالأشياء الفاخرة ولكنها خالية من الروح، حيث يُعرض المقدس ولكن لا يُعاش. أما "ما بعد" فهو الصحراء: وجود تبدو فيه المأساة بلا نهاية لأننا فقدنا بوصلة التوقير. لشفاء هذه الكارما، يجب أن نتعلم النظر بعيون القلب، مدركين أن كل رمز هو باب لا يُفتح إلا أمام التواضع. فقط من يعرف كيف يسجد أمام ما هو أعظم من نفسه، يستعيد كرامة الوقوف منتصباً أمام العالم.</p>

                <!-- RU -->
                <p class="ru"><span class="drop-cap">С</span>вященное — это не вопрос религии, а вопрос почтения перед тайной жизни. Когда человек берет символ божественности — образ, представляющий высшее стремление к миру и мудрости — и низводит его до уровня банального украшения или, что еще хуже, использует его неуважительно в обстановке порока или легкомыслия, он совершает акт духовного самоубийства. Нельзя пребывать в свете, гася лампу, которая его излучает. Карма осквернения — это не внешнее наказание, а внутреннее опустошение собственной благодати.</p>
                <p class="ru">Закон причины и следствия говорит нам, что, относясь к священному с пренебрежением, мы заявляем, что нет ничего за пределами нашего сиюминутного комфорта. Это заявление становится нашей реальностью: жизнь теряет свою «ауру» защиты и смысла. Тот, кто использует святой образ для украшения своего безделья, вскоре обнаружит, что в минуты истинной нужды он нигде не находит утешения. Красота и мир бегут от того, кто не умеет чтить их источник. Страдание, следующее за этим актом — одиночество души, обрубившей свои собственные небесные корни.</p>
                <p class="ru">Состояние «до» этой кармы — жизнь, полная роскошных, но пустых вещей, где священное выставляется напоказ, но не проживается. «После» — это пустыня: существование, в котором трагедия кажется бесконечной, потому что мы потеряли компас почтения. Чтобы исцелить эту карму, мы должны научиться смотреть глазами сердца, признавая, что каждый символ — это дверь, которая открывается только перед смирением. Только тот, кто умеет преклониться перед тем, что выше его самого, обретает достоинство стоять во весь рост перед миром.</p>

                <!-- DE -->
                <p class="de"><span class="drop-cap">D</span>as Heilige ist keine Frage der Religion, sondern der Ehrfurcht vor dem Geheimnis des Lebens. Wenn ein Mensch ein Symbol des Göttlichen nimmt – ein Bild, das das höchste Streben nach Frieden und Weisheit darstellt – und es zum banalen Schmuckstück degradiert oder, schlimmer noch, es respektlos in Umgebungen des Lasters oder der Leichtfertigkeit verwendet, begeht er einen spirituellen Selbstmord. Man kann nicht im Licht verweilen, während man die Lampe verdunkelt, die es ausstrahlt. Das Karma der Entweihung ist keine äußere Strafe, sondern die innere Entleerung der eigenen Gnade.</p>
                <p class="de">Das Gesetz von Ursache und Wirkung sagt uns, dass wir durch die Verachtung des Heiligen erklären, dass es nichts jenseits unserer unmittelbaren Bequemlichkeit gibt. Diese Erklärung wird zu unserer Realität: Das Leben verliert seine „Aura“ des Schutzes und der Bedeutung. Wer das Bild eines Heiligen zur Dekoration seiner Trägheit nutzt, wird bald feststellen, dass er in Momenten wahrer Not nirgendwo Trost findet. Schönheit und Frieden fliehen vor demjenigen, der ihre Quelle nicht zu ehren weiß. Das Elend, das diesem Akt folgt, ist die Einsamkeit einer Seele, die ihre eigenen himmlischen Wurzeln gekappt hat.</p>
                <p class="de">Das „Vorher“ dieses Karmas ist ein Leben voller luxuriöser, aber geistig leerer Objekte, in dem das Heilige zwar ausgestellt, aber nicht gelebt wird. Das „Nachher“ ist die Wüste: eine Existenz, in der die Tragödie endlos scheint, weil wir den Kompass der Ehrfurcht verloren haben. Um dieses Karma zu heilen, müssen wir lernen, mit den Augen des Herzens zu sehen und zu erkennen, dass jedes Symbol eine Tür ist, die sich nur vor der Demut öffnet. Nur wer sich vor dem beugen kann, was größer ist als er selbst, gewinnt die Würde zurück, aufrecht vor der Welt zu stehen.</p>

                <!-- FR -->
                <p class="fr"><span class="drop-cap">L</span>e sacré n'est pas une question de religion, mais de révérence devant le mystère de la vie. Quand un être humain prend un symbole de la divinité — une image qui représente l'aspiration la plus haute à la paix et à la sagesse — et le rabaisse au niveau d'un ornement banal ou, pire encore, l'utilise sans respect dans des environnements de vice ou de frivolité, il commet un acte de suicide spirituel. On ne peut habiter dans la lumière tout en obscurcissant la lampe qui la projette. Le karma de la profanation n'est pas une punition externe, mais le vidage interne de sa propre grâce.</p>
                <p class="fr">La loi de cause à effet nous dit qu'en traitant le sacré avec dédain, nous déclarons qu'il n'y a rien au-delà de notre confort immédiat. Cette déclaration devient notre réalité : la vie perd son « aura » de protection et de sens. Celui qui utilise l'image d'un saint pour décorer son oisiveté découvrira bientôt qu'au moment de ses besoins réels, il ne trouvera de réconfort nulle part. La beauté et la paix fuient celui qui ne sait pas honorer leur source. La misère qui suit cet acte est la solitude d'une âme qui a coupé ses propres racines célestes.</p>
                <p class="fr">Le « avant » de ce karma est une vie pleine d'objets luxueux mais vides d'esprit, où le sacré est exposé mais pas vécu. Le « après » est le désert : une existence où la tragédie semble sans fin parce que nous avons perdu la boussole de la révérence. Pour guérir ce karma, nous devons apprendre à regarder avec les yeux du cœur, en reconnaissant que chaque symbole est une porte qui ne s'ouvre que devant l'humilité. Seul celui qui sait se prosterner devant ce qui est plus grand que lui-même récupère la dignité de se tenir debout face au monde.</p>

                <!-- JA -->
                <p class="ja"><span class="drop-cap">聖</span>なるものは宗教の問題ではなく、生命の神秘に対する畏敬の念の問題です。人間が神性の象徴——平和と知恵の最高の憧れを表す像——を手に取り、それを平凡な装飾品に貶めたり、さらに悪いことに、悪徳や軽薄な環境で不敬に使用したりするとき、その人は精神的な自殺行為を犯していることになります。光を放つランプを暗くしながら、光の中に住むことはできません。冒涜のカルマは外的な罰ではなく、自らの恩寵が内側から空虚になることです。</p>
                <p class="ja">因果応報の法則は、聖なるものを軽蔑をもって扱うことで、自らの目先の快適さ以外には何もないと宣言していることを教えています。その宣言が私たちの現実となります。人生は保護と意味の「オーラ」を失います。聖人の像を怠惰の装飾に使う者は、真に助けが必要な時に、どこにも慰めを見いだせないことに気づくでしょう。美と平和は、その源を敬うことを知らない者から逃げ去ります。この行為の後に続く悲惨さは、自らの天の根を断ち切った魂の孤独です。</p>
                <p class="ja">このカルマの「前」は、豪華だが精神の抜けた物に囲まれた人生であり、聖なるものは展示されていても、生かされてはいません。「後」は砂漠です。畏敬の念という羅針盤を失ったため、悲劇が終わりのないように思える存在の状態です。このカルマを癒やすためには、心の目で見ること、そしてすべての象徴は謙虚さの前にのみ開かれる扉であることを認めることを学ばなければなりません。自分よりも偉大なものに対してひれ伏すことを知る者だけが、世界の前に堂々と立つ尊厳を取り戻すのです。</p>

                <!-- PT -->
                <p class="pt"><span class="drop-cap">O</span> sagrado não é uma questão de religião, mas de reverência perante o misterio da vida. Quando um ser humano toma um símbolo da divindade — uma imagem que representa a aspiração mais alta de paz e sabedoria — e a rebaixa ao nível de um adorno banal ou, pior ainda, a utiliza com falta de respeito em ambientes de vício ou frivolidade, está a cometer um ato de suicídio espiritual. Não se pode habitar na luz enquanto se obscurece a lâmpada que a projeta. O karma da profanação não é um castigo externo, mas o esvaziamento interno da própria graça.</p>
                <p class="pt">A lei da causa e efeito diz-nos que ao tratar o sagrado com desdém, estamos a declarar que não há nada além do nosso conforto imediato. Essa declaração torna-se a nossa realidade: a vida perde a sua "aura" de proteção e significado. Quem usa a imagem de um santo para decorar a sua desídia, cedo descobrirá que nos seus momentos de verdadeira necessidade, não encontra consolo em parte alguma. A beleza e a paz fogem daquele que não sabe honrar a sua fonte. A miséria que se segue a este ato é a solidão de uma alma que cortou as suas próprias raízes celestiais.</p>
                <p class="pt">O "antes" deste karma é uma vida cheia de objetos luxuosos mas vazios de espírito, onde o sagrado é exibido mas não vivido. O "depois" é o deserto: uma existência onde a tragédia parece não ter fim porque perdemos a bússola da reverência. Para curar este karma, devemos aprender a olhar com os olhos do coração, reconhecendo que cada símbolo é uma porta que só se abre perante a humildade. Só aquele que sabe prostrar-se perante o que é maior do que ele mesmo, recupera a dignidade de estar de pé perante o mundo.</p>

                <!-- VI -->
                <p class="vi"><span class="drop-cap">S</span>ự thiêng liêng không phải là vấn đề tôn giáo, mà là sự tôn kính trước sự huyền bí của sự sống. Khi một con người cầm lấy một biểu tượng của thần thánh — một hình ảnh đại diện cho khát vọng cao nhất về hòa bình và trí tuệ — và hạ thấp nó xuống mức trang trí tầm thường hoặc tệ hơn nữa, sử dụng nó một cách thiếu tôn trọng trong môi trường sa đọa hoặc phù phiếm, họ đang thực hiện một hành vi tự sát về tâm linh. Không ai có thể sống trong ánh sáng trong khi lại làm mờ ngọn đèn chiếu sáng nó. Nghiệp quả của sự xúc phạm không phải là một hình phạt bên ngoài, mà là sự trống rỗng nội tâm của chính ân điển mình.</p>
                <p class="vi">Luật nhân quả cho thấy rằng bằng cách coi thường sự thiêng liêng, chúng ta đang tuyên bố rằng không có gì ngoài sự thoải mái tức thời của mình. Tuyên bố đó trở thành thực tế của chúng ta: cuộc sống mất đi "hào quang" bảo vệ và ý nghĩa. Kẻ dùng hình ảnh thánh nhân để trang trí cho sự lười biếng của mình sẽ sớm nhận ra rằng trong những lúc thực sự cần thiết, hắn sẽ chẳng tìm thấy niềm an ủi ở bất cứ đâu. Vẻ đẹp và sự bình an sẽ chạy trốn khỏi kẻ không biết tôn thờ nguồn gốc của chúng. Sự khốn cùng theo sau hành động này là sự cô độc của một linh hồn đã tự cắt đứt gốc rễ thiên thượng của chính mình.</p>
                <p class="vi">Cái "trước" của nghiệp này là một cuộc sống đầy những vật phẩm xa hoa nhưng trống rỗng tâm linh, nơi sự thiêng liêng được trưng bày nhưng không được sống. Cái "sau" là sa mạc: một sự tồn tại mà bi kịch dường như vô tận vì chúng ta đã mất đi la bàn của sự tôn kính. Để chữa lành nghiệp này, chúng ta phải học cách nhìn bằng con mắt của trái tim, nhận ra rằng mỗi biểu tượng là một cánh cửa chỉ mở ra trước sự khiêm nhường. Chỉ có kẻ biết cúi đầu trước những gì vĩ đại hơn chính mình mới lấy lại được phẩm giá để đứng vững trước thế gian.</p>
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
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">C'era una volta un mercante di nome Silas che possedeva una collezione di statue sacre di incalcolabile valore. Silas non era un uomo di fede; per lui, i Buddha di giada e i Cristi d'oro erano solo trofei che dimostravano il suo successo. Nei suoi banchetti, Silas era solito mettere cappelli ridicoli sulle teste delle statue o usarle per reggere i calici dei suoi ospiti, ridendo mentre profanava ciò che migliaia di persone veneravano con le lacrime agli occhi.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Un giorno Silas acquistò una piccola lampada a olio che, si diceva, provenisse dall'altare di un santo dimenticato. La lampada emetteva una luce dorata e soffusa che non si spegneva mai. Tuttavia Silas, volendo impressionare una cortigiana, decise di usare l'olio sacro della lampada per profumare il suo vino. Nell'istante in cui l'olio toccò il vetro, la lampada si ruppe in mille pezzi e la luce svanì, lasciando la sala in un'oscurità assoluta e gelida.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">A partire da quella notte, la fortuna di Silas andò in pezzi. Le sue navi affondarono in mari calmi e i suoi amici scomparvero come fumo. La cosa più tragica fu che Silas iniziò a sentire un freddo interno che nulla poteva calmare. Vagò per il mondo come un mendicante, con i piedi sanguinanti, cercando un tempio dove rifugiarsi, ma ogni volta che si avvicinava a un altare, sentiva che le immagini gli voltavano le spalle. Non era odio divino; era che Silas aveva perso la facoltà di riconoscere il sacro e, pertanto, l'universo non poteva più offrirgli la sua protezione.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Silas morì nella solitudine di un deserto, comprendendo troppo tardi che quando si gioca con l'eterno è il tempo stesso che ci sfugge. Aveva avuto il cielo nelle sue mani e lo aveva usato per adornare la sua superbia. Il suo Ikigai, il suo scopo dimenticato, gli sussurrò nell'ultimo respiro: "Non si può chiedere luce quando si è goduto a spegnere il sole". La sua storia rimase incisa nelle sabbie come avvertimento che il rispetto non è una norma, ma la pelle con cui l'anima sente l'amore di Dio.</p>

                <!-- ZH -->
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">从前有一个叫西拉（Silas）的商人，拥有一批价值连城的圣像收藏。西拉并不是一个虔诚的人；对他来说，翡翠佛像和黄金基督像只是证明他成功的奖杯。在宴会上，西拉经常在圣像头上戴上滑稽的帽子，或用它们来支撑客人的酒杯，嘲笑着亵渎那些成千上万的人流泪膜拜的神圣之物。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">一天，西拉得到了一盏小油灯，据说这盏灯来自一位被遗忘的圣人的祭坛。油灯发出柔和的金色光芒，永不熄灭。然而，西拉为了打动一位名妓，决定使用灯里的圣油来熏香他的美酒。在油触碰到玻璃杯的瞬间，油灯碎成了千万片，光芒消失了，房间陷入了绝对而冰冷的黑暗中。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">从那天晚上起，西拉的财富土崩瓦解。他的船只在平静的海面上沉没，他的朋友们像烟雾一样消失了。最悲惨的是，西拉开始感到一种无法平复的内心寒冷。他像乞丐一样流浪世界，双脚流着血，寻找可以避难的寺庙，但每当他靠近祭坛时，他都感觉到圣像们背对着他。这并非神圣的恨；而是西拉失去了辨识神圣的能力，因此，宇宙再也无法为他提供保护。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">西拉在荒漠的孤独中死去，太晚才明白，当人玩弄永恒时，逃走的正是时间本身。他曾将上天握在手中，却用它来点缀自己的傲慢。他那被遗忘的使命——伊基盖（Ikigai），在弥留之际对他耳语道：“当一个人以熄灭太阳为乐时，就不能祈求光芒。”他的故事被刻在沙中，作为一种告诫：敬畏不是一种规则，而是灵魂感受神之爱的皮肤。</p>

                <!-- AR -->
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">كان يا مكان، كان هناك تاجر يدعى سيلاس يمتلك مجموعة من التماثيل المقدسة التي لا تقدر بثمن. لم يكن سيلاس رجلاً مؤمناً؛ فبالنسبة له، لم تكن تماثيل بوذا المصنوعة من اليشم وتماثيل المسيح الذهبية سوى كؤوس تثبت نجاحه. في مآدبه، اعتاد سيلاس وضع قبعات مضحكة على رؤوس التماثيل أو استخدامها لحمل كؤوس ضيوفه، ضاحكاً بينما يدنس ما كان آلاف الناس يقدسونه بدموع في أعينهم.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">ذات يوم، حصل سيلاس على مصباح زيت صغير، قيل إنه جاء من مذبح قديس منسي. كان المصباح ينبعث منه نور ذهبي ناعم لا ينطفئ أبداً. ومع ذلك، أراد سيلاس إبهار إحدى الغانيات، فقرر استخدام الزيت المقدس من المصباح لتعطير خمره. في اللحظة التي لمس فيها الزيت الكأس، انكسر المصباح إلى ألف قطعة وتلاشى النور، تاركاً القاعة في ظلام دامس وبرد قارس.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">منذ تلك الليلة، انهارت ثروة سيلاس. غرقت سفنه في بحار هادئة، واختفى أصدقاؤه كالدخان. والأكثر مأساوية هو أن سيلاس بدأ يشعر ببرد داخلي لا يمكن لأي شيء تهدئته. هام في العالم كمتسول، قدماه تنزفان، باحثاً عن معبد يلجأ إليه، لكن في كل مرة كان يقترب فيها من مذبح، كان يشعر أن الصور تدير ظهرها له. لم يكن ذلك كرهاً إلهياً؛ بل لأن سيلاس قد فقد القدرة على التعرف على المقدس، وبالتالي، لم يعد الكون قادراً على تقديم حمايته له.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">مات سيلاس في وحدة الصحراء، مدركاً بعد فوات الأوان أنه عندما يتم اللعب بالأبدي، فإن الوقت نفسه هو ما يهرب منا. كان قد أمسك بالسماء بين يديه واستخدمها لتزيين كبريائه. همس له الـ "إيكيغاي" الخاص به، غرضه المنسي، في أنفاسه الأخيرة: "لا يمكن للمرء أن يطلب النور عندما يستمتع بإطفاء الشمس". ظلت قصته محفورة في الرمال كتحذير بأن الاحترام ليس قاعدة، بل هو الجلد الذي تشعر به الروح بمحبة الله.</p>

                <!-- RU -->
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Жил-был торговец по имени Сайлас, владевший коллекцией бесценных священных статуй. Сайлас не был верующим человеком; для него нефритовые Будды и золотые распятия были лишь трофеями, подтверждающими его успех. На своих пирах Сайлас надевал на головы статуй шутовские колпаки или использовал их как подставки для кубков своих гостей, смеясь над тем, что тысячи людей почитали со слезами на глазах.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Однажды Сайлас приобрел маленькую масляную лампаду, которая, как говорили, когда-то стояла на алтаре забытого святого. Лампада излучала мягкий золотистый свет, который никогда не гас. Однако Сайлас, желая произвести впечатление на куртизанку, решил использовать священное масло из лампады, чтобы ароматизировать свое вино. В тот миг, когда масло коснулось бокала, лампада разлетелась на тысячу осколков, и свет исчез, оставив зал в абсолютной и ледяной тьме.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">С той ночи удача Сайласа рухнула. Его корабли тонули в спокойном море, а друзья исчезали, словно дым. Самым трагичным было то, что Сайлас начал чувствовать внутренний холод, который ничто не могло унять. Он бродил по миру как нищий, с окровавленными ногами, ища храм, где можно было бы укрыться, но всякий раз, когда он приближался к алтарю, он чувствовал, что лики святых отворачиваются от него. Это не была божественная ненависть; дело было в том, что Сайлас утратил способность узнавать священное, и поэтому Вселенная больше не могла предложить ему свою защиту.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Сайлас умер в одиночестве в пустыне, слишком поздно поняв: когда играешь с вечностью, ускользает само время. В его руках было небо, а он использовал его для украшения своей гордыни. Его Икигай, его забытая цель, прошептал ему в последнем вздохе: «Нельзя просить света, если ты наслаждался, гася солнце». Его история осталась запечатленной в песках как предупреждение о том, что почтение — это не норма, а кожа, которой душа чувствует любовь Бога.</p>

                <!-- DE -->
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Es war einmal ein Kaufmann namens Silas, der eine Sammlung wertvoller heiliger Statuen besaß. Silas war kein Mann des Glaubens; für ihn waren die Jade-Buddhas und goldenen Christusstatuen nur Trophäen, die seinen Erfolg bewiesen. Bei seinen Banketten setzte Silas den Statuen lächerliche Hüte auf oder benutzte sie als Halter für die Kelche seiner Gäste, während er über das lachte, was Tausende von Menschen mit Tränen in den Augen verehrten.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Eines Tages erwarb Silas eine kleine Öllampe, die angeblich vom Altar eines vergessenen Heiligen stammte. Die Lampe verströmte ein sanftes, goldenes Licht, das niemals erlosch. Doch Silas wollte eine Kurtisane beeindrucken und beschloss, das heilige Öl der Lampe zu verwenden, um seinen Wein zu parfümieren. In dem Moment, als das Öl das Glas berührte, zerbrach die Lampe in tausend Stücke und das Licht erlosch, was den Saal in absolute und eisige Dunkelheit tauchte.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Von dieser Nacht an zerfiel Silas' Vermögen. Seine Schiffe sanken in ruhiger See und seine Freunde verschwanden wie Rauch. Am tragischsten war, dass Silas anfing, eine innere Kälte zu spüren, die durch nichts gelindert werden konnte. Er wanderte als Bettler durch die Welt, mit blutenden Füßen, auf der Suche nach einem Tempel, in dem er Zuflucht finden konnte, doch jedes Mal, wenn er sich einem Altar näherte, spürte er, dass die Heiligenbilder ihm den Rücken kehrten. Es war kein göttlicher Hass; es war so, dass Silas die Fähigkeit verloren hatte, das Heilige zu erkennen, und daher konnte das Universum ihm seinen Schutz nicht mehr anbieten.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Silas starb in der Einsamkeit einer Wüste und begriff zu spät, dass man Zeit selbst verliert, wenn man mit dem Ewigen spielt. Er hatte den Himmel in seinen Händen gehalten und ihn benutzt, um seinen Hochmut zu schmücken. Sein Ikigai, sein vergessenes Lebensziel, flüsterte ihm im letzten Atemzug zu: „Man kann nicht um Licht bitten, wenn man es genossen hat, die Sonne zu löschen.“ Seine Geschichte blieb im Sand eingraviert als Mahnung, dass Ehrfurcht keine Norm ist, sondern die Haut, mit der die Seele Gottes Liebe spürt.</p>

                <!-- FR -->
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Il était une fois un marchand nommé Silas qui possédait une collection de statues sacrées d'une valeur inestimable. Silas n'était pas un homme de foi ; pour lui, les Bouddhas de jade et les Christs d'or n'étaient que des trophées qui démontraient sa réussite. Lors de ses banquets, Silas avait l'habitude de coiffer les statues de chapeaux ridicules ou de les utiliser pour tenir les verres de ses invités, riant tout en profanant ce que des milliers de personnes vénéraient avec des larmes dans les yeux.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Un jour, Silas acquit une petite lampe à huile qui, disait-on, provenait de l'autel d'un saint oublié. La lampe émettait une lumière dorée et douce qui ne s'éteignait jamais. Cependant, Silas, voulant impressionner une courtisane, décida d'utiliser l'huile sacrée de la lampe pour parfumer son vin. À l'instant où l'huile toucha le verre, la lampe se brisa en mille morceaux et la lumière s'évanouit, laissant la salle dans une obscurité absolue et glaciale.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">À partir de cette nuit-là, la fortune de Silas s'effondra. Ses navires coulèrent dans des mers calmes et ses amis disparurent comme de la fumée. Le plus tragique fut que Silas commença à ressentir un froid intérieur que rien ne pouvait calmer. Il erra à travers le monde comme un mendiant, les pieds en sang, cherchant un temple où se réfugier, mais chaque fois qu'il s'approchait d'un autel, il sentait que les images lui tournaient le dos. Ce n'était pas de la haine divine ; c'était que Silas avait perdu la faculté de reconnaître le sacré et, par conséquent, l'univers ne pouvait plus lui offrir sa protection.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Silas mourut dans la solitude d'un désert, comprenant trop tard que lorsqu'on joue avec l'éternel, c'est le temps lui-même qui nous échappe. Il avait tenu le ciel entre ses mains et l'avait utilisé pour orner son orgueil. Son Ikigai, son but oublié, lui murmura dans son dernier souffle : « On ne peut demander la lumière quand on a pris plaisir à éteindre le soleil ». Son histoire resta gravée dans les sables comme un avertissement que le respect n'est pas une norme, mais la peau avec laquelle l'âme ressent l'amour de Dieu.</p>

                <!-- JA -->
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">昔、サイラスという商人が、計り知れない価値のある聖像のコレクションを持っていました。サイラスは信仰心のある男ではありませんでした。彼にとって、翡翠の仏像や黄金のキリスト像は、自分の成功を証明するトロフィーに過ぎませんでした。宴会の席で、サイラスは聖像の頭に滑稽な帽子を被せたり、客のグラスを持たせたりして、何千人もの人々が涙を流して崇拝するものを嘲笑いながら冒涜していました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">ある日、サイラスは、忘れ去られた聖人の祭壇から来たとされる小さな油灯を手に入れました。そのランプは、決して消えることのない柔らかな黄金の光を放っていました。しかし、サイラスは、ある遊女を感銘させようとして、ランプの聖なる油を使ってワインに香りをつけようと決めたのです。油がグラスに触れた瞬間、ランプは千々に砕け、光は消え去り、部屋は絶対的な凍てつく闇に包まれました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">その夜から、サイラスの富は崩れ去りました。彼の船は穏やかな海で沈没し、友人たちは煙のように消えていきました。最も悲劇的だったのは、サイラスが何をもってしても鎮めることのできない内面的な冷たさを感じ始めたことでした。彼は足から血を流しながら物乞いとして世界を彷徨い、避難できる寺院を探しましたが、祭壇に近づくたびに、聖像たちが彼に背を向けているように感じました。それは神の憎しみではありませんでした。サイラスが聖なるものを認識する能力を失ってしまったため、宇宙がもはや彼に保護を提供できなくなったのです。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">サイラスは砂漠の孤独の中で死に、永遠なるものを弄ぶとき、逃げていくのは時間そのものであることをあまりにも遅くに悟りました。彼は天をその手に持っていながら、それを自らの傲慢さを飾るために使ったのです。彼の生きがい（Ikigai）、すなわち忘れ去られた使命は、最期の息の中で彼にこう囁きました。「太陽を消すことを楽しんでいた者が、光を求めることはできない」。彼の物語は、畏敬の念こそが魂が神の愛を感じるための皮膚であることを教えています。</p>

                <!-- PT -->
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Havia uma vez um mercador chamado Silas que possuía uma coleção de estátuas sagradas de incalculável valor. Silas não era um homem de fé; para ele, os Budas de jade e os Cristos de ouro eram apenas troféus que demonstravam o seu sucesso. Nos seus banquetes, Silas costumava colocar chapéus ridículos sobre as cabeças das estatuas ou usá-las para segurar as taças dos seus convidados, rindo enquanto profanava aquilo que milhares de pessoas veneravam com lágrimas nos olhos.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Um dia, Silas adquiriu uma pequena lâmpada de azeite que, segundo se dizia, provinha do altar de um santo esquecido. A lâmpada emitia uma luz dourada e suave que nunca se apagava. No entanto, Silas, querendo impressionar uma cortesã, decidiu usar o azeite sagrado da lâmpada para perfumar o seu vinho. No instante em que o azeite tocou o vidro, a lâmpada quebrou-se em mil pedaços e a luz desvaneceu-se, deixando a sala numa escuridão absoluta e gélida.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">A partir dessa noite, a fortuna de Silas desmoronou-se. Os seus barcos afundaram-se em mares tranquilos e os seus amigos desapareceram como o fumo. O mais trágico foi que Silas começou a sentir um frio interno que nada podia acalmar. Vagou pelo mundo como um mendigo, com os pés sangrentos, procurando um templo onde refugiar-se, mas cada vez que se aproximava de um altar, sentia que as imagens lhe davam as costas. Não era ódio divino; era que Silas tinha perdido a faculdade de reconhecer o sagrado e, portanto, o universo já não podia oferecer-lhe a sua proteção.</p> Portuguese訳-->
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Silas morreu na solidão de um deserto, compreendendo tarde demais que quando se joga com o eterno, é o próprio tempo que nos escapa. Tinha tido o céu nas suas mãos e tinha-o usado para adornar a sua soberba. O seu Ikigai, o seu propósito esquecido, sussurrou-lhe no último suspiro: "Não se pode pedir luz quando se desfrutou a apagar o sol". A sua história ficou gravada nas areias como um aviso de que o respeito não é uma norma, mas a pele com que a alma sente o amor de Deus.</p>

                <!-- VI -->
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Ngày xưa, có một thương nhân tên là Silas sở hữu một bộ sưu tập các bức tượng thánh vô giá. Silas không phải là người có đức tin; đối với ông, những bức tượng Phật bằng ngọc bích và tượng Chúa bằng vàng chỉ là những chiến lợi phẩm thể hiện sự thành đạt của mình. Trong các bữa tiệc, Silas thường đặt những chiếc mũ nực cười lên đầu các bức tượng hoặc dùng chúng để đỡ ly rượu của thực khách, vừa cười vừa xúc phạm những gì mà hàng ngàn người tôn kính với những giọt lệ trong mắt.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Một ngày nọ, Silas có được một ngọn đèn dầu nhỏ, người ta nói rằng nó đến từ bệ thờ của một vị thánh bị lãng quên. Ngọn đèn tỏa ra ánh sáng vàng dịu nhẹ và không bao giờ tắt. Tuy nhiên, Silas vì muốn gây ấn tượng với một kỹ nữ nên đã quyết định dùng dầu thánh từ ngọn đèn để ướp hương cho rượu của mình. Ngay khoảnh khắc dầu chạm vào ly, ngọn đèn vỡ tan thành ngàn mảnh và ánh sáng biến mất, để lại căn phòng trong bóng tối băng giá và tuyệt đối.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Từ đêm đó, vận may của Silas sụp đổ. Những con tàu của ông bị chìm giữa biển khơi phẳng lặng và bạn bè ông biến mất như làn khói. Điều bi thảm nhất là Silas bắt đầu cảm thấy một luồng hơi lạnh từ bên trong mà không gì có thể xoa dịu được. Ông lang thang khắp thế gian như một kẻ ăn xin, đôi chân rỉ máu, tìm kiếm một ngôi đền để nương náu, nhưng mỗi khi ông đến gần bệ thờ, ông cảm thấy những bức tượng như quay lưng lại với mình. Đó không phải là sự ghét bỏ của thần thánh; mà là vì Silas đã mất đi khả năng nhận ra sự thiêng liêng, và do đó, vũ trụ không còn có thể cung cấp sự bảo vệ cho ông nữa.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Silas chết trong sự cô độc giữa sa mạc, hiểu ra quá muộn rằng khi người ta đùa giỡn với những điều vĩnh cửu, thì chính thời gian sẽ vuột mất. Ông đã từng nắm giữ cả thiên thượng trong tay nhưng lại dùng nó để trang điểm cho sự ngạo mạn của mình. Ikigai của ông, mục đích đã bị lãng quên, đã thì thầm vào hơi thở cuối cùng của ông: "Không thể cầu xin ánh sáng khi người ta đã từng thích thú với việc dập tắt mặt trời". Câu chuyện của ông vẫn còn ghi khắc trong những hạt cát như một lời cảnh báo rằng sự tôn kính không phải là một chuẩn mực, mà là làn da để linh hồn cảm nhận được tình yêu của Thiên Chúa.</p>
            </div>

            <!-- ═══ ART ═══ -->
            <div class="final-art fade-in" style="text-align: center; margin-top: 4rem; margin-bottom: 2rem;">
                <img src="assets/art.jpg" alt="Obra de Arte Karma LXI" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            </div>

            <!-- ═══ MORAL ═══ -->
            <div class="moral fade-in">
                <span class="es">Quien trata lo sagrado como un adorno, termina por encontrar que su propia vida carece de cimiento; la reverencia es el alimento del alma.</span>
                <span class="en">He who treats the sacred as an ornament ends up finding that his own life lacks a foundation; reverence is the food of the soul.</span>
                <span class="it">Chi tratta il sacro come un ornamento finisce per scoprire che la sua stessa vita manca di fondamenta; la riverenza è l'alimento dell'anima.</span>
                <span class="zh">将神圣视为装饰的人，最终会发现自己的生活缺乏根基；敬畏是灵魂的食粮。</span>
                <span class="ar">من يعامل المقدس كزينة، ينتهي به الأمر ليجد أن حياته تفتقر إلى أساس؛ التوقير هو غذاء الروح.</span>
                <span class="ru">Тот, кто относится к священному как к украшению, в итоге обнаруживает, что его собственной жизни не хватает фундамента; почтение — это пища для души.</span>
                <span class="de">Wer das Heilige wie einen Schmuck behandelt, muss feststellen, dass seinem eigenen Leben das Fundament fehlt; Ehrfurcht ist die Nahrung der Seele.</span>
                <span class="fr">Celui qui traite le sacré comme un ornement finit par découvrir que sa propre vie manque de fondement ; la révérence est l'aliment de l'âme.</span>
                <span class="ja">聖なるものを装飾品として扱う者は、自らの人生に基盤がないことに気づくことになります。畏敬の念は魂の糧なのです。</span>
                <span class="pt">Quem trata o sagrado como um adorno, acaba por descobrir que a sua própria vida carece de alicerces; a reverência é l'alimento da alma.</span>
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

print("Chapter 61 HTML successfully updated with FULL translations.")
