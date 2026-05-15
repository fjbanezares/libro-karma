
import os

# Content for Chapter 59: Living with Honesty and Wisdom
# Title: La Transparencia del Alma / The Transparency of the Soul

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capítulo LIX: El Libro del Karma</title>
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
            <img src="assets/hero.jpg" alt="Karma LIX" id="hero-img">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <div class="chapter-num">
                    <span class="es">CAPÍTULO LIX</span><span class="en">CHAPTER LIX</span><span class="it">CAPITOLO LIX</span><span class="zh">第五十九章</span><span class="ar">الفصل التاسع والخمسون</span><span class="ru">ГЛАВА LIX</span><span class="de">KAPITEL LIX</span><span class="fr">CHAPITRE LIX</span><span class="ja">第59章</span><span class="pt">CAPÍTULO LIX</span><span class="vi">CHƯƠNG LIX</span>
                </div>
                <h1 class="chapter-title">
                    <span class="es">La Transparencia del Alma</span>
                    <span class="en">The Transparency of the Soul</span>
                    <span class="it">La Trasparenza dell'Anima</span>
                    <span class="zh">灵魂的透明度</span>
                    <span class="ar">شفافية الروح</span>
                    <span class="ru">Прозрачность души</span>
                    <span class="de">Die Transparenz der Seele</span>
                    <span class="fr">La Transparence de l'Âme</span>
                    <span class="ja">魂の透明性</span>
                    <span class="pt">A Transparência da Alma</span>
                    <span class="vi">Sự Trong Suốt Của Tâm Hồn</span>
                </h1>
                <p class="subtitle">
                    <span class="es">"La verdad no se busca, se permite; solo el corazón honesto es capaz de ver lo que siempre ha estado allí."</span>
                    <span class="en">"Truth is not sought, it is allowed; only the honest heart is capable of seeing what has always been there."</span>
                    <span class="it">"La verità non si cerca, si permette; solo il cuore onesto è capace di vedere ciò che è sempre stato lì."</span>
                    <span class="zh">“真理不是被寻找的，而是被允许的；唯有诚实的心才能看到一直存在在那里的东西。”</span>
                    <span class="ar">"الحقيقة لا تُطلب، بل تُمنح؛ فقط القلب الصادق هو القادر على رؤية ما كان موجوداً دائماً."</span>
                    <span class="ru">«Истину не ищут, ей позволяют быть; только честное сердце способно увидеть то, что всегда было рядом».</span>
                    <span class="de">„Die Wahrheit wird nicht gesucht, sie wird zugelassen; nur das ehrliche Herz ist in der Lage, das zu sehen, was schon immer da war.“</span>
                    <span class="fr">« La vérité ne se cherche pas, elle se permet ; seul le cœur honnête est capable de voir ce qui a toujours été là. »</span>
                    <span class="ja">「真理は探されるものではなく、許されるものです。誠実な心だけが、常にそこにあったものを見ることができるのです。」</span>
                    <span class="pt">"A verdad não se busca, permite-se; apenas o coração honesto é capaz de ver o que sempre esteve lá."</span>
                    <span class="vi">"Sự thật không phải để tìm kiếm, mà là để cho phép nó hiện diện; chỉ có trái tim chân thật mới có thể nhìn thấy những gì luôn ở đó."</span>
                </p>
                <div class="scroll-indicator"></div>
            </div>
        </section>

        <div class="story-container">
            <!-- ═══ EXPLICACIÓN KÁRMICA ═══ -->
            <div class="story-block fade-in">
                <!-- ES -->
                <p class="es"><span class="drop-cap">L</span>a honestidad no es simplemente el acto de decir la verdad a los demás, sino el compromiso de no mentirse a uno mismo. Cada mentira, por pequeña que sea, actúa como una capa de hollín que se deposita sobre el espejo del alma. Con el tiempo, este hollín se vuelve tan denso que la luz de la sabiduría no puede reflejarse en él. Vivir una vida de engaño es como intentar navegar en una noche de niebla espesa con una brújula rota; el mundo se vuelve confuso, las señales se distorsionan y la verdad se convierte en una amenaza en lugar de un refugio.</p>
                <p class="es">La ley del karma establece que la causa de una vida honesta produce el efecto de una mente clara. Cuando un ser humano elige la integridad sobre la conveniencia, está limpiando su visión interior. La sabiduría no es un conocimiento que se adquiere en los libros, sino la capacidad natural de percibir la realidad tal como es. Solo aquel que no tiene nada que ocultar posee la calma necesaria para observar los misterios del universo. La honestidad disuelve las sombras del miedo y la culpa, dejando espacio para que la intuición pura florezca.</p>
                <p class="es">El "antes" de este karma es una vida envuelta en máscaras, donde la energía se gasta en mantener apariencias y proteger secretos, resultando en una percepción nublada y juicios erróneos. El "después" es la liberación: una transparencia que permite que la luz de la verdad atraviese todo nuestro ser. Al ser honestos, nos alineamos con la frecuencia de la creación, y como recompensa, el universo nos regala la capacidad de ver más allá de las apariencias, otorgándonos la sabiduría que otros buscan desesperadamente en la oscuridad.</p>

                <!-- EN -->
                <p class="en"><span class="drop-cap">H</span>onesty is not simply the act of telling the truth to others, but the commitment to not lying to oneself. Every lie, no matter how small, acts as a layer of soot that settles on the mirror of the soul. Over time, this soot becomes so dense that the light of wisdom cannot reflect in it. Living a life of deception is like trying to navigate on a thick foggy night with a broken compass; the world becomes confusing, signs are distorted, and truth becomes a threat instead of a refuge.</p>
                <p class="en">The law of karma states that the cause of an honest life produces the effect of a clear mind. When a human being chooses integrity over convenience, they are clearing their inner vision. Wisdom is not knowledge acquired in books, but the natural capacity to perceive reality as it is. Only one who has nothing to hide possesses the calm necessary to observe the mysteries of the universe. Honesty dissolves the shadows of fear and guilt, leaving room for pure intuition to flourish.</p>
                <p class="en">The "before" of this karma is a life wrapped in masks, where energy is spent maintaining appearances and protecting secrets, resulting in clouded perception and erroneous judgments. The "after" is liberation: a transparency that allows the light of truth to pierce our entire being. By being honest, we align ourselves with the frequency of creation, and as a reward, the universe gifts us the ability to see beyond appearances, granting us the wisdom that others desperately seek in the darkness.</p>

                <!-- IT -->
                <p class="it"><span class="drop-cap">L</span>'onestà non è semplicemente l'atto di dire la verità agli altri, ma l'impegno a non mentire a se stessi. Ogni bugia, per quanto piccola, agisce come uno strato di fuliggine che si deposita sullo specchio dell'anima. Con il tempo, questa fuliggine diventa così densa che la luce della saggezza non può riflettersi in essa. Vivere una vita di inganno è come navigare in una notte di nebbia fitta con una bussola rotta; il mondo diventa confuso e la verità una minaccia.</p>
                <p class="it">La legge del karma stabilisce che la causa di una vita onesta produce l'effetto di una mente chiara. Quando un essere umano sceglie l'integrità, pulisce la sua visione interiore. La saggezza non è conoscenza acquisita nei libri, ma la capacità naturale di percepire la realtà così com'è. L'onestà dissolve le ombre della paura e della colpa, lasciando spazio alla fioritura dell'intuizione pura.</p>
                <p class="it">Il "prima" di questo karma è una vita avvolta in maschere, con una percezione offuscata. Il "dopo" è la liberazione: una trasparenza che permette alla luce della verità di attraversare tutto il nostro essere. Essendo onesti, ci allineiamo con la creazione e l'universo ci regala la capacità di vedere oltre le apparenze.</p>

                <!-- ZH -->
                <p class="zh"><span class="drop-cap">诚</span>实不仅是对他人说实话，更是对自己不撒谎。每一句谎言，无论多么微小，都像一层灰尘沉积在心灵的镜子上。久而久之，这些灰尘变得如此厚重，以至于智慧之光无法反射。过着欺骗的生活就像在浓雾笼罩的夜晚拿着坏掉的指南针航行；世界变得混乱，真相变成了威胁而非避风港。</p>
                <p class="zh">业力法则指出，诚实生活的因会产生清明心境的果。当一个人选择正直而非便利时，他正在清理内在的视线。智慧不是书本上学到的知识，而是如实感知现实的自然能力。只有问心无愧的人，才拥有观察宇宙奥秘所需的平静。诚实化解了恐惧和内疚的阴影，为纯粹的直觉留出了绽放的空间。</p>
                <p class="zh">这种业力的“前因”是戴着面具生活，导致感知模糊和判断错误。而“后果”则是解脱：一种让真理之光穿透我们整个生命的透明度。通过诚实，我们与创造的频率保持一致，作为奖励，宇宙赋予我们洞察表象的能力，给予我们他人在黑暗中拼命寻找的智慧。</p>

                <!-- AR -->
                <p class="ar"><span class="drop-cap">ا</span>لصدق ليس مجرد قول الحقيقة للآخرين، بل هو الالتزام بعدم الكذب على النفس. كل كذبة، مهما كانت صغيرة، تعمل كطبقة من السخام تتراكم على مرآة الروح. مع مرور الوقت، يصبح هذا السخام كثيفاً لدرجة أن نور الحكمة لا يمكنه الانعكاس فيه. العيش في حياة من الخداع يشبه محاولة الإبحار في ليلة ضبابية كثيفة ببوصلة مكسورة؛ يصبح العالم مربكاً، وتتحول الحقيقة إلى تهديد بدلاً من ملجأ.</p>
                <p class="ar">ينص قانون الكارما على أن سبب الحياة الصادقة ينتج عنه أثر العقل الصافي. عندما يختار الإنسان النزاهة على المصلحة، فإنه ينظف رؤيته الداخلية. الحكمة ليست معرفة تُكتسب من الكتب، بل هي القدرة الطبيعية على إدراك الواقع كما هو. الصدق يذيب ظلال الخوف والذنب، تاركاً مساحة للحدس النقي ليزدهر.</p>
                <p class="ar">"ما قبل" هذه الكارما هي حياة ملفوفة بالأقنعة، مما يؤدي إلى إدراك غائم. أما "ما بعد" فهو التحرر: شفافية تسمح لنور الحقيقة باختراق كياننا بالكامل. بكوننا صادقين، فإننا نتماشى مع تردد الخلق، وكافأة لنا، يمنحنا الكون القدرة على رؤية ما وراء المظاهر، ويمنحنا الحكمة التي يبحث عنها الآخرون بيأس في الظلام.</p>

                <!-- RU -->
                <p class="ru"><span class="drop-cap">Ч</span>естность — это не просто умение говорить правду другим, но обязательство не лгать самому себе. Каждая ложь, какой бы мелкой она ни была, ложится слоем сажи на зеркало души. Со временем эта сажа становится настолько плотной, что свет мудрости не может в ней отразиться. Жизнь в обмане подобна навигации в густом тумане с неисправным компасом: мир становится запутанным, а истина — угрозой, а не убежищем.</p>
                <p class="ru">Закон кармы гласит, что честная жизнь ведет к ясному уму. Когда человек выбирает честность вместо выгоды, он очищает свое внутреннее зрение. Мудрость — это не книжное знание, а естественная способность воспринимать реальность такой, какая она есть. Честность рассеивает тени страха и вины, освобождая место для чистой интуиции.</p>
                <p class="ru">Состояние «до» этой кармы — это жизнь под масками, приводящая к затуманенному восприятию. «После» — это освобождение: прозрачность, позволяющая свету истины пронизывать все наше существо. Будучи честными, мы настраиваемся на частоту творения, и в награду Вселенная дарует нам способность видеть за пределами видимого, открывая мудрость, которую другие тщетно ищут во тьме.</p>

                <!-- DE -->
                <p class="de"><span class="drop-cap">E</span>hrlichkeit ist nicht nur die Tat, anderen die Wahrheit zu sagen, sondern die Verpflichtung, sich selbst nicht zu belügen. Jede Lüge wirkt wie eine Rußschicht auf dem Spiegel der Seele. Mit der Zeit wird dieser Ruß so dicht, dass das Licht der Weisheit nicht mehr reflektiert werden kann. Ein Leben voller Täuschung ist wie das Navigieren in einer nebligen Nacht mit einem kaputten Kompass; die Welt wird verwirrend und die Wahrheit zur Bedrohung statt zum Zufluchtsort.</p>
                <p class="de">Das Gesetz des Karma besagt, dass die Ursache eines ehrlichen Lebens die Wirkung eines klaren Geistes erzeugt. Wenn ein Mensch Integrität wählt, reinigt er seine innere Sicht. Weisheit ist kein Buchwissen, sondern die natürliche Fähigkeit, die Realität so wahrzunehmen, wie sie ist. Ehrlichkeit löst die Schatten von Angst und Schuld auf und schafft Raum für reine Intuition.</p>
                <p class="de">Das „Vorher“ dieses Karmas ist ein Leben in Masken, das zu getrübter Wahrnehmung führt. Das „Nachher“ ist Befreiung: eine Transparenz, die das Licht der Wahrheit durch unser gesamtes Wesen scheinen lässt. Indem wir ehrlich sind, richten wir uns nach der Schöpfung aus, und das Universum schenkt uns die Fähigkeit, hinter die Fassaden zu blicken.</p>

                <!-- FR -->
                <p class="fr"><span class="drop-cap">L</span>'honnêteté n'est pas simplement l'acte de dire la vérité aux autres, mais l'engagement de ne pas se mentir à soi-même. Chaque mensonge agit comme une couche de suie sur le miroir de l'âme. Avec le temps, cette suie devient si dense que la lumière de la sagesse ne peut s'y refléter. Vivre une vie de tromperie, c'est comme naviguer par une nuit de brouillard épais avec une boussole cassée ; le monde devient confus et la vérité une menace au lieu d'un refuge.</p>
                <p class="fr">La loi du karma stipule que la cause d'une vie honnête produit l'effet d'un esprit clair. Quand un être humain choisit l'intégrité, il nettoie sa vision intérieure. La sagesse n'est pas une connaissance livresque, mais la capacité naturelle de percevoir la réalité telle qu'elle est. L'honnêteté dissout les ombres de la peur et de la culpabilité, laissant place à l'intuition pure.</p>
                <p class="fr">Le « avant » de ce karma est une vie enveloppée de masques, entraînant une perception trouble. Le « après » est la libération : une transparence qui permet à la lumière de la vérité de traverser tout notre être. En étant honnêtes, nous nous alignons sur la création, et l'univers nous offre la capacité de voir au-delà des apparences.</p>

                <!-- JA -->
                <p class="ja"><span class="drop-cap">正</span>直さとは、単に他人に真実を話すことではなく、自分自身に嘘をつかないという誓いです。どんなに小さな嘘でも、魂の鏡に降り積もる煤（すす）のように作用します。時が経つにつれ、この煤は非常に厚くなり、知恵の光が反射できなくなります。欺瞞に満ちた人生を送ることは、壊れたコンパスを持って濃霧の夜を航海するようなものです。世界は混乱し、真実は救いではなく脅威となります。</p>
                <p class="ja">カルマの法則は、正直な人生という原因が、澄んだ心という結果をもたらすと説いています。人間が利便性よりも誠実さを選ぶとき、内なる視界は清められます。知恵とは本から得る知識ではなく、現実をありのままに認識する自然な能力です。正直さは恐れと罪悪感の影を消し去り、純粋な直感が花開く空間を作ります。</p>
                <p class="ja">このカルマの「前」は、仮面に包まれた人生であり、知覚を曇らせます。「後」は解放です。真実の光が私たちの全存在を突き抜ける透明性です。正直であることで、私たちは創造の周波数と同調し、報酬として、宇宙は私たちに外見を超えて見る力を与え、他の人々が暗闇の中で必死に探している知恵を授けてくれるのです。</p>

                <!-- PT -->
                <p class="pt"><span class="drop-cap">A</span> honestidade não é simplesmente o ato de dizer a verdade aos outros, mas o compromisso de não mentir a si mesmo. Cada mentira atua como uma camada de fuligem no espelho da alma. Com o tempo, essa fuligem torna-se tão densa que a luz da sabedoria não se pode refletir. Viver uma vida de engano é como navegar numa noite de nevoeiro espesso com uma bússola partida; o mundo torna-se confuso e a verdade uma ameaça em vez de um refúgio.</p>
                <p class="pt">A lei do karma estabelece que a causa de uma vida honesta produz o efeito de uma mente clara. Quando um ser humano escolhe a integridade, está a limpar a sua visão interior. A sabedoria não é conhecimento de livros, mas a capacidade natural de perceber a realidade como ela é. A honestidade dissolve as sombras do medo e da culpa, deixando espaço para a intuição pura florescer.</p>
                <p class="pt">O "antes" deste karma é uma vida envolta em máscaras, resultando numa perceção turva. O "depois" é a libertação: uma transparência que permite que a luz da verdade atravesse todo o nosso ser. Ao sermos honestos, alinhamo-nos com a criação e o universo presenteia-nos com a sabedoria que outros buscam desesperadamente na escuridão.</p>

                <!-- VI -->
                <p class="vi"><span class="drop-cap">L</span>òng chân thật không chỉ đơn thuần là việc nói sự thật với người khác, mà là lời cam kết không tự lừa dối chính mình. Mỗi lời nói dối, dù nhỏ đến đâu, cũng giống như một lớp nhọ nồi bám lên tấm gương tâm hồn. Theo thời gian, lớp nhọ này trở nên dày đặc đến mức ánh sáng trí tuệ không thể phản chiếu được nữa. Sống một cuộc đời lừa dối giống như cố gắng chèo lái trong đêm sương mù dày đặc với một chiếc la bàn hỏng; thế giới trở nên hỗn loạn, và sự thật trở thành một mối đe dọa thay vì là nơi trú ẩn.</p>
                <p class="vi">Luật nhân quả quy định rằng nhân sống chân thật sẽ trổ ra quả là một tâm trí sáng suốt. Khi một con người chọn sự chính trực thay vì sự tiện lợi, họ đang làm sạch tầm nhìn nội tâm của mình. Trí tuệ không phải là kiến thức thu lượm từ sách vở, mà là khả năng tự nhiên cảm nhận thực tại đúng như nó đang là. Lòng chân thật làm tan biến những bóng ma sợ hãi và tội lỗi, nhường chỗ cho trực giác thuần khiết nảy nở.</p>
                <p class="vi">"Trước khi" có nghiệp này là một cuộc đời bao phủ trong những chiếc mặt nạ, dẫn đến nhận thức mờ mịt. "Sau khi" là sự giải thoát: một sự trong suốt cho phép ánh sáng sự thật xuyên thấu toàn bộ con người chúng ta. Bằng cách sống chân thật, chúng ta hòa nhịp với tần số của tạo hóa, và như một phần thưởng, vũ trụ ban tặng cho chúng ta khả năng nhìn thấu những biểu hiện bên ngoài, ban cho chúng ta trí tuệ mà những người khác đang tuyệt vọng tìm kiếm trong bóng tối.</p>
            </div>

            <!-- ═══ PARÁBOLA ═══ -->
            <div class="story-block parable-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">
                <h3 class="es" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">El Espejo del Valle Silencioso</h3>
                <h3 class="en" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">The Mirror of the Silent Valley</h3>
                <h3 class="it" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Lo Specchio della Valle Silenziosa</h3>
                <h3 class="zh" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">寂静谷的镜子</h3>
                <h3 class="ar" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">مرآة الوادي الصامت</h3>
                <h3 class="ru" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Зеркало Тихой Долины</h3>
                <h3 class="de" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Der Spiegel des Stillen Tales</h3>
                <h3 class="fr" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Le Miroir de la Vallée Silencieuse</h3>
                <h3 class="ja" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">沈黙の谷の鏡</h3>
                <h3 class="pt" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">O Espelho do Vale Silencioso</h3>
                <h3 class="vi" style="color: var(--gold); text-align: center; font-family: 'Cinzel', serif; margin-bottom: 2rem;">Chiếc Gương Của Thung Lũng Tĩnh Lặng</h3>

                <!-- ES -->
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Había una vez un hombre llamado Elian que vivía en una ciudad de espejos deformados. Elian era famoso por su astucia; sabía decir lo que cada persona quería escuchar, incluso si era falso. Gracias a sus mentiras, acumuló grandes riquezas y prestigio. Sin embargo, con el paso de los años, algo extraño comenzó a suceder: Elian empezó a ver el mundo borroso. Los rostros de sus amigos parecían sombras, y el sol mismo parecía una mancha opaca en el cielo. Consultó a médicos y sabios, pero ninguno encontró cura para su ceguera progresiva.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Un día, desesperado, viajó al Valle Silencioso para ver a un anciano eremita que, según decían, podía ver a través de las montañas. Al llegar, Elian le suplicó: "Sabio, devuélveme la vista. El mundo se ha vuelto gris y confuso". El anciano, sin abrir los ojos, le entregó un pequeño cuenco de agua clara y le dijo: "El mundo no está gris, Elian. Tus ojos están cubiertos por el humo de tus propias palabras. Cada vez que engañaste a otro, pusiste un velo sobre tu propio espíritu. Para ver la verdad afuera, primero debes dejar de esconderla adentro".</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Elian pasó meses en el valle, practicando el silencio y, sobre todo, la verdad. Confesó sus engaños, devolvió lo que obtuvo con falsedades y aprendió a hablar con el corazón desnudo. Fue un proceso doloroso, como si le arrancaran costras de los ojos. Un día, al amanecer, vio una gota de rocío sobre una hoja de loto. Era tan perfecta y clara que rompió a llorar. En ese momento, no solo recuperó la vista, sino que empezó a ver la esencia de todas las cosas: el amor en los extraños, la sabiduría en el viento y la divinidad en el silencio.</p>
                <p class="es" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Regresó a su ciudad, pero ya no era un mercader de mentiras, sino un faro de verdad. Quienes lo miraban sentían que sus propias sombras se disolvían. Elian comprendió que la honestidad no era una carga moral, sino el precio de la libertad absoluta. Su Ikigai, su propósito, se volvió claro como el cristal: ayudar a otros a limpiar sus propios espejos para que pudieran ver la belleza infinita que la mentira siempre les había ocultado.</p>

                <!-- EN -->
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Once there was a man named Elian who lived in a city of distorted mirrors. Elian was famous for his cunning; he knew how to say what each person wanted to hear, even if it was false. Thanks to his lies, he accumulated great wealth and prestige. However, over the years, something strange began to happen: Elian started to see the world as a blur. His friends' faces looked like shadows, and the sun itself looked like an opaque spot in the sky. He consulted doctors and sages, but none found a cure for his progressive blindness.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">One day, in despair, he traveled to the Silent Valley to see an old hermit who was said to be able to see through mountains. Upon arrival, Elian begged: "Wise one, restore my sight. The world has turned gray and confusing." The old man, without opening his eyes, handed him a small bowl of clear water and said: "The world is not gray, Elian. Your eyes are covered by the smoke of your own words. Every time you deceived another, you placed a veil over your own spirit. To see the truth outside, you must first stop hiding it inside."</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Elian spent months in the valley, practicing silence and, above all, truth. He confessed his deceptions, returned what he obtained with falsehoods, and learned to speak with a naked heart. It was a painful process, as if scabs were being torn from his eyes. One day at dawn, he saw a drop of dew on a lotus leaf. It was so perfect and clear that he burst into tears. At that moment, he not only regained his sight but began to see the essence of all things: the love in strangers, the wisdom in the wind, and the divinity in the silence.</p>
                <p class="en" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">He returned to his city, but he was no longer a merchant of lies, but a beacon of truth. Those who looked at him felt their own shadows dissolve. Elian understood that honesty was not a moral burden, but the price of absolute freedom. His Ikigai, his purpose, became crystal clear: to help others clean their own mirrors so they could see the infinite beauty that lies had always hidden from them.</p>

                <!-- IT -->
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">C'era una volta un uomo di nome Elian che viveva in una città di specchi deformati. Elian era famoso per la sua astuzia; sapeva dire ciò che ogni persona voleva sentire. Grazie alle sue bugie, accumulò grandi ricchezze. Tuttavia, con il passare degli anni, Elian iniziò a vedere il mondo sfocato. I volti degli amici sembravano ombre e il sole una macchia opaca. Nessun medico trovò una cura per la sua cecità progressiva.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Disperato, viaggiò nella Valle Silenziosa per vedere un vecchio eremita. Elian supplicò: "Saggio, restituiscimi la vista". L'anziano gli porse una ciotola d'acqua chiara e disse: "Il mondo non è grigio, Elian. I tuoi occhi sono coperti dal fumo delle tue stesse parole. Ogni volta che hai ingannato un altro, hai posto un velo sul tuo spirito. Per vedere la verità fuori, devi smettere di nasconderla dentro".</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Elian passò mesi nella valle, praticando il silenzio e la verità. Confessò i suoi inganni e imparò a parlare con il cuore nudo. Un giorno, all'alba, vide una goccia di rugiada su una foglia di loto. Era così perfetta che scoppiò a piangere. In quel momento, recuperò la vista e iniziò a vedere l'essenza di tutte le cose: l'amore negli estranei e la saggezza nel vento.</p>
                <p class="it" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Tornò nella sua città come un faro di verità. Chi lo guardava sentiva le proprie ombre dissolversi. Elian capì che l'onestà non era un peso, ma il prezzo della libertà assoluta. Il suo scopo divenne chiaro: aiutare gli altri a pulire i propri specchi per vedere la bellezza infinita che la menzogna aveva loro nascosto.</p>

                <!-- ZH -->
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">从前有一个叫埃连的人，住在一个充满扭曲镜子的城市里。埃连以狡黠闻名；他知道如何说出每个人想听的话。凭借谎言，他积累了巨大的财富。然而，随着岁月的流逝，埃连开始看世界变得模糊。朋友们的脸看起来像影子，太阳本身也像天空中的一块模糊光斑。他咨询了医生和智者，但没有人能治好他的渐进性失明。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">绝望中，他前往寂静谷拜访一位隐士。埃连哀求道：“智者，请恢复我的视力。世界变得灰暗混乱。”老人递给他一小碗清澈的水说：“世界并不灰暗，埃连。你的眼睛被你自己的谎言之烟覆盖了。每当你欺骗别人，你就给自己的灵魂蒙上了一层纱。要看清外面的真相，你必须先停止在内心隐藏真相。”</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">埃连在山谷里待了几个月，练习沉默，尤其是练习真实。他坦白了自己的欺骗，学会了赤诚相待。一天清晨，他看到莲叶上的一滴露珠。它是如此完美清澈，他不禁流下泪来。那一刻，他不仅恢复了视力，还开始看到了万物的本质：陌生人中的爱，风中的智慧，以及沉默中的神性。</p>
                <p class="zh" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">他回到了城市，不再是一个谎言贩子，而是一座真理的灯塔。看着他的人都感觉到自己的阴影在消散。埃连明白，诚实不是道德负担，而是绝对自由的代价。他的生命意义变得晶莹剔透：帮助他人清理自己的镜子，让他们能看到谎言一直遮蔽的无限美景。</p>

                <!-- AR -->
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">كان يا مكان، كان هناك رجل يدعى إليان يعيش في مدينة من المرايا المشوهة. اشتهر إليان بدهائه؛ فقد كان يعرف كيف يقول ما يريد كل شخص سماعه. بفضل أكاذيبه، جمع ثروة طائلة. ومع ذلك، مع مرور السنين، بدأ إليان يرى العالم ضبابياً. بدت وجوه أصدقائه كظلال، والشمس نفسها بدت كبقعة معتمة في السماء. استشار الأطباء والحكماء، لكن لم يجد أحد علاجاً لعمى بصره التدريجي.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">في يأس، سافر إلى الوادي الصامت لرؤية ناسك عجوز. توسل إليان: "أيها الحكيم، أعد لي بصري". قدم له العجوز وعاءً صغيراً من الماء الصافي وقال: "العالم ليس رمادياً يا إليان. عيناك مغطاة بدخان كلماتك. في كل مرة خدعت فيها أحداً، وضعت حجاباً على روحك. لرؤية الحقيقة في الخارج، يجب عليك أولاً التوقف عن إخفائها في الداخل".</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">قضى إليان شهوراً في الوادي، ممارساً الصمت، والأهم من ذلك، الصدق. اعترف بخداعه، وتعلم التحدث بقلب عارٍ. في أحد الأيام عند الفجر، رأى قطرة ندى على ورقة لوتس. كانت مثالية وصافية لدرجة أنه بكى. في تلك اللحظة، لم يستعد بصره فحسب، بل بدأ يرى جوهر كل الأشياء: الحب في الغرباء، والحكمة في الريح.</p>
                <p class="ar" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">عاد إلى مدينته، ولم يعد تاجراً للأكاذيب، بل منارة للحقيقة. شعر من ينظر إليه أن ظلالهم تذوب. فهم إليان أن الصدق لم يكن عبئاً أخلاقياً، بل ثمن الحرية المطلقة. أصبح غرضه واضحاً ك الكريستال: مساعدة الآخرين على تنظيف مراياهم الخاصة ليروا الجمال اللامتناهي الذي أخفاه الكذب عنهم دائماً.</p>

                <!-- RU -->
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Давным-давно жил человек по имени Элиан в городе искаженных зеркал. Элиан славился своей хитростью: он умел говорить то, что каждый хотел услышать. Благодаря своей лжи он накопил огромные богатства. Однако с годами мир для Элиана начал тускнеть. Лица друзей казались тенями, а само солнце — мутным пятном. Ни один лекарь не мог найти исцеление от его прогрессирующей слепоты.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">В отчаянии он отправился в Тихую Долину к старому отшельнику. Элиан умолял: «Мудрец, верни мне зрение». Старик протянул ему чашу с чистой водой и сказал: «Мир не серый, Элиан. Твои глаза застланы дымом твоих собственных слов. Каждый раз, когда ты обманывал, ты набрасывал вуаль на свой дух. Чтобы увидеть правду снаружи, нужно перестать прятать ее внутри».</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Элиан провел месяцы в долине, практикуя тишину и честность. Он признался в своих обманах и научился говорить от чистого сердца. Однажды на рассвете он увидел каплю росы на листе лотоса. Она была настолько прозрачной, что он заплакал. В тот миг он не только прозрел, но и начал видеть суть вещей: любовь в незнакомцах и мудрость в шуме ветра.</p>
                <p class="ru" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Он вернулся в город не торговцем ложью, а маяком истины. Те, кто смотрел на него, чувствовали, как исчезают их собственные тени. Элиан понял, что честность — это не бремя, а цена абсолютной свободы. Его цель стала ясной как кристалл: помогать другим очищать их зеркала, чтобы они могли увидеть бесконечную красоту, которую всегда скрывала ложь.</p>

                <!-- DE -->
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Es war einmal ein Mann namens Elian, der in einer Stadt voller verzerrter Spiegel lebte. Elian war berühmt für seine List; er wusste genau, was die Leute hören wollten. Durch seine Lügen häufte er großen Reichtum an. Doch im Laufe der Jahre geschah etwas Seltsames: Elian begann, die Welt nur noch verschwommen wahrzunehmen. Die Gesichter seiner Freunde erschienen wie Schatten. Kein Arzt fand eine Heilung für seine fortschreitende Erblindung.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Verzweifelt reiste er in das Stille Tal zu einem alten Eremiten. Elian flehte: „Weiser, gib mir mein Augenlicht zurück.“ Der Alte reichte ihm eine Schale mit klarem Wasser und sagte: „Die Welt ist nicht grau, Elian. Deine Augen sind vom Rauch deiner eigenen Worte bedeckt. Jedes Mal, wenn du jemanden getäuscht hast, hast du einen Schleier über deinen Geist gelegt. Um die Wahrheit draußen zu sehen, musst du aufhören, sie drinnen zu verstecken.“</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Elian verbrachte Monate im Tal und übte sich in Stille und Wahrheit. Er gestand seine Täuschungen und lernte, mit offenem Herzen zu sprechen. Eines Tages sah er einen Tautropfen auf einem Lotusblatt. Er war so klar, dass er in Tränen ausbrach. In diesem Moment erlangte er nicht nur sein Augenlicht zurück, sondern begann, das Wesen aller Dinge zu sehen: die Liebe in Fremden und die Weisheit im Wind.</p>
                <p class="de" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Er kehrte als Leuchtturm der Wahrheit in seine Stadt zurück. Wer ihn ansah, spürte, wie sich die eigenen Schatten auflösten. Elian begriff, dass Ehrlichkeit keine moralische Last war, sondern der Preis für absolute Freiheit. Seine Bestimmung wurde kristallklar: anderen zu helfen, ihre eigenen Spiegel zu reinigen, damit sie die unendliche Schönheit sehen konnten, die die Lüge vor ihnen verborgen hatte.</p>

                <!-- FR -->
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Il était une fois un homme nommé Elian qui vivait dans une ville de miroirs déformés. Elian était célèbre pour sa ruse ; il savait dire ce que chaque personne voulait entendre. Grâce à ses mensonges, il accumula de grandes richesses. Cependant, au fil des ans, Elian commença à voir le monde flou. Les visages de ses amis semblaient être des ombres et le soleil une tache opaque. Aucun médecin ne trouva de remède à sa cécité progressive.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Désespéré, il se rendit dans la Vallée Silencieuse pour voir un vieil ermite. Elian supplia : « Sage, rends-moi la vue. » Le vieillard lui tendit un bol d'eau claire et dit : « Le monde n'est pas gris, Elian. Tes yeux sont couverts par la fumée de tes propres paroles. Chaque fois que tu as trompé autrui, tu as posé un voile sur ton esprit. Pour voir la vérité à l'extérieur, tu dois d'abord cesser de la cacher à l'intérieur. »</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Elian passa des mois dans la vallée, pratiquant le silence et la vérité. Il confessa ses tromperies et apprit à parler avec un cœur nu. Un jour, à l'aube, il vit une goutte de rosée sur une feuille de lotus. Elle était si pure qu'il éclata en sanglots. À cet instant, il retrouva la vue et commença à voir l'essence de toutes choses : l'amour chez les inconnus et la sagesse dans le vent.</p>
                <p class="fr" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Il retourna dans sa ville comme un phare de vérité. Ceux qui le regardaient sentaient leurs propres ombres se dissoudre. Elian comprit que l'honnêteté n'était pas un fardeau, mais le prix de la liberté absolue. Son but devint clair : aider les autres à nettoyer leurs propres miroirs pour voir la beauté infinie que le mensonge leur avait cachée.</p>

                <!-- JA -->
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">昔、歪んだ鏡の街にエリアンという男が住んでいました。エリアンはその抜け目なさで有名でした。彼は他人が聞きたがっている言葉を、たとえそれが嘘であっても、巧みに操ることができました。その嘘のおかげで、彼は莫大な富と名声を築きました。しかし、年月が経つにつれ、奇妙なことが起こり始めました。エリアンの目には世界がぼやけて見えるようになったのです。友人の顔は影のように見え、太陽さえも空に浮かぶ濁った斑点のように見えました。彼は医者や賢者に相談しましたが、その進行性の盲目を治せる者は誰もいませんでした。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">絶望した彼は、山をも見通すという沈黙の谷の老隠者に会いに行きました。エリアンは嘆願しました。「賢者よ、私の視力を取り戻してください。世界が灰色で混乱に満ちて見えるのです」。老人は目を開けることなく、澄んだ水の入った小さな鉢を差し出し、こう言いました。「世界が灰色なのではない、エリアン。お前の目は、お前自身の言葉が吐き出す煙に覆われているのだ。他人を欺くたびに、お前は自らの霊魂にベールをかけてきた。外の真理を見るためには、まず内の真実を隠すのをやめなければならない」。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">エリアンは谷で数ヶ月を過ごし、沈黙を、そして何よりも真実を語る修行をしました。自らの欺瞞を告白し、偽りで得たものを返し、ありのままの心で語ることを学びました。それは、目からかさぶたを剥ぎ取るような痛みを伴う過程でした。ある日の夜明け、彼は蓮の葉の上の露のしずくを見ました。それはあまりに完璧で澄んでいて、彼は涙を流しました。その瞬間、彼は視力を取り戻しただけでなく、万物の本質が見えるようになりました。見知らぬ人の中にある愛、風の中にある知恵、そして沈黙の中にある神性を。</p>
                <p class="ja" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">彼は自分の街に戻りましたが、もはや嘘の商人ではなく、真理の灯台となっていました。彼を見る人々は、自分たちの影が消えていくのを感じました。エリアンは、正直さは道徳的な重荷ではなく、絶対的な自由の代価であることを悟りました。彼の「生きがい」は水晶のように明快になりました。他人が自らの鏡を清めるのを助け、嘘が常に隠してきた無限の美しさを見せてあげることだったのです。</p>

                <!-- PT -->
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Era uma vez um homem chamado Elian que vivia numa cidade de espelhos deformados. Elian era famoso pela sua astúcia; sabia dizer o que cada pessoa queria ouvir. Graças às suas mentiras, acumulou grandes riquezas. No entanto, com o passar dos anos, Elian começou a ver o mundo baço. Os rostos dos amigos pareciam sombras e o sol uma mancha opaca. Nenhum médico encontrou cura para a sua cegueira progressiva.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Desesperado, viajou para o Vale Silencioso para ver um velho eremita. Elian suplicou: "Sábio, devolve-me a vista". O ancião entregou-lhe uma taça de água límpida e disse: "O mundo não está cinzento, Elian. Os teus olhos estão cobertos pelo fumo das tuas próprias palavras. Para veres a verdade fora, tens primeiro de parar de a esconder dentro".</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Elian passou meses no vale, praticando o silêncio e a verdade. Confessou os seus enganos e aprendeu a falar com o coração nu. Um dia, ao amanhecer, viu uma gota de orvalho numa folha de lótus. Era tão perfeita que rompeu a chorar. Nesse momento, recuperou a vista e começou a ver a essência de todas as coisas: o amor nos estranhos e a sabedoria no vento.</p>
                <p class="pt" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Regressou à sua cidade como um farol de verdade. Quem o olhava sentia as suas próprias sombras dissolverem-se. Elian compreendeu que a honestidade não era um fardo, mas o preço da liberdade absoluta. O seu propósito tornou-se claro: ajudar os outros a limpar os seus espelhos para verem a beleza infinita que a mentira lhes tinha ocultado.</p>

                <!-- VI -->
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Ngày xửa ngày xưa, có một người đàn ông tên là Elian sống trong một thành phố của những chiếc gương biến dạng. Elian nổi tiếng với sự xảo quyệt; anh ta biết nói những gì mỗi người muốn nghe, ngay cả khi điều đó là giả dối. Nhờ những lời nói dối, anh ta đã tích lũy được khối tài sản kếch xù. Tuy nhiên, năm tháng trôi qua, một điều kỳ lạ bắt đầu xảy ra: Elian bắt đầu nhìn thế giới mờ ảo. Khuôn mặt của bạn bè anh trông như những bóng ma, và mặt trời trông như một vệt mờ đục trên bầu trời. Anh đã tham khảo ý kiến của các bác sĩ và nhà thông thái, nhưng không ai tìm ra cách chữa trị cho chứng mù lòa tiến triển của mình.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Trong tuyệt vọng, anh tìm đến Thung lũng Tĩnh lặng để gặp một vị ẩn sĩ già. Elian cầu xin: "Thưa bậc trí giả, xin hãy trả lại thị lực cho con. Thế giới đã trở nên xám xịt và hỗn loạn." Vị trưởng lão không mở mắt, đưa cho anh một bát nước trong và nói: "Thế giới không xám xịt đâu Elian. Đôi mắt con đã bị bao phủ bởi làn khói từ chính những lời nói của con. Mỗi khi con lừa dối người khác, con đã phủ một bức màn lên linh hồn mình. Để nhìn thấy sự thật bên ngoài, trước tiên con phải ngừng che giấu nó bên trong."</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Elian đã dành nhiều tháng trong thung lũng, thực hành sự tĩnh lặng và trên hết là sự thật. Anh thú nhận những trò lừa dối của mình, trả lại những gì có được bằng sự giả dối và học cách nói bằng một trái tim trần trụi. Đó là một quá trình đau đớn, giống như bị bóc từng lớp vảy ra khỏi mắt. Một ngày nọ, vào lúc bình minh, anh nhìn thấy một giọt sương trên lá sen. Nó hoàn hảo và trong trẻo đến mức anh bật khóc. Ngay lúc đó, anh không chỉ lấy lại được thị lực mà còn bắt đầu nhìn thấu bản chất của vạn vật: tình yêu trong những người xa lạ, trí tuệ trong cơn gió và sự thiêng liêng trong tĩnh lặng.</p>
                <p class="vi" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">Anh trở lại thành phố của mình, nhưng không còn là một kẻ buôn bán những lời dối trá, mà là một ngọn hải đăng của sự thật. Những ai nhìn vào anh đều cảm thấy bóng tối của chính họ tan biến. Elian hiểu rằng sự chân thật không phải là một gánh nặng đạo đức, mà là cái giá của sự tự do tuyệt đối. Lẽ sống (Ikigai) của anh trở nên rõ ràng như pha lê: giúp người khác lau sạch tấm gương của chính họ để họ có thể nhìn thấy vẻ đẹp vô tận mà những lời nói dối bấy lâu nay đã che giấu.</p>
            </div>

            <!-- ═══ ART ═══ -->
            <div class="final-art fade-in" style="text-align: center; margin-top: 4rem; margin-bottom: 2rem;">
                <img src="assets/art.jpg" alt="Obra de Arte Karma LIX" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            </div>

            <!-- ═══ MORAL ═══ -->
            <div class="moral fade-in">
                <span class="es">La honestidad es el cristal que limpia la visión; quien miente al mundo, termina por no ver la luz de su propio camino.</span>
                <span class="en">Honesty is the crystal that clears the vision; he who lies to the world ends up not seeing the light of his own path.</span>
                <span class="it">L'onestà è il cristallo che pulisce la visione; chi mente al mondo, finisce per non vedere la luce del proprio cammino.</span>
                <span class="zh">诚实是清理视野的晶体；向世界撒谎的人，最终会看不见自己道路上的光。</span>
                <span class="ar">الصدق هو الكريستال الذي ينظف الرؤية؛ من يكذب على العالم ينتهي به المطاف بعدم رؤية النور في طريقه.</span>
                <span class="ru">Честность — это кристалл, очищающий зрение; тот, кто лжет миру, в конце концов перестает видеть свет собственного пути.</span>
                <span class="de">Ehrlichkeit ist das Kristall, das die Sicht reinigt; wer die Welt belügt, sieht am Ende das Licht seines eigenen Weges nicht mehr.</span>
                <span class="fr">L'honnêteté est le cristal qui nettoie la vision ; celui qui ment au monde finit par ne plus voir la lumière de son propre chemin.</span>
                <span class="ja">正直さは視界を清める水晶です。世界に嘘をつく者は、やがて自らの道の光さえも見失うことになります。</span>
                <span class="pt">A honestidade é o cristal que limpa a visão; quem mente ao mundo, acaba por não ver a luz do seu próprio caminho.</span>
                <span class="vi">Lòng chân thật là viên pha lê gột rửa tầm nhìn; kẻ lừa dối thế gian rốt cuộc sẽ không thể nhìn thấy ánh sáng trên con đường của chính mình.</span>
            </div>

            <center class="fade-in" style="margin-top: 4rem;">
                <img src="assets/hero.jpg" alt="Karma LIX Full" style="max-width: 600px; width: 100%; border-radius: 8px; border: 1px solid rgba(197,160,89,0.3); box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
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
                        <strong>🇻🇳 Tiếng Việt:</strong><br>Nhân: Sống chân thật.<br>Quả: Có trí tuệ biết được sự thật.
                    </p>
                    <p style="color: #ddd; margin-bottom: 1.5rem;"><strong>🇬🇧 English:</strong><br>Cause: Living an honest life.<br>Effect: Brings wisdom to see the truth.</p>
                    <p class="es" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197,160,89,0.1); padding: 1rem; border-left: 3px solid var(--gold);"><strong>Traducción Recreada:</strong><br>Causa: Vivir una vida de absoluta honestidad e integridad.<br>Efecto: Se obtiene la sabiduría suprema para ver la verdad oculta tras las ilusiones del mundo.</p>
                </div>
            </div>

            <div class="linktree-subtle fade-in" style="margin-top: 6rem; padding: 3rem 0; border-top: 1px solid rgba(197,160,89,0.2); text-align: center;">
                <p class="es" style="color: #999; font-style: italic; margin-bottom: 1.5rem;">Si quieres conocer más sobre el proyecto o colaborar, accede a nuestro <a href="../../linktree.html" style="color: var(--gold); text-decoration: none; border-bottom: 1px dotted var(--gold);">Linktree</a>.</p>
            </div>
        </div>
    </main>

    <script src="../../shared/script.js"></script>
</body>
</html>"""

with open("/Users/fjbanezares/libro del karma/59_vivir_con_honestidad_sabiduria/web/index.html", "w") as f:
    f.write(html_content)

print("Chapter 59 HTML successfully updated with all 11 languages and new styling.")
