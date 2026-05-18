
import os

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capítulo LXII: El Libro del Karma</title>
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
            <img src="assets/hero.jpg" alt="Karma LXII" id="hero-img">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <div class="chapter-num">
                    <span class="es">CAPÍTULO LXII</span><span class="en">CHAPTER LXII</span><span class="it">CAPITOLO LXII</span><span class="zh">第六十二章</span><span class="ar">الفصل الثاني والستون</span><span class="ru">ГЛАВА LXII</span><span class="de">KAPITEL LXII</span><span class="fr">CHAPITRE LXII</span><span class="ja">第62章</span><span class="pt">CAPÍTULO LXII</span><span class="vi">CHƯƠNG LXII</span>
                </div>
                <h1 class="chapter-title">
                    <span class="es">El Veneno de la Limosna Arrogante</span>
                    <span class="en">The Poison of Arrogant Alms</span>
                    <span class="it">Il Veleno dell'Elemosina Arrogante</span>
                    <span class="zh">傲慢施舍之毒</span>
                    <span class="ar">سم الصدقة المتكبرة</span>
                    <span class="ru">Яд высокомерной милостыни</span>
                    <span class="de">Das Gift des hochmütigen Almosens</span>
                    <span class="fr">Le Poison de l'Aumône Arrogante</span>
                    <span class="ja">傲慢な施しの毒</span>
                    <span class="pt">O Veneno da Esmola Arrogante</span>
                    <span class="vi">Chất Độc Của Sự Bố Thí Kiêu Ngạo</span>
                </h1>
                <p class="subtitle">
                    <span class="es">"La mano que da para humillar, no está soltando el oro, sino comprando su propia soledad; lo que das con burla, te será devuelto en el eco de las risas de quienes te rodean."</span>
                    <span class="en">"The hand that gives to humiliate is not releasing gold, but buying its own loneliness; what you give with mockery will be returned to you in the echo of the laughter of those around you."</span>
                    <span class="it">"La mano che dà per umiliare non sta lasciando l'oro, ma comprando la propria solitudine; ciò che dai con scherno ti tornerà nell'eco delle risate di chi ti circonda."</span>
                    <span class="zh">“为了羞辱而施予的手，放下的不是黄金，而是购买了自己的孤独；你带着嘲弄给予的一切，都将在周围人的笑声回响中还给你。”</span>
                    <span class="ar">"اليد التي تعطي للإذلال لا تطلق الذهب، بل تشتري وحدتها الخاصة؛ وما تعطيه بسخرية سيعود إليك في صدى ضحكات من حولك."</span>
                    <span class="ru">«Рука, дающая ради унижения, не выпускает золото, а покупает собственное одиночество; то, что ты даешь с насмешкой, вернется к тебе эхом смеха окружающих».</span>
                    <span class="de">„Die Hand, die gibt, um zu demütigen, lässt nicht Gold los, sondern kauft ihre eigene Einsamkeit; was du mit Spott gibst, wird dir im Echo des Lachens derer um dich herum zurückgegeben.“</span>
                    <span class="fr">« La main qui donne pour humilier ne lâche pas l'or, mais achète sa propre solitude ; ce que tu donnes avec dérision te sera rendu dans l'écho des rires de ceux qui t'entourent. »</span>
                    <span class="ja">「屈辱を与えるために差し出される手は、黄金を放しているのではなく、自らの孤独を買っているのです。嘲笑とともに与えたものは、周囲の人々の笑い声の響きとなってあなたに返ってくるでしょう。」</span>
                    <span class="pt">"A mão que dá para humilhar não está a soltar o ouro, mas a comprar a sua própria solidão; o que dás com deboche ser-te-á devolvido no eco dos risos de quem te rodeia."</span>
                    <span class="vi">"Bàn tay cho đi để nhục mạ không phải đang buông bỏ vàng bạc, mà là đang mua lấy sự cô độc của chính mình; những gì bạn cho đi với sự chế nhạo sẽ quay lại với bạn trong tiếng cười nhạo báng của những kẻ xung quanh."</span>
                </p>
                <div class="scroll-indicator"></div>
            </div>
        </section>

        <div class="story-container">
            <!-- ═══ EXPLICACIÓN KÁRMICA ═══ -->
            <div class="story-block fade-in">
                <!-- ES -->
                <p class="es"><span class="drop-cap">E</span>l karma es un espejo de una precisión aterradora, no solo registra lo que hacemos, sino la frecuencia emocional desde la que actuamos. El acto de dar, la generosidad, es en esencia una apertura del corazón, una expansión del alma hacia el otro. Sin embargo, cuando esa generosidad se contamina con la soberbia, el resultado kármico se fragmenta. El universo reconoce el flujo de la riqueza y te devuelve abundancia material, pero también registra la humillación que infligiste. El resultado es una paradoja dolorosa: una vida llena de recursos pero vacía de respeto genuino.</p>
                <p class="es">Este mecanismo funciona porque el desprecio que lanzas al dar es una declaración de superioridad ilusoria. Al burlarte de quien recibe, estás sembrando la semilla de tu propio aislamiento. En el futuro, tu fortuna será como un banquete en una sala llena de espejos deformantes: verás gente a tu alrededor, disfrutarás de los mejores manjares, pero percibirás que nadie te mira con amor, sino con la misma mirada de mofa que tú regalaste un día. Estar rodeado de personas que se ríen de ti a tus espaldas es el eco exacto del desprecio que sembraste bajo el disfraz de la caridad.</p>
                <p class="es">El "antes" de este karma es la ceguera del ego, que cree que el dinero le da derecho a pisotear la dignidad ajena. El "después" es la riqueza amarga, donde el dinero no puede comprar un solo gramo de lealtad o afecto real. Para alinear nuestra vida con el Ikigai luminoso, debemos entender que el respeto es el recipiente que contiene la bendición de la abundancia. Sin respeto, la riqueza es solo un adorno en una celda de soledad. Dar con humildad es la única forma de asegurar que nuestra cosecha futura sea dulce y esté habitada por la luz de la verdadera compañía.</p>

                <!-- EN -->
                <p class="en"><span class="drop-cap">K</span>arma is a mirror of terrifying precision; it records not only what we do, but the emotional frequency from which we act. The act of giving, of generosity, is essentially an opening of the heart, an expansion of the soul toward another. However, when that generosity is contaminated with pride, the karmic result fragments. The universe recognizes the flow of wealth and returns material abundance to you, but it also records the humiliation you inflicted. The result is a painful paradox: a life full of resources but empty of genuine respect.</p>
                <p class="en">This mechanism works because the contempt you throw when giving is a declaration of illusory superiority. By mocking the recipient, you are sowing the seed of your own isolation. In the future, your fortune will be like a banquet in a room full of distorting mirrors: you will see people around you, you will enjoy the finest delicacies, but you will perceive that no one looks at you with love, but with the same mocking gaze you once gave. Being surrounded by people who laugh at you behind your back is the exact echo of the contempt you sowed under the guise of charity.</p>
                <p class="en">The "before" of this karma is the blindness of the ego, which believes that money gives it the right to trample on the dignity of others. The "after" is bitter wealth, where money cannot buy a single gram of loyalty or real affection. To align our lives with the luminous Ikigai, we must understand that respect is the vessel that contains the blessing of abundance. Without respect, wealth is just an ornament in a cell of loneliness. Giving with humility is the only way to ensure that our future harvest is sweet and inhabited by the light of true companionship.</p>

                <!-- IT -->
                <p class="it"><span class="drop-cap">I</span>l karma è uno specchio di precisione terrificante: registra non solo l'azione, ma la frequenza emotiva del cuore. Quando la generosità è contaminata dall'orgoglio, il risultato è una paradossale vita piena di risorse ma vuota di rispetto genuino.</p>
                <p class="it">Il disprezzo che lanci nel dare è un seme di isolamento. In futuro, la tua fortuna sarà come un banchetto pieno di persone che ti guardano con lo stesso sguardo di scherno che tu hai rivolto agli altri. Essere circondati da chi ride alle tue spalle è l'eco dell'arroganza travestita da carità.</p>
                <p class="it">Senza rispetto, la ricchezza è solo un ornamento in una cella di solitudine. Dare con umiltà è l'unico modo per assicurare che il raccolto futuro sia dolce e abitato dalla luce della vera compagnia.</p>

                <!-- ZH -->
                <p class="zh"><span class="drop-cap">业</span>力是一面极其精确的镜子，它记录的不仅是我们的行为，还有我们行为时的情感频率。当慷慨被傲慢污染时，结果就是一种资源充足却缺乏真诚尊重的痛苦悖论。</p>
                <p class="zh">你在施予时表现出的蔑视是孤独的种子。未来，你的财富将像一场充满嘲笑目光的宴会。被在背后嘲笑你的人包围，正是你曾经伪装成慈善的傲慢所产生的回响。</p>
                <p class="zh">没有尊重，财富只是孤独牢房中的装饰品。以谦卑之心施予，是确保未来收获甜蜜且充满真诚陪伴之光的唯一途径。</p>

                <!-- AR -->
                <p class="ar"><span class="drop-cap">ا</span>لكارما هي مرآة ذات دقة مرعبة؛ فهي لا تسجل ما نفعله فحسب، بل تسجل التردد العاطفي الذي نتصرف من خلاله. عندما يتلوث الكرم بالكبرياء، تكون النتيجة مفارقة مؤلمة: حياة مليئة بالموارد ولكنها خالية من الاحترام الحقيقي.</p>
                <p class="ar">الازدراء الذي تظهره أثناء العطاء هو بذرة عزلتك. في المستقبل، ستكون ثروتك مثل مأدبة محاطة بأشخاص ينظرون إليك بنفس نظرة السخرية التي منحتها يوماً ما. إن كونك محاطاً بأشخاص يضحكون عليك خلف ظهرك هو الصدى الدقيق للازدراء الذي زرعته تحت قناع الصدقة.</p>
                <p class="ar">بدون احترام، الثروة هي مجرد زينة في زنزانة من الوحدة. العطاء بتواضع هو الطريقة الوحيدة لضمان أن يكون حصادك المستقبلي حلواً ومسكوناً بنور الرفقة الحقيقية.</p>

                <!-- RU -->
                <p class="ru"><span class="drop-cap">К</span>арма — это зеркало пугающей точности; оно фиксирует не только наши поступки, но и эмоциональную частоту сердца. Когда щедрость осквернена гордыней, результатом становится болезненный парадокс: жизнь, полная ресурсов, но лишенная подлинного уважения.</p>
                <p class="ru">Презрение, проявленное при даянии — это семя одиночества. В будущем ваше богатство станет подобно банкету, где окружающие смотрят на вас с той же насмешкой, которую вы когда-то проявляли к другим. Смех за вашей спиной — это эхо высокомерия, скрытого под маской благотворительности.</p>
                <p class="ru">Без уважения богатство — лишь украшение в камере одиночества. Даяние со смирением — единственный способ гарантировать, что будущий урожай будет сладким и наполненным светом истинной дружбы.</p>

                <!-- DE -->
                <p class="de"><span class="drop-cap">K</span>arma ist ein Spiegel von erschreckender Präzision; es registriert nicht nur, was wir tun, sondern auch die emotionale Frequenz unseres Herzens. Wenn Großzügigkeit durch Stolz verunreinigt wird, ist das Ergebnis ein schmerzhaftes Paradoxon: ein Leben voller Ressourcen, aber ohne echten Respekt.</p>
                <p class="de">Die Verachtung, die du beim Geben zeigst, ist der Samen deiner Isolation. In Zukunft wird dein Reichtum wie ein Bankett sein, bei dem dich die Menschen mit demselben Spott ansehen, den du einst anderen entgegengebracht hast. Von Menschen umgeben zu sein, die hinter deinem Rücken lachen, ist das Echo des Hochmuts.</p>
                <p class="de">Ohne Respekt ist Reichtum nur ein Schmuck in einer Zelle der Einsamkeit. Mit Demut zu geben ist der einzige Weg, um sicherzustellen, dass die künftige Ernte süß und vom Licht wahrer Gemeinschaft erfüllt ist.</p>

                <!-- FR -->
                <p class="fr"><span class="drop-cap">L</span>e karma est un miroir d'une précision terrifiante ; il enregistre non seulement ce que nous faisons, mais aussi la fréquence émotionnelle du cœur. Quand la générosité est contaminée par l'orgueil, le résultat est un paradoxe douloureux : une vie pleine de ressources mais vide de respect sincère.</p>
                <p class="fr">Le mépris que vous manifestez en donnant est une graine d'isolement. À l'avenir, votre fortune sera comme un banquet où les gens vous regarderont avec le même regard moqueur que vous avez eu autrefois. Être entouré de gens qui rient dans votre dos est l'écho exact de l'arrogance déguisée en charité.</p>
                <p class="fr">Sans respect, la richesse n'est qu'un ornement dans une cellule de solitude. Donner avec humilité est le seul moyen de s'assurer que la récolte future sera douce et habitée par la lumière d'une véritable compagnie.</p>

                <!-- JA -->
                <p class="ja"><span class="drop-cap">カ</span>ルマは恐ろしいほど精密な鏡です。それは私たちの行動だけでなく、心の底にある感情をも記録します。寛大さがプライドによって汚されるとき、その結果は「物質的には豊かだが、真の尊敬を欠く」という苦いパラドックスとなります。</p>
                <p class="ja">与えるときに見せる軽蔑は、自らの孤独の種となります。将来、あなたの富は、かつてあなたが他人に向けたのと同じ嘲笑の目に囲まれた宴会のようになるでしょう。背後で笑う人々に囲まれることは、慈善の仮面を被った傲慢さの正確な反響なのです。</p>
                <p class="ja">尊敬がなければ、富は孤独という独房の装飾に過ぎません。謙虚に与えることこそが、将来の収穫を甘美なものにし、真の友情の光に満ちたものにする唯一の方法なのです。</p>

                <!-- PT -->
                <p class="pt"><span class="drop-cap">O</span> karma é um espelho de uma precisão aterradora; regista não só o que fazemos, mas a frequência emocional do coração. Quando a generosidade é contaminada pelo orgulho, o resultado é um paradoxo doloroso: uma vida cheia de recursos, mas vazia de respeito genuíno.</p>
                <p class="pt">O desprezo que lanças ao dar é a semente do teu isolamento. No futuro, a tua fortuna será como um banquete onde as pessoas te olham com o mesmo olhar de deboche que um dia deste a outros. Estar rodeado de quem se ri de ti pelas costas é o eco exato da arrogância disfarçada de caridade.</p>
                <p class="pt">Sem respeito, a riqueza é apenas um adorno numa cela de solidão. Dar com humildade é a única forma de assegurar que a colheita futura seja doce e habitada pela luz da verdadeira companhia.</p>

                <!-- VI -->
                <p class="vi"><span class="drop-cap">N</span>hân quả là một tấm gương có độ chính xác đáng sợ; nó không chỉ ghi lại những gì chúng ta làm, mà cả tần số cảm xúc của trái tim. Khi lòng tốt bị vấy bẩn bởi sự kiêu ngạo, kết quả sẽ là một nghịch lý đau đớn: một cuộc sống đầy đủ tài nguyên nhưng lại trống rỗng sự tôn trọng chân thành.</p>
                <p class="vi">Sự khinh miệt mà bạn thể hiện khi cho đi chính là hạt giống của sự cô lập. Trong tương lai, sự giàu có của bạn sẽ giống như một bữa tiệc nơi mọi người nhìn bạn với cùng ánh mắt chế nhạo mà bạn đã từng dành cho người khác. Việc bị vây quanh bởi những kẻ cười nhạo sau lưng chính là tiếng vang chính xác của sự kiêu ngạo núp bóng từ thiện.</p>
                <p class="vi">Không có sự tôn trọng, giàu sang chỉ là vật trang trí trong ngục tù đơn độc. Cho đi với sự khiêm nhường là cách duy nhất để đảm bảo rằng mùa gặt tương lai sẽ ngọt ngào và tràn đầy ánh sáng của sự đồng hành thực sự.</p>
            </div>

            <!-- ═══ PARÁBOLA ═══ -->
            <div class="story-block parable-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">
                <h3 class="es" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">El Banquete de las Risas Huecas</h3>
                <h3 class="en" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">The Banquet of Hollow Laughter</h3>
                <h3 class="it" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Il Banchetto delle Risate Vuote</h3>
                <h3 class="zh" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">空洞笑声之宴</h3>
                <h3 class="ar" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">مأدبة الضحكات الجوفاء</h3>
                <h3 class="ru" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Пир пустых насмешек</h3>
                <h3 class="de" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Das Bankett des hohlen Lachens</h3>
                <h3 class="fr" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Le Banquet des Rires Creux</h3>
                <h3 class="ja" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">虚ろな笑いの宴</h3>
                <h3 class="pt" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">O Banquete dos Risos Vazios</h3>
                <h3 class="vi" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Bữa Tiệc Của Những Tiếng Cười Rỗng Tuếch</h3>

                <!-- ES -->
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">En la antigua ciudad de Benarés, vivía un joven rico llamado Vimal que se jactaba de su gran generosidad. Vimal solía salir a las plazas y, con gesto altivo, lanzaba monedas de oro a los mendigos, disfrutando de ver cómo se peleaban por ellas. "¡Mirad cómo se arrastran por mi brillo!", decía entre risas a sus amigos, mientras señalaba las cicatrices y los harapos de los necesitados. Daba mucho, pero cada moneda iba acompañada de un chiste cruel o una mirada de profundo asco. Creía que su riqueza le otorgaba un trono de superioridad desde el cual podía juzgar la desdicha ajena.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Los años pasaron y, tal como dicta el karma, la generosidad de Vimal le trajo aún más riquezas. Se convirtió en el hombre más próspero de la región, dueño de palacios que deslumbraban al sol. Sin embargo, algo extraño empezó a suceder en su círculo social. Vimal organizaba fiestas legendarias, gastando fortunas en los mejores músicos y vinos, pero pronto se dio cuenta de que el ambiente era gélido. Notaba cómo, en el momento en que él entraba en una sala, los murmullos se detenían, y en cuanto se daba la vuelta, el aire se llenaba de risas disimuladas. Sus "amigos" comían de su mesa, pero sus ojos brillaban con la misma burla que él había mostrado antaño.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Un día, Vimal escuchó a su invitado más cercano decir: "Es patético, cree que su oro oculta lo ridículo que se ve intentando comprar nuestra admiración. Es solo un tonto con monedas". En ese instante, Vimal recordó la cara del niño mendigo al que le había lanzado una moneda mientras se reía de su orfandad. Comprendió que había construido un palacio de oro, pero que el cemento eran las burlas que había sembrado. Tenía todo lo que el dinero podía comprar, excepto lo único que su alma necesitaba: el respeto sincero de otro ser humano.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal pasó el resto de sus días en el silencio de sus salones vacíos, dándose cuenta de que la verdadera caridad no es dar lo que te sobra, sino reconocer tu propia fragilidad en el otro. Su Ikigai se había oscurecido porque había olvidado que la riqueza sin honor es una corona de espinas doradas. Su historia nos enseña que el karma no se equivoca de dirección: si siembras monedas con espinas de desprecio, recogerás una montaña de oro, pero te pincharás con cada pieza al intentar abrazar a alguien.</p>

                <!-- EN -->
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">In the ancient city of Varanasi, lived a wealthy young man named Vimal who boasted of his great generosity. Vimal used to go out to the squares and, with a haughty gesture, throw gold coins to the beggars, enjoying seeing them fight over them. "Look how they crawl for my shine!" he would say with a laugh to his friends, while pointing at the scars and rags of the needy. He gave a lot, but every coin was accompanied by a cruel joke or a look of profound disgust. He believed that his wealth gave him a throne of superiority from which he could judge the misfortune of others.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Years passed and, as karma dictates, Vimal's generosity brought him even more wealth. He became the most prosperous man in the region, owner of palaces that dazzled in the sun. However, something strange began to happen in his social circle. Vimal organized legendary parties, spending fortunes on the best musicians and wines, but he soon realized that the atmosphere was icy. He noticed how, the moment he entered a room, the murmurs stopped, and as soon as he turned around, the air was filled with disguised laughter. His "friends" ate from his table, but their eyes shone with the same mockery he had shown in the past.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">One day, Vimal heard his closest guest say: "It's pathetic; he thinks his gold hides how ridiculous he looks trying to buy our admiration. He's just a fool with coins." At that moment, Vimal remembered the face of the beggar child to whom he had thrown a coin while laughing at his orphanhood. He understood that he had built a palace of gold, but the cement was the mockery he had sown. He had everything money could buy, except the only thing his soul needed: the sincere respect of another human being.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal spent the rest of his days in the silence of his empty halls, realizing that true charity is not giving what you have left over, but recognizing your own fragility in the other. His Ikigai had darkened because he had forgotten that wealth without honor is a crown of golden thorns. His story teaches us that karma does not mistake its direction: if you sow coins with thorns of contempt, you will reap a mountain of gold, but you will prick yourself with every piece when trying to embrace someone.</p>

                <!-- IT -->
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal era un giovane ricco che gettava monete ai mendicanti per il gusto di vederli umiliarsi. Rideva dei loro stracci, convinto che il suo oro lo rendesse superiore. Gli anni passarono e divenne l'uomo più prospero della regione, ma le sue feste erano fredde. Non appena si voltava, la stanza si riempiva di risate soffocate.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">I suoi "amici" mangiavano alla sua tavola ma lo deridevano in segreto. Vimal capì di aver costruito un palazzo d'oro usando il disprezzo come cemento. Aveva tutto, tranne l'unica cosa di cui la sua anima aveva bisogno: il rispetto sincero.</p>

                <!-- ZH -->
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">富有青年维马尔常带着傲慢向乞丐扔金币，以此为乐。多年后他富甲一方，但他发现宴会上气氛冰冷。每当他转身，身后便满是窃笑。他的“朋友”享用他的美酒，却在心中鄙视他。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">维马尔意识到，他用蔑视堆砌了金碧辉煌的宫殿。他拥有金钱能买到的一切，唯独缺少灵魂最渴望的东西：他人真心的尊重。他的故事告诉我们，如果施予时带着蔑视的刺，收获的金山也会刺痛双臂。</p>

                <!-- AR -->
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">كان فيمال شاباً غنياً يرمي العملات للفقراء ليتلذذ برؤيتهم يتوسلون. مرت السنين وأصبح أغنى رجل في المنطقة، لكن حفلاته كانت باردة. بمجرد أن يدير ظهره، تمتلئ القاعة بضحكات السخرية المكتومة من "أصدقائه".</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">أدرك فيمال أنه بنى قصراً من ذهب باستخدام الاحتقار كإسمنت. كان لديه كل شيء يمكن للمال شراؤه، باستثناء الاحترام الصادق. قصته تعلمنا أن الكارما لا تخطئ الطريق: إذا زرعت نقوداً بأشواك الازدراء، فستحصد جبل ذهب سيجرحك عند كل محاولة عناق.</p>

                <!-- RU -->
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Богатый юноша Вимал бросал монеты нищим ради забавы. С годами он стал самым процветающим человеком, но на его пирах царил холод. Как только он отворачивался, зал наполнялся насмешливым шепотом его «друзей», которые презирали его в душе.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Вимал понял, что построил золотой дворец, скрепив его насмешками. У него было всё, кроме искреннего уважения. Его история учит нас: если сеять монеты с шипами презрения, вы соберете гору золота, но уколетесь о каждую монету, пытаясь кого-то обнять.</p>

                <!-- DE -->
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal war ein reicher Mann, der Bettlern Münzen zuwarf, nur um sie zu demütigen. Er wurde steinreich, doch seine Feste blieben freudlos. Sobald er sich umdrehte, lachten seine Gäste hinter seinem Rücken über ihn. Er begriff, dass er seinen Palast mit Verachtung als Zement gebaut hatte.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Er hatte alles, was man kaufen kann, außer ehrlichem Respekt. Seine Geschichte lehrt uns, dass Karma den Weg kennt: Wenn du Münzen mit Dornen der Verachtung säst, wirst du einen Berg Gold ernten, dich aber bei jedem Versuch einer Umarmung daran stechen.</p>

                <!-- FR -->
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal était un jeune riche qui jetait des pièces aux mendiants pour le plaisir de les voir s'humilier. Devenu richissime, il s'aperçut que ses fêtes étaient glaciales. Ses "amis" profitaient de sa table mais se moquaient de lui dès qu'il avait le dos tour.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal comprit qu'il avait bâti un palais d'or en utilisant le mépris comme ciment. Il possédait tout, sauf le respect sincère. Son histoire nous enseigne que si l'on sème des pièces avec des épines de dédain, on récolte une montagne d'or qui blesse dès qu'on veut embrasser quelqu'un.</p>

                <!-- JA -->
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">富裕な若者ヴィマルは、物乞いたちに小銭を投げ、彼らが争う姿を見て嘲笑っていました。数年後、彼は地域で最も裕福になりましたが、彼の宴会には冷たい空気が流れていました。彼が背を向けた途端、部屋は「友人」たちの忍び笑いで満たされました。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">ヴィマルは、蔑みをセメントにして金の宮殿を建ててしまったことに気づきました。彼は金で買えるものはすべて持っていましたが、魂が切望する真の尊敬だけは持っていませんでした。軽蔑の棘とともに種をまけば、収穫した金山に抱きつこうとするたびに傷つくことになるのです。</p>

                <!-- PT -->
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal era um jovem rico que atirava moedas aos mendigos para se rir da sua miséria. Tornou-se o homem mais próspero da região, mas as suas festas eram gélidas. Os seus "amigos" comiam à sua mesa, mas troçavam dele assim que ele se virava de costas.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal percebeu que tinha construído um palácio de ouro usando o desprezo como cimento. Tinha tudo o que o dinheiro comprava, exceto o respeito sincero. Se semeias moedas com espinhos de deboche, colherás montanhas de ouro, mas picar-te-ás em cada peça ao tentar abraçar alguém.</p>

                <!-- VI -->
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal là một thiếu gia giàu có thường ném tiền cho người nghèo để tiêu khiển. Sau này ông trở thành người giàu nhất vùng, nhưng các bữa tiệc của ông luôn lạnh lẽo. Những "người bạn" hưởng thụ sự xa hoa của ông nhưng lại chế nhạo ông ngay khi ông quay lưng đi.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Vimal nhận ra mình đã xây cung điện vàng bằng chất kết dính là sự khinh miệt. Ông có mọi thứ tiền mua được, ngoại trừ sự tôn trọng chân thành. Câu chuyện dạy rằng nếu gieo những đồng tiền bằng cái gai của sự coi thường, bạn sẽ gặt được núi vàng nhưng sẽ bị đâm đau mỗi khi muốn ôm lấy ai đó.</p>
            </div>

            <!-- ═══ ART ═══ -->
            <div class="final-art fade-in" style="text-align: center; margin-top: 4rem; margin-bottom: 2rem;">
                <img src="assets/art.jpg" alt="Obra de Arte Karma LXII" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            </div>

            <!-- ═══ MORAL ═══ -->
            <div class="moral fade-in">
                <span class="es">La riqueza que humilla es una cárcel de oro; da con amor y serás rico en respeto, da con burla y serás pobre en medio de tesoros.</span>
                <span class="en">Wealth that humiliates is a golden prison; give with love and you will be rich in respect, give with mockery and you will be poor in the midst of treasures.</span>
                <span class="it">La ricchezza che umilia è una prigione d'oro; dai con amore e sarai ricco di rispetto, dai con scherno e sarai povero in mezzo ai tesori.</span>
                <span class="zh">羞辱他人的财富是黄金牢房；用爱施予，你将富有尊重；用嘲弄施予，你将在宝藏中贫穷。</span>
                <span class="ar">الثروة التي تذل هي سجن ذهبي؛ أعطِ بحب وستكون غنياً بالاحترام، أعطِ بسخرية وستكون فقيراً وسط الكنوز.</span>
                <span class="ru">Богатство, которое унижает — это золотая тюрьма; давай с любовью, и будешь богат уважением, давай с насмешкой, и будешь беден среди сокровищ.</span>
                <span class="de">Reichtum, der demütigt, ist ein goldenes Gefängnis; gib mit Liebe und du wirst reich an Respekt sein, gib mit Spott und du wirst arm inmitten von Schätzen sein.</span>
                <span class="fr">La richesse qui humilie est une prison dorée ; donne avec amour et tu seras riche de respect, donne avec dérision et tu seras pauvre au milieu des trésors.</span>
                <span class="ja">屈辱を与える富は黄金の牢獄です。愛とともに与えれば尊敬において富み、嘲笑とともに与えれば宝物の中で貧しくなるでしょう。</span>
                <span class="pt">A riqueza que humilha é uma prisão de ouro; dá com amor e serás rico em respeito, dá com deboche e serás pobre no meio de tesouros.</span>
                <span class="vi">Sự giàu sang làm nhục người khác là ngục tù bằng vàng; hãy cho đi bằng tình thương và bạn sẽ giàu sự tôn trọng, cho đi bằng sự chế nhạo và bạn sẽ nghèo nàn giữa những kho báu.</span>
            </div>

            <center class="fade-in" style="margin-top: 4rem;">
                <img src="assets/hero.jpg" alt="Karma LXII Full" style="max-width: 600px; width: 100%; border-radius: 8px; border: 1px solid rgba(197,160,89,0.3); box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
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
                        <strong>🇻🇳 Tiếng Việt:</strong><br>Nhân: Bố thí mà không tôn trọng người.<br>Quả: Giàu mà không được người thương kính.
                    </p>
                    <p style="color: #ddd; margin-bottom: 1.5rem;"><strong>🇬🇧 English:</strong><br>Cause: Doing charity without respect.<br>Effect: Brings wealthy, but unbeloved and disrespectful people.</p>
                    <p class="es" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197,160,89,0.1); padding: 1rem; border-left: 3px solid var(--gold);"><strong>Traducción Recreada:</strong><br>Causa: Realizar actos de generosidad o caridad sin respeto por la dignidad de la otra persona, ya sea por soberbia, burla o superioridad.<br>Efecto: Se obtiene riqueza material, pero se vive rodeado de personas que no te aman ni te respetan, convirtiendo tu abundancia en soledad y mofa.</p>
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

with open("/Users/fjbanezares/libro del karma/62_dar_con_burla_desprecio/web/index.html", "w") as f:
    f.write(html_content)

print("Chapter 62 HTML successfully updated with all 11 languages.")
