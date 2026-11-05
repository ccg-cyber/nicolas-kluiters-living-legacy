#!/usr/bin/env python3
"""Build the multilingual, dependency-free static memorial site."""
from pathlib import Path
from html import escape
from datetime import date

ROOT = Path(__file__).resolve().parent
BASE = "https://ccg-cyber.github.io/nicolas-kluiters-living-legacy"
UPDATED = "2026-11-05"
LOCALES = ("ar", "en", "fr")
PAGES = ("index", "life", "barqa", "timeline", "cause", "places", "archive", "sources")

TEXT = {
    "ar": {
        "langname": "العربية", "site": "الأب نيكولا كلويترز",
        "tagline": "يسوعي · برقا والبقاع · 1940–1985",
        "nav": ["الرئيسية", "السيرة", "برقا والعمل", "الخط الزمني", "دعوى التطويب", "أماكن الذاكرة", "الأرشيف المصوّر", "المصادر"],
        "skip": "انتقل إلى المحتوى", "menu": "التنقّل", "home": "الرئيسية",
        "footer_note": "أرشيف مستقل للتوثيق والذاكرة، وليس موقعًا رسميًا لليسوعيين أو لدعوى التطويب.",
        "updated": "آخر مراجعة للمصادر: 5 تشرين الثاني 2026",
        "source_label": "المصدر", "photo_label": "الصورة", "open_image": "عرض الصورة الأصلية",
        "source_note": "ملاحظات التوثيق وحقوق الصور", "external": "يفتح في نافذة جديدة",
        "map_barqa": "افتح بحث الخرائط عن مركز برقا", "map_taanayel": "افتح بحث الخرائط عن دير تعنايل",
    },
    "en": {
        "langname": "English", "site": "Father Nicolas Kluiters",
        "tagline": "Jesuit · Barqa & the Bekaa · 1940–1985",
        "nav": ["Home", "Life", "Barqa & work", "Timeline", "The cause", "Places of memory", "Photo archive", "Sources"],
        "skip": "Skip to content", "menu": "Explore", "home": "Home",
        "footer_note": "An independent historical archive. Not an official Jesuit or beatification-cause website.",
        "updated": "Sources last reviewed: 5 November 2026",
        "source_label": "Source", "photo_label": "Photograph", "open_image": "Open source image",
        "source_note": "Research and image-rights notes", "external": "Opens in a new tab",
        "map_barqa": "Open map search for the Barqa centre", "map_taanayel": "Open map search for Deir Taanayel",
    },
    "fr": {
        "langname": "Français", "site": "Père Nicolas Kluiters",
        "tagline": "Jésuite · Barqa et la Békaa · 1940–1985",
        "nav": ["Accueil", "Biographie", "Barqa et son œuvre", "Chronologie", "La cause", "Lieux de mémoire", "Photographies", "Sources"],
        "skip": "Aller au contenu", "menu": "Explorer", "home": "Accueil",
        "footer_note": "Archives historiques indépendantes. Site non officiel de la Compagnie de Jésus ou de la cause de béatification.",
        "updated": "Sources revues le 5 novembre 2026",
        "source_label": "Source", "photo_label": "Photographie", "open_image": "Voir l’image source",
        "source_note": "Notes de recherche et droits des images", "external": "S’ouvre dans un nouvel onglet",
        "map_barqa": "Rechercher le centre de Barqa sur une carte", "map_taanayel": "Rechercher Deir Taanayel sur une carte",
    },
}

NAV = dict(zip(LOCALES, [
    ["الرئيسية", "السيرة", "برقا والعمل", "الخط الزمني", "دعوى التطويب", "أماكن الذاكرة", "الأرشيف المصوّر", "المصادر"],
    ["Home", "Biography", "Barqa & its work", "Timeline", "The cause", "Places of memory", "Photo archive", "Sources"],
    ["Accueil", "Biographie", "Barqa et son œuvre", "Chronologie", "La cause", "Lieux de mémoire", "Photographies", "Sources"],
]))

SLUGS = {
    "index": ["index", "index", "index"],
    "life": ["life", "life", "life"],
    "barqa": ["barqa", "barqa", "barqa"],
    "timeline": ["timeline", "timeline", "timeline"],
    "cause": ["cause", "cause", "cause"],
    "places": ["places", "places", "places"],
    "archive": ["archive", "archive", "archive"],
    "sources": ["sources", "sources", "sources"],
}

CONTENT = {
    "ar": {
        "index": {
            "title": "حياة من الإيمان والخدمة في البقاع",
            "eyebrow": "سيرة موثّقة · ذاكرة برقا الحيّة",
            "summary": "كان الأب نيكولا كلويترز يسوعيًا هولنديًا، وفنانًا قبل الكهنوت، خدم قرى البقاع الشمالي في سنوات الحرب. يجمع هذا الأرشيف ما أمكن توثيقه عن حياته، وأثره العملي، والذاكرة التي ما زالت حيّة في برقا.",
            "body": """
<section class='feature-grid'>
  <a class='feature-card' href='life.html'><span class='card-number'>01</span><h2>الرجل والدعوة</h2><p>من دلفت في هولندا إلى التكوين اليسوعي والكهنوت والخدمة في لبنان.</p><span class='text-link'>اقرأ السيرة ←</span></a>
  <a class='feature-card' href='barqa.html'><span class='card-number'>02</span><h2>برقا: الإيمان في عمل يومي</h2><p>الرعاية، المياه والطرقات، الزراعة، المدرسة والمستوصف؛ مع إظهار دور المجتمع والمؤسسات.</p><span class='text-link'>اكتشف برقا ←</span></a>
  <a class='feature-card' href='cause.html'><span class='card-number'>03</span><h2>ما الذي تعنيه دعوى التطويب؟</h2><p>افتُتحت المرحلة الأبرشية عام 2022. نميّز بين الإيمان الشعبي والمسار الكنسي الرسمي.</p><span class='text-link'>تابع الوقائع ←</span></a>
</section>
<section class='home-feature'>
  <div><p class='eyebrow'>الذاكرة تحتاج إلى دقّة</p><h2>نحفظ ما نعرفه، ونُظهر ما لا نعرفه.</h2>
  <p>تختلف بعض المصادر في السنة التي تولّى فيها الأب نيكولا خدمة برقا، كما أن تفاصيل مقتله ومكان دفنه تُروى أحيانًا بصيغ مختلفة. لذلك نذكر مصادر كل معلومة، ونفصل الوقائع الموثقة عن الشهادات والتقوى الشعبية.</p>
  <a class='text-link' href='sources.html'>كيف بُني هذا الأرشيف؟ ←</a></div>
  <aside class='fact-box'><span class='fact-year'>22 · 01 · 2022</span><h3>افتتاح التحقيق الأبرشي</h3><p>أعلنت الرهبنة اليسوعية في أوروبا افتتاح دعوى التطويب في بيروت. الافتتاح ليس إعلانًا للتطويب أو القداسة.</p><a href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>الخبر لدى اليسوعيين ↗</a></aside>
</section>
<section class='section-block'>
  <p class='eyebrow'>إرث مستمر في المكان</p><h2>مركز برقا الصحي اليوم</h2>
  <p>تذكر جمعية فرسان مالطا في لبنان أن مركز برقا أُنشئ عام 1985 تكريمًا لذكرى الأب نيكولا، ويعمل بالتعاون مع راهبات يسوع ومريم. المركز مؤسسة جاءت بعد وفاته؛ لا ننسب تأسيسه إليه شخصيًا.</p>
  <a class='button-link' href='barqa.html#centre'>معلومات المركز والزيارة</a>
</section>
<section class='editorial-note'><p>هذه منصة توثيق مستقلة. لقب «خادم الله» وافتتاح الدعوى لا يعنيان أن الكنيسة أعلنت تطويبه أو قداسته. تُراجع الوقائع والمصادر قبل أي إضافة.</p></section>
""",
        },
        "life": {
            "title": "من دلفت إلى البقاع",
            "eyebrow": "سيرة · 1940–1985",
            "summary": "فنان هولندي دخل الرهبنة اليسوعية، وتكوّن في لبنان، ثم عاش خدمته الكهنوتية والاجتماعية بين قرى البقاع الشمالي.",
            "body": """
<section class='prose-layout'><div class='prose'>
<h2>طفولة وفنّ ودعوة</h2>
<p>وُلد نيكولا كلويترز في 25 أيار 1940 في مدينة دلفت بهولندا. قبل دخوله الرهبنة درس الفنون الجميلة؛ وتصفه مصادر يسوعية بأنه ظلّ فنانًا حتى بعد اختياره الكهنوت. لا يقدّم هذا الأرشيف اقتباسات فنية منسوبة إليه ما لم يكن لها مصدر منشور يمكن الرجوع إليه.</p>
<p>تذكر رواية يسوعية أنه انضم إلى جمعية يسوع عام 1966، وهو العام الذي وصل فيه إلى لبنان ليتابع تكوينه. درس العربية والعلوم الاجتماعية في بيروت، وأكمل دراساته الكهنوتية. رُسم كاهنًا في أمستردام في صيف 1973. ترد هذه المحطات في تقارير يسوعية وصحافية، ومنها مقابلات ومواد تعريفية عن حياته.</p>
<h2>لبنان: لغة ومجتمع وخدمة</h2>
<p>تذكر جامعة القديس يوسف أن كلويترز تعلّم العربية في لبنان ودرس العمل الاجتماعي فيها. هذا الجانب يوضح أن حضوره لم يكن رعويًا فقط: كان يحاول فهم واقع القرى واحتياجاتها اليومية في منطقة مهمّشة، خلال حرب أهلية وانهيار الخدمات.</p>
<p>في منتصف السبعينيات بدأ عمله الرعوي في قرى البقاع. تختلف المصادر في تأريخ انتقاله إلى برقا تحديدًا: تذكر تقارير سنوات 1974 و1976 و1977، ويورد تقرير آخر تعيينًا لاحقًا. لذلك نستخدم في الخط الزمني نطاق «منتصف السبعينيات» ونشرح اختلاف الروايات بدل تثبيت سنة واحدة.</p>
<h2>فنان المصالحة</h2>
<p>تصف مصادر يسوعية ومقابلات مع من عرفوه نشاطه في جمع الناس حول مبادرات اجتماعية ودينية، وفي التشجيع على التعايش والمصالحة بين عائلات ومجتمعات متجاورة. ويذكر تقرير يسوعي أن درب الصليب الحيّ صار تقليدًا سنويًا في برقا منذ نحو 1980. هذه التفاصيل منقولة عن رفاقه وشهود محليين؛ وهي ليست سجلًا إداريًا مستقلًا لكل مشروع.</p>
<div class='quote-card'><p>المصادر الأقرب إليه تصوّره كاهنًا وفنانًا وعاملًا اجتماعيًا في آن واحد؛ لا كسيرة بطولة مجرّدة من الناس الذين عملوا معه.</p><span>ملاحظة تحريرية من فريق الأرشيف</span></div>
<h2>الاختطاف والوفاة</h2>
<p>في 14 آذار 1985 اختُطف الأب نيكولا في البقاع خلال الحرب الأهلية. أفادت الرهبنة اليسوعية في أوروبا أن جثمانه عُثر عليه في 1 نيسان في وادٍ عميق. لا نحدد هوية الخاطفين أو دوافعهم في هذا الموقع؛ فالمصادر المتاحة التي راجعناها لا تقدّم أساسًا موحدًا كافيًا لذلك.</p>
<p>يضع تقرير صحافي لبناني ضريحه في دير تعنايل. نذكر ذلك بوصفه تقريرًا صحافيًا مصوّرًا، لا سجلًا كنسيًا لرفات أو موقع حجّ معتمد.</p>
<p class='source-line'>للقراءة: <a class='cite' href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>السيرة لدى اليسوعيين الهولنديين</a> · <a class='cite' href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>تحقيق L’Orient-Le Jour</a> · <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>خبر افتتاح الدعوى</a></p>
</div><aside class='side-portrait'><img src='{{ASSET}}portrait-formal.jpg' alt='صورة أرشيفية للأب نيكولا كلويترز، قدّمها صاحب المشروع' loading='lazy'><p>صورة أرشيفية مقدّمة من صاحب المشروع. تاريخ الصورة واسم المصوّر غير مثبتين.</p><a href='archive.html'>تصفّح الأرشيف المصوّر ←</a></aside></section>
""",
        },
        "barqa": {
            "title": "برقا والعمل الذي بقي",
            "eyebrow": "المكان · المجتمع · الخدمات",
            "summary": "لا تُختزل برقا في سيرة رجل واحد. كان أثر الأب نيكولا مرتبطًا بعمل أهل البلدة، والراهبات، والرهبنة اليسوعية، وجمعية مالطا، والداعمين.",
            "body": """
<section class='prose'>
<h2>قرى البقاع الشمالي</h2>
<p>عمل كلويترز في مجموعة قرى في شمال البقاع، وكانت برقا مركزًا مهمًا لخدمته. تصف مصادر الرهبنة المنطقة بأنها ريفية ومهمّشة ومتأثرة بالحرب وبضعف البنية والخدمات. اسم القرية يرد بصيغ لاتينية متعدّدة مثل Barqa وBarka وBarqa/Barkaa؛ نستخدم «برقا» وBarqa لتجنّب الخلط بقرى أخرى تحمل الاسم نفسه.</p>
<h2>مشاريع عملية وشراكة محلية</h2>
<p>تتكرر في الشهادات المنشورة إشارات إلى تحسين الوصول إلى الأراضي الزراعية، ومشاريع المياه والريّ، والبساتين، والتعليم والرعاية الصحية. وتُظهر روايات محلية أن هذه المبادرات نُفّذت بجهد مشترك مع الأهالي، والراهبات، والجهات الداعمة؛ لذلك لا ننسب كل بناء أو مشروع إلى شخص واحد.</p>
<p>يذكر تقرير اليسوعيين أعمالًا اجتماعية رعوية ومصالحة بين العائلات، بينما تسرد مواد «أرشيف برقا» المنشورة في الصحافة المحلية تفاصيل إضافية عن الطرق والمياه والبساتين ومشاغل البلدة. نعامل التفاصيل الأخيرة كشهادات محلية منشورة، لا كإحصاءات رسمية مستقلة.</p>
<h2 id='centre'>مركز برقا الصحي</h2>
<p>تقول جمعية مالطا لبنان إن المركز الصحي في برقا أُنشئ عام 1985 تكريمًا لذكرى الأب نيكولا، وتقول صفحة المركز الرسمية إنه يعمل بالتعاون مع راهبات يسوع ومريم. ويؤكد تقرير جمعية مالطا لعام 2026 استمرار عمل المركز واستقبال وفد الجمعية فيه.</p>
<p>بحسب قائمة المركز الرسمية: العنوان برقا، البقاع؛ هاتف محلي <a href='tel:28320490'>28-320490</a>. لا تنشر الصفحة ساعات الدوام أو قائمة تفصيلية للخدمات المحلية، لذا يُفضّل الاتصال قبل الزيارة أو الاعتماد على الحالات الطبية الطارئة.</p>
<div class='map-actions'><a class='button-link' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>صفحة مركز برقا الرسمية ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Order+of+Malta+Barqa+Community+Health+Centre+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_BARQA}} ↗</a></div>
<div class='callout'><strong>تمييز مهم</strong><p>مركز برقا مؤسسة رعاية أُنشئت بعد وفاة الأب نيكولا. يوثق الموقع صلته بذكراه ولا يقدّمه على أنه أسّسه شخصيًا.</p></div>
<h2>القرية اليوم</h2>
<p>تصف جمعية مالطا مركز برقا ضمن شبكة رعاية صحية أولية في لبنان. أما أعداد القرى التي يخدمها المركز، فتختلف بين المواد المنشورة على مرّ السنوات؛ لا نكرر رقمًا واحدًا بوصفه حقيقة حالية من دون تحديث رسمي مباشر.</p>
<p class='source-line'>مصادر: <a class='cite' href='https://malte-liban.org/centre-de-barqa/' target='_blank' rel='noopener noreferrer'>جمعية مالطا لبنان: مركز برقا</a> · <a class='cite' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>الدليل الرسمي للمركز</a> · <a class='cite' href='https://www.orderofmalta.int/news/grand-hospitaller-lebanon-healthcare-aid-order-of-malta-humanitarian-visit/' target='_blank' rel='noopener noreferrer'>تقرير الجمعية عن زيارة 2026</a></p>
</section><figure class='wide-photo'><img src='https://s.lorientlejour.com/storage/attachments/1498/364623_364806.jpeg/r/800/364623_364806.jpeg' alt='فريق جمعية مالطا ووفدها في مركز برقا الصحي، صورة مقدّمة من جمعية مالطا لبنان إلى L’Orient-Le Jour' loading='lazy' referrerpolicy='strict-origin-when-cross-origin'><figcaption>زيارة إلى مركز برقا الصحي، 2026. الصورة مقدّمة من جمعية مالطا لبنان إلى L’Orient-Le Jour. <a href='https://www.lorientlejour.com/article/1497432/-vous-etes-un-modele-le-message-du-grand-hospitalier-a-lordre-de-malte-liban.html' target='_blank' rel='noopener noreferrer'>التقرير والصورة لدى الصحيفة ↗</a></figcaption></figure>
""",
        },
        "timeline": {
            "title": "الخط الزمني",
            "eyebrow": "محطات موثقة واختلافات معلنة",
            "summary": "يورد الخط الزمني الأحداث ذات السند المنشور. حين تختلف المصادر، نعرض نطاقًا زمنيًا أو نذكر الخلاف بدل إعطاء دقة غير مضمونة.",
            "body": """
<ol class='timeline-list'>
<li><time>25 أيار 1940</time><div><h2>الولادة في دلفت</h2><p>وُلد نيكولا كلويترز في دلفت، هولندا. <a class='cite' href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>السيرة اليسوعية الهولندية</a></p></div></li>
<li><time>1966</time><div><h2>الانضمام إلى اليسوعيين والوصول إلى لبنان</h2><p>تذكر مصادر يسوعية وصحافية أنه دخل الرهبنة اليسوعية ووصل إلى لبنان في هذا العام بعد دراسة الفنون الجميلة. درس العربية والعمل الاجتماعي في بيروت. <a class='cite' href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour</a></p></div></li>
<li><time>صيف 1973</time><div><h2>السيامة الكهنوتية</h2><p>رُسم كاهنًا في أمستردام، بحسب السيرة اليسوعية الهولندية. <a class='cite' href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>الرهبنة اليسوعية الهولندية</a></p></div></li>
<li><time>منتصف السبعينيات</time><div><h2>الخدمة الرعوية في شمال البقاع</h2><p>تختلف التواريخ المنشورة لبداية الخدمة في برقا بين 1974 و1976 و1977، مع تقارير عن تعيين لاحق. تؤكد الرهبنة اليسوعية أنه خدم قرى البقاع نحو عشر سنوات. لذلك لا نختار سنة واحدة بلا تحفظ. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>الرهبنة اليسوعية في أوروبا</a></p></div></li>
<li><time>نحو 1980</time><div><h2>درب الصليب الحيّ</h2><p>تذكر مصادر يسوعية أن تمثيل درب الصليب مع أهل برقا أصبح مبادرة سنوية منذ نحو 1980. <a class='cite' href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>الرواية اليسوعية</a></p></div></li>
<li><time>14 آذار 1985</time><div><h2>الاختطاف</h2><p>اختُطف الأب نيكولا في البقاع أثناء الحرب الأهلية. لا تنسب المصادر التي راجعناها المسؤولية إلى جهة واحدة مثبتة قضائيًا. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>الرهبنة اليسوعية في أوروبا</a></p></div></li>
<li><time>1 نيسان 1985</time><div><h2>العثور على جثمانه</h2><p>تذكر الرهبنة اليسوعية العثور على جثمانه في وادٍ عميق. ويصف تقرير صحافي لاحق ضريحه في دير تعنايل. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>الرهبنة اليسوعية</a> · <a class='cite' href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>نداء الوطن</a></p></div></li>
<li><time>1985</time><div><h2>إنشاء مركز برقا الصحي تكريمًا لذكراه</h2><p>تقول جمعية مالطا لبنان إن المركز أُنشئ في العام نفسه، بعد مقتله. <a class='cite' href='https://malte-liban.org/centre-de-barqa/' target='_blank' rel='noopener noreferrer'>جمعية مالطا لبنان</a></p></div></li>
<li><time>22 كانون الثاني 2022</time><div><h2>افتتاح المرحلة الأبرشية لدعوى التطويب</h2><p>افتتح الأسقف سيزار عسيّان التحقيق الأبرشي في بيروت. هذه خطوة في مسار كنسي، وليست إعلانًا للتطويب. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>الخبر الرسمي لليسوعيين</a></p></div></li>
</ol>
<p class='editorial-note'>التواريخ الرئيسية هنا مستندة إلى مصادر منشورة. تفاصيل اليوم الأخير، وتاريخ تعيينه الدقيق في برقا، ومراحل الدعوى بعد افتتاحها تحتاج إلى مصادر أولية إضافية.</p>
""",
        },
        "cause": {
            "title": "دعوى التطويب: ما نعرفه",
            "eyebrow": "المسار الكنسي · آخر توثيق علني",
            "summary": "افتتحت المرحلة الأبرشية لدعوى الأب نيكولا في 22 كانون الثاني 2022. ما بعد ذلك يجب أن يُثبت بإعلان كنسي موثوق، لا بالتداول أو التوقع.",
            "body": """
<section class='prose'>
<div class='status-panel'><span class='status-dot'></span><div><strong>الخطوة المثبتة علنًا في المصادر التي راجعناها</strong><p>افتتاح التحقيق الأبرشي في بيروت عام 2022. آخر تحديث لهذه الصفحة: 5 تشرين الثاني 2026.</p></div></div>
<h2>ما جرى في 2022</h2>
<p>أعلنت الرهبنة اليسوعية في أوروبا أن الأسقف اللبناني سيزار عسيّان افتتح الدعوى يوم 22 كانون الثاني 2022. وتذكر أن هيئة كنسية تدرس ما إذا كان كلويترز قد مات شهيدًا، وفق التعريف الكنسي. افتتاح الدعوى يبدأ مسار التحقيق ولا يحسم نتيجته.</p>
<h2>ما لا نقوله</h2>
<ul><li>لا نصفه بأنه طوباوي أو قديس؛ لم نعثر في المصادر الرسمية التي راجعناها على إعلان تطويب أو قداسة.</li><li>لا نؤكد أن ملفًا أُحيل إلى روما أو أن معجزة اعتمدت؛ لم نعثر على توثيق رسمي متاح يؤيد ذلك.</li><li>نميز بين تكريم الناس له بوصفه شهيدًا في لغة الإيمان، وبين الحكم الكنسي الذي ما زالت الدعوى تبحث فيه.</li></ul>
<h2>ماذا تعني المصطلحات؟</h2>
<p>تشرح دائرة دعاوى القديسين في الفاتيكان أن الأسقف الأبرشي يجمع أعمال التحقيق ويرفعها وفق الإجراءات، ثم تُفحص الدعوى في المراحل اللاحقة. لقب «خادم الله» الذي تستعمله مصادر يسوعية يأتي في سياق بدء الدعوى؛ ولا يساوي إعلانًا بالتطويب.</p>
<p class='source-line'><a class='button-link' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>إعلان اليسوعيين عن افتتاح الدعوى ↗</a> <a class='quiet-link' href='https://www.vatican.va/content/romancuria/en/dicasteri/dicastero-cause-santi/profilo.html' target='_blank' rel='noopener noreferrer'>إجراءات الدائرة في الفاتيكان ↗</a></p>
<div class='callout'><strong>إذا ظهر تحديث رسمي</strong><p>ينبغي تحديث هذه الصفحة مع رابط الإعلان وتاريخه، مع نقل المعلومة كما وردت وعدم استنتاج مرحلة جديدة من عبارات عامة.</p></div>
</section>
""",
        },
        "places": {
            "title": "أماكن الذاكرة والزيارة",
            "eyebrow": "برقا · مركز الرعاية · تعنايل",
            "summary": "ما نقدر على توثيقه هو مركز برقا الصحي، ودير تعنايل بوصفه موقع دفن يذكره تقرير صحافي. لم نعثر على إعلان يصف المكان رسميًا بأنه مزار أو مزار معتمد.",
            "body": """
<section class='place-grid'>
<article class='place-card'><p class='eyebrow'>برقا · البقاع</p><h2>مركز برقا الصحي الاجتماعي</h2><p>مركز صحي أُنشئ عام 1985 تكريمًا لذكرى الأب نيكولا، ويعمل بالتعاون مع راهبات يسوع ومريم وفق صفحة جمعية مالطا لبنان.</p><p><strong>العنوان المنشور:</strong> برقا، البقاع<br><strong>الهاتف المنشور:</strong> <a href='tel:28320490'>28-320490</a></p><p>لا تظهر ساعات الزيارة على الصفحة الرسمية. اتصل قبل الذهاب؛ لا تستخدم مركزًا صحيًا كوجهة سياحية من دون تنسيق.</p><div class='map-actions'><a class='button-link' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>المركز لدى مالطا لبنان ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Order+of+Malta+Barqa+Community+Health+Centre+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_BARQA}} ↗</a></div></article>
<article class='place-card'><p class='eyebrow'>تعنايل · سهل البقاع</p><h2>دير تعنايل وضريح الأب نيكولا</h2><p>نشرت نداء الوطن عام 2025 صورة بعنوان «ضريح الأب الشهيد في دير تعنايل»، وذكرت رواية عن طلب محلي لنقل رفاته إلى برقا. لم نعثر على مصدر رسمي يثبت قبول الطلب أو حصول النقل.</p><p>لذلك نعرض تعنايل بوصفه موقعًا يذكره التقرير الصحافي، لا مزارًا كنسيًا معتمدًا. لم نجد ساعات زيارة أو ترتيبات دخول منشورة.</p><div class='map-actions'><a class='button-link' href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>التقرير والصورة ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Jesuit+Monastery+Taanayel+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_TAANAYEL}} ↗</a></div></article>
</section>
<section class='prose'><h2>هل يوجد مزار رسمي؟</h2><p>لم نعثر في إعلانات الرهبنة اليسوعية أو صفحات جمعية مالطا التي راجعناها على تسمية «مزار» أو «مقدس» رسمي للأب نيكولا. حضور صوره في بيوت برقا وتكريم الأهالي له يعبّران عن ذاكرة وتكريم محليين، ولا يثبتان وضعًا كنسيًا أو ترتيبات حجّ.</p>
<h2>تأمل قصير</h2><div class='prayer-card'><p>يا إله السلام، اذكر أهل برقا وكل من يخدم المجتمعات المهمّشة. امنحنا شجاعة الإصغاء والعمل معًا، واحفظ ضحايا العنف وعائلاتهم. آمين.</p><span>نص تحريري أُعدّ لهذا الموقع؛ ليس صلاة كنسية رسمية ولا طلب شفاعة معتمدًا.</span></div>
<p>للخدمات الصحية أو التنسيق حول زيارة المركز، استخدم بيانات الاتصال المنشورة من <a class='cite' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>جمعية مالطا لبنان</a>. وللزيارة الدينية، تواصل مسبقًا مع الجهة الكنسية المعنية؛ لا نفترض أن الدير مفتوح للزوار.</p></section>
""",
        },
        "archive": {
            "title": "الأرشيف المصوّر",
            "eyebrow": "صور أصلية · صور منشورة · فن معاصر",
            "summary": "يحفظ المعرض صور المشروع كما قُدّمت، ويضيف صورًا أرشيفية منشورة تنسبها الصحافة إلى «أرشيف برقا»، وصورة معاصرة للمركز الصحي. لكل صورة مصدر ووصف وحدود معروفة.",
            "body": """
<div class='gallery-intro'><p>الصور التاريخية المضافة أدناه تظهر في تحقيق «نداء الوطن» المنشور عام 2025 مع نسبة مجموعة منها إلى أرشيف برقا. نعرضها من خادم الصحيفة، ونربطها بالمادة الأصلية؛ لا نعيد رفعها إلى مستودع الموقع. حقوق الصور تعود إلى أصحابها أو ناشرها، ونرحب بتزويدنا ببيانات المصوّر والترخيص.</p><p>صور «المشروع» هي الملفات الخمسة التي قدّمها صاحب الموقع. لا تتوفر لنا بيانات مصور أو تاريخ لكل ملف.</p></div>
<div id='gallery' class='photo-grid'>{{GALLERY}}</div>
<section class='editorial-note'><p><strong>تمييز بصري:</strong> الصورة الملوّنة معالجة رقميًا وليست صورة ملوّنة أصلية. والعمل التذكاري تركيب فني معاصر، لا مشهدًا تاريخيًا. لم نستخدم صورًا مولّدة بالذكاء الاصطناعي على أنها صور أرشيفية.</p></section>
""",
        },
        "sources": {
            "title": "المصادر وطريقة التوثيق",
            "eyebrow": "أرشيف مفتوح · مراجعة 5 تشرين الثاني 2026",
            "summary": "تُسنَد الوقائع إلى مصادرها قرب النص. نفضّل الرهبنة اليسوعية، المؤسسات الصحية والجامعية، والتغطية الصحافية المعروفة؛ ونسمي الشهادات المحلية بوصفها شهادات.",
            "body": """
<section class='prose'><h2>سجل المصادر</h2><p>هذه القائمة تجمع أهم المراجع التي بُنيت عليها صفحات الموقع. المواد تتفاوت في طبيعتها: إعلان مؤسسي، سيرة يسوعية، تقرير صحافي، سجل مرجعي أو شهادة محلية. لا نتعامل معها كلها على أنها نوع واحد من الأدلة.</p></section>
<div class='source-list'>
<article><span class='source-type'>رهبنة يسوعية · خبر رسمي</span><h3>افتتاح دعوى التطويب</h3><p>تاريخ افتتاح المرحلة الأبرشية في بيروت، مدة خدمته في قرى البقاع، وتواريخ الاختطاف والعثور على الجثمان.</p><a href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jesuits in Europe ↗</a></article>
<article><span class='source-type'>رهبنة يسوعية هولندية · سيرة</span><h3>Nico Kluiters SJ</h3><p>سيرة مؤسسية باللغة الهولندية، تتناول التكوين والرسالة في لبنان.</p><a href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>Jezuïeten ↗</a></article>
<article><span class='source-type'>رهبنة يسوعية · شهادات وتاريخ</span><h3>Martelaar voor geloof, gerechtigheid en vrede</h3><p>رواية عن الصلح والمبادرات الاجتماعية، ودرب الصليب الحيّ. نتعامل مع مشاهدها بوصفها رواية يسوعية وشهادات، لا محضرًا رسميًا لكل نشاط.</p><a href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>Jezuïeten ↗</a></article>
<article><span class='source-type'>جامعة القديس يوسف · خبر</span><h3>التحقيق الأبرشي في بيروت</h3><p>تغطية جامعية للاحتفال الكنسي وافتتاح الدعوى في كانون الثاني 2022.</p><a href='https://www.usj.edu.lb/news.php?id=11479' target='_blank' rel='noopener noreferrer'>Université Saint-Joseph ↗</a></article>
<article><span class='source-type'>رهبنة مالطا · دليل حالي</span><h3>مركز برقا الصحي</h3><p>العنوان والهاتف والتشغيل المشترك مع راهبات يسوع ومريم.</p><a href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Order of Malta Lebanon ↗</a></article>
<article><span class='source-type'>رهبنة مالطا · تحديث 2026</span><h3>زيارة المستشفى الأكبر إلى لبنان</h3><p>تأكيد زيارة مركز برقا عام 2026، ووصفه مركزًا صحيًا أُنشئ عام 1985 تكريمًا لذكرى الأب نيكولا.</p><a href='https://www.orderofmalta.int/news/grand-hospitaller-lebanon-healthcare-aid-order-of-malta-humanitarian-visit/' target='_blank' rel='noopener noreferrer'>Order of Malta ↗</a></article>
<article><span class='source-type'>صحافة لبنانية · سيرة مصوّرة</span><h3>الأب نيكولا كلويترز… حين صار الكاهن وطنًا لبرقا</h3><p>تحقيق عربي عام 2025 يستند إلى شهادات وأرشيف محلي. صور المجموعة تحمل نسبة «أرشيف برقا»؛ لذلك نعرضها عبر رابط الصحيفة ونحافظ على هذه النسبة.</p><a href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>نداء الوطن ↗</a></article>
<article><span class='source-type'>L’Orient-Le Jour · تحقيق 2022</span><h3>Passion et martyre</h3><p>مادة فرنسية عن دراسته ووصوله إلى لبنان والعمل الاجتماعي، وتضم صورًا تاريخية من مصادر مختلفة.</p><a href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour ↗</a></article>
<article><span class='source-type'>L’Orient-Le Jour · صورة 2026</span><h3>زيارة مركز برقا</h3><p>صورة معاصرة عند المركز الصحي، منسوبة إلى جمعية مالطا لبنان.</p><a href='https://www.lorientlejour.com/article/1497432/-vous-etes-un-modele-le-message-du-grand-hospitalier-a-lordre-de-malte-liban.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour ↗</a></article>
<article><span class='source-type'>Ignis · صوتيات</span><h3>وثائقي صوتي عن Nico Kluiters</h3><p>وثائقي باللغة الهولندية يستند إلى رسائل وشهادات ومقابلات.</p><a href='https://igniswebmagazine.nl/kerk/audio-documentaire-nico-kluiters/' target='_blank' rel='noopener noreferrer'>استمع إلى الوثائقي ↗</a></article>
<article><span class='source-type'>كتاب</span><h3>Carole Dagher, Passion pour une terre délaissée</h3><p>سيرة مطوّلة منشورة عام 2013؛ صدرت ترجمتها الهولندية عام 2023. الكتاب مصدر مهم للتفاصيل، لكنه ليس متاحًا كاملًا مجانًا على الويب.</p><a href='https://www.abdijvanberne.nl/nieuws/boekpresentatie-nicolaas-kluiters/' target='_blank' rel='noopener noreferrer'>معلومات طبعة 2023 ↗</a></article>
<article><span class='source-type'>كتاب ووثائق شخصية</span><h3>Frans Berkemeijer SJ, Verzoeningsartiest in het gebroken Libanon</h3><p>مختارات منشورة عام 2025 من رسائل ويوميات وشهادات. للمؤرخين والباحثين، تُعدّ اليوميات والرسائل أصلًا مهمًا للتحقق من تفاصيل العمل.</p><a href='https://www.otheo.be/artikel/verzoeningsartiest-nicolaas-kluiters-stierf-40-jaar-geleden-marteldood-portret' target='_blank' rel='noopener noreferrer'>عرض الكتاب والسياق ↗</a></article>
<article><span class='source-type'>سجل مرجعي · بيانات مقتضبة</span><h3>Wikidata وملف السلطة الألماني</h3><p>يسجلان بيانات ولادة أساسية. مدخل Wikidata لا يملك حاليًا رابطًا إلى صفحة Wikipedia مستقلة؛ لا نستعمله مصدرًا لتفاصيل السيرة.</p><a href='https://www.wikidata.org/wiki/Q133745483' target='_blank' rel='noopener noreferrer'>Wikidata ↗</a></article>
<article><span class='source-type'>الفاتيكان · شرح مؤسسي</span><h3>دائرة دعاوى القديسين</h3><p>مرجع عام لفهم دور الدائرة والمراحل الكنسية؛ ليس تحديثًا خاصًا بملف الأب نيكولا.</p><a href='https://www.vatican.va/content/romancuria/en/dicasteri/dicastero-cause-santi/profilo.html' target='_blank' rel='noopener noreferrer'>Vatican.va ↗</a></article>
</div>
<section class='prose'>
<h2>ما وجدناه على Wikipedia ووسائل التواصل</h2>
<p>لم يظهر في Wikidata رابطٌ إلى مقالة Wikipedia مستقلة للأب نيكولا بالإنجليزية أو العربية أو الفرنسية، والسجل المرجعي نفسه محدود. بعض مقالات ويكيبيديا عن أحداث أوسع تذكر اسمه، لكنها ليست سيرة كافية.</p>
<p>تُظهر التغطية الصحافية صورًا من «أرشيف برقا» وبعضها وُصف بأنه نُشر عبر Facebook. لم نتحقق من حساب عام رسمي مخصص له على Facebook أو Instagram، ولذلك لا ننسب إليه أو إلى عائلته أو لجنة الدعوى أي حساب. الصور المنشورة هنا ترتبط بالمادة الصحافية التي عرضتها.</p>
<h2>اختلافات نصرّح بها</h2>
<ul><li>تختلف بعض المصادر في سنة بدء خدمته في برقا؛ نذكر «منتصف السبعينيات» ونوضح الخلاف.</li><li>تُفصل واقعة اختطافه في 14 آذار 1985 عن خبر العثور على جثمانه في 1 نيسان.</li><li>لا نعلن مرحلة جديدة في دعوى التطويب بعد افتتاح التحقيق الأبرشي ما لم نجد إعلانًا رسميًا أحدث.</li><li>يُذكر ضريحه في دير تعنايل في تقرير صحافي؛ لم نجد تأكيدًا رسميًا لنقل الرفات أو اعتماد الموقع مزارًا.</li></ul>
<h2>الصور والحقوق</h2>
<p>الملفات الخمسة المحلية قدّمها صاحب المشروع؛ تبقى أسماء المصورين والتواريخ وحقوق النشر بحاجة إلى توثيق. صور «أرشيف برقا» وصورة المركز الصحي محمّلة مباشرة من مواقع ناشريها، مع نسبتها ورابط المصدر. لم تُنسخ إلى مستودع هذا الموقع؛ حقوقها تبقى لأصحابها والناشرين. يُرجى التواصل معنا عبر مالك المشروع لإضافة التصحيحات أو بيانات الترخيص.</p>
</section>
""",
        },
    },
    "en": {
        "index": {
            "title": "A life of faith and service in the Bekaa",
            "eyebrow": "Documented biography · Barqa’s living memory",
            "summary": "Father Nicolas Kluiters was a Dutch Jesuit, an artist before priesthood, and a pastor and social worker among villages in Lebanon’s northern Bekaa. This archive brings together the documented story, the practical legacy, and the memory that remains in Barqa.",
            "body": """
<section class='feature-grid'>
  <a class='feature-card' href='life.html'><span class='card-number'>01</span><h2>The person and his vocation</h2><p>From Delft in the Netherlands to Jesuit formation, priesthood and ministry in Lebanon.</p><span class='text-link'>Read the biography →</span></a>
  <a class='feature-card' href='barqa.html'><span class='card-number'>02</span><h2>Barqa: faith in practical work</h2><p>Pastoral life, water and access roads, farming, education and healthcare—with community partners named.</p><span class='text-link'>Explore Barqa →</span></a>
  <a class='feature-card' href='cause.html'><span class='card-number'>03</span><h2>What is the beatification cause?</h2><p>The diocesan inquiry opened in 2022. We distinguish local devotion from formal Church decisions.</p><span class='text-link'>See the documented status →</span></a>
</section>
<section class='home-feature'>
  <div><p class='eyebrow'>Memory needs careful history</p><h2>Keep what is known. Show what is not.</h2>
  <p>Sources differ on the year Father Nicolas began ministry in Barqa. Accounts of his final days and burial also vary. We cite claims near the text and separate documented facts from testimony and popular devotion.</p>
  <a class='text-link' href='sources.html'>How this archive was researched →</a></div>
  <aside class='fact-box'><span class='fact-year'>22 · 01 · 2022</span><h3>Diocesan inquiry opened</h3><p>The Jesuit Conference of European Provincials reported the opening of the cause in Beirut. Opening a cause is not beatification or canonization.</p><a href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Read the Jesuit announcement ↗</a></aside>
</section>
<section class='section-block'>
  <p class='eyebrow'>A continuing local legacy</p><h2>Barqa’s community health centre today</h2>
  <p>The Lebanese Association of the Order of Malta says the Barqa centre was established in 1985 in memory of Father Nicolas and is operated with the Sisters of Jesus and Mary. It is an institution established after his death; we do not say he personally founded it.</p>
  <a class='button-link' href='barqa.html#centre'>Centre information and visiting details</a>
</section>
<section class='editorial-note'><p>This is an independent documentary project, not an official Jesuit or beatification-cause website. “Servant of God” and the opening of a cause do not mean the Church has beatified or canonized him.</p></section>
""",
        },
        "life": {
            "title": "From Delft to the Bekaa",
            "eyebrow": "Biography · 1940–1985",
            "summary": "A Dutch artist entered the Society of Jesus, trained in Lebanon, and spent his priestly and social ministry among villages in the northern Bekaa.",
            "body": """
<section class='prose-layout'><div class='prose'>
<h2>Art, formation and vocation</h2>
<p>Nicolas Kluiters was born in Delft, the Netherlands, on 25 May 1940. He studied fine arts before joining the Jesuits; Jesuit accounts describe a man who remained an artist after choosing priesthood. This archive does not reproduce quotations attributed to him unless a published, traceable source can be identified.</p>
<p>A Jesuit biography dates his entry into the Society of Jesus to 1966, the year he arrived in Lebanon for formation. He studied Arabic and social work in Beirut and completed priestly formation. He was ordained in Amsterdam in the summer of 1973. These milestones appear in Jesuit and press accounts, including biographical material.</p>
<h2>Lebanon: language, society and ministry</h2>
<p>Saint Joseph University reports that Kluiters learned Arabic and studied social work in Lebanon. This background helps explain why his work was not only pastoral: he sought to understand the daily conditions of villages marginalized by poor infrastructure and war.</p>
<p>By the mid-1970s he was serving villages in the Bekaa. Sources differ on the exact year he moved to Barqa: reports cite 1974, 1976 and 1977, while another refers to a later appointment. We use “mid-1970s” in the timeline and explain the discrepancy instead of fixing a date without adequate evidence.</p>
<h2>An artist of reconciliation</h2>
<p>Jesuit accounts and interviews with people who knew him describe efforts to bring people together through social and pastoral work, and to encourage reconciliation among families and neighboring communities. A Jesuit retrospective says a live Stations of the Cross became an annual Barqa tradition around 1980. These details are reported memories, not an independent administrative record for every project.</p>
<div class='quote-card'><p>The sources closest to his life portray him as priest, artist and social worker at once—not as an abstract hero detached from the people who worked alongside him.</p><span>Editorial note from the archive</span></div>
<h2>Kidnapping and death</h2>
<p>On 14 March 1985, Father Nicolas was kidnapped in the Bekaa during the Lebanese Civil War. The Jesuit Conference of European Provincials reports that his body was found in a deep ravine on 1 April. We do not name a perpetrator or motive here: the sources reviewed do not establish a single, independently documented account.</p>
<p>A Lebanese press report identifies his tomb at Deir Taanayel. We describe this as a published report with a photograph, not as an ecclesiastical register of relics or an approved pilgrimage site.</p>
<p class='source-line'>Read more: <a class='cite' href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>Dutch Jesuit biography</a> · <a class='cite' href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour feature</a> · <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Beatification-cause announcement</a></p>
</div><aside class='side-portrait'><img src='{{ASSET}}portrait-formal.jpg' alt='Archival portrait of Father Nicolas Kluiters, supplied by the project owner' loading='lazy'><p>Archival image supplied by the project owner. The date and photographer have not been established.</p><a href='archive.html'>Browse the photo archive →</a></aside></section>
""",
        },
        "barqa": {
            "title": "Barqa and the work that remains",
            "eyebrow": "Place · community · services",
            "summary": "Barqa cannot be reduced to one man’s biography. Father Nicolas’s legacy is bound up with the work of residents, sisters, Jesuits, the Order of Malta and other supporters.",
            "body": """
<section class='prose'>
<h2>Villages of the northern Bekaa</h2>
<p>Kluiters served a group of villages in the northern Bekaa, with Barqa central to his ministry. Jesuit sources describe a rural, underserved region affected by war and weak infrastructure. The village name appears in Latin spellings including Barqa and Barka; this site uses Barqa and the Arabic برقا to avoid confusion with other places of the same name.</p>
<h2>Practical projects and shared work</h2>
<p>Published accounts repeatedly refer to better access to farmland, water and irrigation projects, orchards, education and healthcare. Local accounts describe these efforts as collaborative, involving residents, sisters and supporting organizations. We therefore do not attribute every building or project to one person.</p>
<p>Jesuit retrospectives emphasize socio-pastoral work and reconciliation. A 2025 local history published by Nidaa Al Watan adds accounts of roads, water, orchards, schools, a dispensary and workshops. We identify those details as published local testimony, not as an independently audited project register.</p>
<h2 id='centre'>Barqa Community Health Centre</h2>
<p>The Lebanese Association of the Order of Malta says the centre was established in 1985 in memory of Father Nicolas. Its official centre listing says it operates in cooperation with the Sisters of Jesus and Mary. A 2026 Order of Malta report confirms a visit to the centre and its continued operation.</p>
<p><strong>Published address:</strong> Barqa, Bekaa<br><strong>Published local telephone:</strong> <a href='tel:28320490'>28-320490</a></p>
<p>The official listing does not provide opening hours or a detailed list of services at this specific centre. Call before visiting; do not rely on this archive for emergency care.</p>
<div class='map-actions'><a class='button-link' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Official Barqa centre listing ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Order+of+Malta+Barqa+Community+Health+Centre+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_BARQA}} ↗</a></div>
<div class='callout'><strong>An important distinction</strong><p>The health centre was established after Father Nicolas’s death. This archive documents its connection to his memory; it does not describe him as its personal founder.</p></div>
<h2>The village today</h2>
<p>The Order of Malta lists Barqa as one of its community health centres in Lebanon. Published estimates of the number of surrounding villages served vary over time, so this site does not repeat a single figure as current without a current official source.</p>
<p class='source-line'>Sources: <a class='cite' href='https://malte-liban.org/centre-de-barqa/' target='_blank' rel='noopener noreferrer'>Association Malte Liban: Barqa centre</a> · <a class='cite' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Official centre listing</a> · <a class='cite' href='https://www.orderofmalta.int/news/grand-hospitaller-lebanon-healthcare-aid-order-of-malta-humanitarian-visit/' target='_blank' rel='noopener noreferrer'>2026 Order of Malta report</a></p>
</section><figure class='wide-photo'><img src='https://s.lorientlejour.com/storage/attachments/1498/364623_364806.jpeg/r/800/364623_364806.jpeg' alt='Order of Malta delegation and centre team at the Barqa health centre; photo supplied by the Order of Malta Lebanon to L’Orient-Le Jour' loading='lazy' referrerpolicy='strict-origin-when-cross-origin'><figcaption>Visit to the Barqa health centre, 2026. Photo supplied by the Order of Malta Lebanon to L’Orient-Le Jour. <a href='https://www.lorientlejour.com/article/1497432/-vous-etes-un-modele-le-message-du-grand-hospitalier-a-lordre-de-malte-liban.html' target='_blank' rel='noopener noreferrer'>Read the article and photo credit ↗</a></figcaption></figure>
""",
        },
        "timeline": {
            "title": "Timeline",
            "eyebrow": "Documented milestones and stated discrepancies",
            "summary": "This timeline includes events with published support. Where sources differ, it gives a range or explains the disagreement instead of claiming false precision.",
            "body": """
<ol class='timeline-list'>
<li><time>25 May 1940</time><div><h2>Born in Delft</h2><p>Nicolas Kluiters was born in Delft, the Netherlands. <a class='cite' href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>Dutch Jesuit biography</a></p></div></li>
<li><time>1966</time><div><h2>Joined the Jesuits and arrived in Lebanon</h2><p>Jesuit and press sources date his entry into the Society and arrival in Lebanon to this year, after fine-arts studies. He studied Arabic and social work in Beirut. <a class='cite' href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour</a></p></div></li>
<li><time>Summer 1973</time><div><h2>Ordained a priest</h2><p>He was ordained in Amsterdam, according to the Dutch Jesuit biography. <a class='cite' href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>Dutch Jesuits</a></p></div></li>
<li><time>Mid-1970s</time><div><h2>Pastoral ministry in the northern Bekaa</h2><p>Published sources give different starting years for his ministry in Barqa: 1974, 1976 and 1977, and one account cites a later appointment. Jesuit sources agree that he served Bekaa villages for about ten years. We do not choose one year without qualification. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jesuits in Europe</a></p></div></li>
<li><time>c. 1980</time><div><h2>Live Stations of the Cross</h2><p>Jesuit accounts describe an annual live Stations of the Cross with Barqa residents from around 1980. <a class='cite' href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>Jesuit retrospective</a></p></div></li>
<li><time>14 March 1985</time><div><h2>Kidnapped</h2><p>Father Nicolas was kidnapped in the Bekaa during the Lebanese Civil War. The sources reviewed here do not establish one perpetrator in a court-confirmed account. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jesuits in Europe</a></p></div></li>
<li><time>1 April 1985</time><div><h2>His body was found</h2><p>The Jesuit account reports that his body was found in a deep ravine. A later press article identifies his tomb at Deir Taanayel. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jesuits in Europe</a> · <a class='cite' href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>Nidaa Al Watan</a></p></div></li>
<li><time>1985</time><div><h2>Barqa health centre established in his memory</h2><p>The Lebanese Association of the Order of Malta dates the centre’s establishment to 1985, after his death. <a class='cite' href='https://malte-liban.org/centre-de-barqa/' target='_blank' rel='noopener noreferrer'>Association Malte Liban</a></p></div></li>
<li><time>22 January 2022</time><div><h2>Diocesan inquiry opened</h2><p>Bishop César Essayan opened the diocesan phase of the beatification cause in Beirut. This is a step in a Church process, not a beatification. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jesuit announcement</a></p></div></li>
</ol>
<p class='editorial-note'>Key dates are based on published sources. The exact start of his Barqa appointment, details of his final day and any cause developments after the inquiry opened require additional primary documentation.</p>
""",
        },
        "cause": {
            "title": "The beatification cause: what is known",
            "eyebrow": "Church process · last public documentation checked",
            "summary": "The diocesan phase of Father Nicolas’s cause opened on 22 January 2022. Any later stage should be supported by a Church announcement, not by rumor or expectation.",
            "body": """
<section class='prose'>
<div class='status-panel'><span class='status-dot'></span><div><strong>Publicly documented step in the sources reviewed</strong><p>The diocesan inquiry opened in Beirut in 2022. This page was checked on 5 November 2026.</p></div></div>
<h2>What happened in 2022</h2>
<p>The Jesuit Conference of European Provincials reported that Lebanese Bishop César Essayan opened the cause on 22 January 2022. It says an ecclesiastical tribunal would examine whether Kluiters died as a martyr under the Church’s definition. Opening a cause begins an investigation; it does not decide the outcome.</p>
<h2>What this site does not claim</h2>
<ul><li>We do not call him Blessed or Saint. We found no official beatification or canonization decree in the sources reviewed.</li><li>We do not say the case has been transmitted to Rome or that a miracle has been approved; we found no accessible official record confirming either claim.</li><li>We distinguish local Christian devotion and the word “martyr” used in remembrance from the Church judgment the cause is investigating.</li></ul>
<h2>What the terms mean</h2>
<p>The Vatican Dicastery for the Causes of Saints explains that a diocesan bishop collects and instructs a cause under established procedures; later stages involve examination by the Dicastery. The title “Servant of God,” used by Jesuit sources after the cause began, is not equivalent to beatification.</p>
<p class='source-line'><a class='button-link' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jesuit announcement of the opening ↗</a> <a class='quiet-link' href='https://www.vatican.va/content/romancuria/en/dicasteri/dicastero-cause-santi/profilo.html' target='_blank' rel='noopener noreferrer'>Vatican procedure overview ↗</a></p>
<div class='callout'><strong>If an official update appears</strong><p>This page should be revised with the announcement and date, quoting its stated stage rather than inferring progress from general language.</p></div>
</section>
""",
        },
        "places": {
            "title": "Places of memory and visiting",
            "eyebrow": "Barqa · health centre · Taanayel",
            "summary": "The Barqa health centre is verifiable. A press report identifies Father Nicolas’s tomb at Deir Taanayel. We found no announcement formally designating a sanctuary or approved shrine.",
            "body": """
<section class='place-grid'>
<article class='place-card'><p class='eyebrow'>Barqa · Bekaa</p><h2>Barqa Community Health Centre</h2><p>The Lebanese Association of the Order of Malta says the centre was established in 1985 in memory of Father Nicolas and is operated in cooperation with the Sisters of Jesus and Mary.</p><p><strong>Published address:</strong> Barqa, Bekaa<br><strong>Published local telephone:</strong> <a href='tel:28320490'>28-320490</a></p><p>No visiting hours are listed on the official centre page. Call before going; this archive is not an emergency-care directory.</p><div class='map-actions'><a class='button-link' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Order of Malta Lebanon listing ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Order+of+Malta+Barqa+Community+Health+Centre+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_BARQA}} ↗</a></div></article>
<article class='place-card'><p class='eyebrow'>Taanayel · Bekaa Valley</p><h2>Deir Taanayel and the reported tomb</h2><p>A 2025 Nidaa Al Watan report published a photograph captioned “the tomb of the martyred father at Deir Taanayel.” The article also reports a local request to move his remains to Barqa. We found no official source confirming that the request was accepted or that a transfer took place.</p><p>We therefore describe Taanayel as the burial site identified in a press report, not as an approved Church shrine. No public visiting hours or access arrangements were found.</p><div class='map-actions'><a class='button-link' href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>Read the report and view its photo ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Jesuit+Monastery+Taanayel+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_TAANAYEL}} ↗</a></div></article>
</section>
<section class='prose'><h2>Is there an official sanctuary?</h2><p>We found no Jesuit or Order of Malta notice designating an official sanctuary for Father Nicolas. The presence of his photographs in Barqa homes and local devotion described by reporters document community memory; they do not establish ecclesiastical status or pilgrimage arrangements.</p>
<h2>A short reflection</h2><div class='prayer-card'><p>God of peace, remember the people of Barqa and all who serve underserved communities. Give us courage to listen and work together, and protect victims of violence and their families. Amen.</p><span>Original editorial text for this site; not an official Church prayer or approved request for intercession.</span></div>
<p>For healthcare or to coordinate a centre visit, use the contact details published by the <a class='cite' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Order of Malta Lebanon</a>. For a religious visit, contact the relevant Church community in advance; we cannot confirm that the monastery is open to visitors.</p></section>
""",
        },
        "archive": {
            "title": "Photographic archive",
            "eyebrow": "Original photographs · published archive · contemporary work",
            "summary": "This gallery preserves the project photographs as supplied, adds historical images published and credited to the “Barqa Archive,” and includes a recent photograph of the health centre. Each image has a source and a note on its limits.",
            "body": """
<div class='gallery-intro'><p>The historical images below appear in Nidaa Al Watan’s 2025 feature, which credits a group of them to the Barqa Archive. They are loaded from the newspaper’s image server and linked to the original story; they are not re-uploaded to this repository. Rights remain with the image owners or publisher. Photographer names, dates and licences are welcome additions.</p><p>The “project” photographs are the five files supplied with this website. We do not have photographer or date information for each file.</p></div>
<div id='gallery' class='photo-grid'>{{GALLERY}}</div>
<section class='editorial-note'><p><strong>Visual distinctions:</strong> the colorized portrait is a digital restoration, not an original color photograph. The memorial artwork is contemporary, not a historical scene. No AI-generated image is presented as archival photography.</p></section>
""",
        },
        "sources": {
            "title": "Sources and research method",
            "eyebrow": "Open archive · reviewed 5 November 2026",
            "summary": "Claims link to sources near the text. We prioritize Jesuit sources, healthcare and university institutions, and established reporting, while identifying local testimony as testimony.",
            "body": """
<section class='prose'><h2>Source register</h2><p>This list gathers the principal references used on this site. Their evidentiary roles differ: institutional announcement, Jesuit biography, press reporting, authority record or local testimony. We do not treat them as interchangeable.</p></section>
<div class='source-list'>
<article><span class='source-type'>Jesuits · institutional report</span><h3>Beatification process of Dutch Jesuit started</h3><p>Reports the diocesan opening in Beirut, approximate duration of Bekaa ministry, kidnapping and recovery dates.</p><a href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jesuits in Europe ↗</a></article>
<article><span class='source-type'>Dutch Jesuits · biography</span><h3>Nico Kluiters SJ</h3><p>Institutional biography of his formation and ministry in Lebanon.</p><a href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>Jezuïeten ↗</a></article>
<article><span class='source-type'>Dutch Jesuits · testimony and history</span><h3>Martelaar voor geloof, gerechtigheid en vrede</h3><p>Jesuit account of reconciliation work and the live Stations of the Cross. Details are presented as a Jesuit retrospective and testimony, not as an administrative record for every project.</p><a href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>Jezuïeten ↗</a></article>
<article><span class='source-type'>Saint Joseph University · report</span><h3>Diocesan inquiry in Beirut</h3><p>University coverage of the church service and opening of the cause in January 2022.</p><a href='https://www.usj.edu.lb/news.php?id=11479' target='_blank' rel='noopener noreferrer'>Université Saint-Joseph ↗</a></article>
<article><span class='source-type'>Order of Malta · current listing</span><h3>Barqa Community Health Centre</h3><p>Published address, telephone and operating partnership with the Sisters of Jesus and Mary.</p><a href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Order of Malta Lebanon ↗</a></article>
<article><span class='source-type'>Order of Malta · 2026 update</span><h3>Grand Hospitaller visits Lebanon</h3><p>Confirms a 2026 visit to Barqa and identifies the centre as established in 1985 in memory of Father Nicolas.</p><a href='https://www.orderofmalta.int/news/grand-hospitaller-lebanon-healthcare-aid-order-of-malta-humanitarian-visit/' target='_blank' rel='noopener noreferrer'>Order of Malta ↗</a></article>
<article><span class='source-type'>Lebanese press · illustrated history</span><h3>When the priest became a homeland for Barqa</h3><p>A 2025 Arabic feature based on local testimony and archive material. Its image captions credit the Barqa Archive; the site preserves that credit and links to the publisher.</p><a href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>Nidaa Al Watan ↗</a></article>
<article><span class='source-type'>L’Orient-Le Jour · 2022 feature</span><h3>Passion et martyre</h3><p>French-language coverage of his studies, arrival in Lebanon and social-work background, with photographs credited to multiple sources.</p><a href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour ↗</a></article>
<article><span class='source-type'>L’Orient-Le Jour · 2026 photograph</span><h3>Visit to the Barqa centre</h3><p>Contemporary photo at the health centre, credited in the article to the Order of Malta Lebanon.</p><a href='https://www.lorientlejour.com/article/1497432/-vous-etes-un-modele-le-message-du-grand-hospitalier-a-lordre-de-malte-liban.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour ↗</a></article>
<article><span class='source-type'>Ignis · audio documentary</span><h3>Het levensverhaal van Nico Kluiters SJ</h3><p>Dutch audio documentary drawing on letters, testimony and interviews.</p><a href='https://igniswebmagazine.nl/kerk/audio-documentaire-nico-kluiters/' target='_blank' rel='noopener noreferrer'>Listen to the documentary ↗</a></article>
<article><span class='source-type'>Book</span><h3>Carole Dagher, <em>Passion pour une terre délaissée</em></h3><p>A full biography published in 2013; a Dutch translation appeared in 2023. The book is an important source for detail but is not fully available online.</p><a href='https://www.abdijvanberne.nl/nieuws/boekpresentatie-nicolaas-kluiters/' target='_blank' rel='noopener noreferrer'>2023 edition information ↗</a></article>
<article><span class='source-type'>Book and personal papers</span><h3>Frans Berkemeijer SJ, <em>Verzoeningsartiest in het gebroken Libanon</em></h3><p>A 2025 selection of letters, diary entries and testimony. The original papers are a useful research path for verifying details of his work.</p><a href='https://www.otheo.be/artikel/verzoeningsartiest-nicolaas-kluiters-stierf-40-jaar-geleden-marteldood-portret' target='_blank' rel='noopener noreferrer'>Book and context ↗</a></article>
<article><span class='source-type'>Reference record · limited data</span><h3>Wikidata and the German authority file</h3><p>Records basic birth details. The Wikidata item currently has no sitelink to a standalone Wikipedia biography; it is not used here for detailed life claims.</p><a href='https://www.wikidata.org/wiki/Q133745483' target='_blank' rel='noopener noreferrer'>Wikidata ↗</a></article>
<article><span class='source-type'>Vatican · institutional overview</span><h3>Dicastery for the Causes of Saints</h3><p>General explanation of the Dicastery’s role; it is not a case-specific update about Father Nicolas.</p><a href='https://www.vatican.va/content/romancuria/en/dicasteri/dicastero-cause-santi/profilo.html' target='_blank' rel='noopener noreferrer'>Vatican.va ↗</a></article>
</div>
<section class='prose'>
<h2>Wikipedia and social platforms</h2>
<p>Wikidata currently shows no sitelink to a standalone Wikipedia biography in English, Arabic or French, and its own record is sparse. Some broader Wikipedia-derived articles mention Kluiters, but they are not a sufficient biography.</p>
<p>News coverage reproduces photographs from the Barqa Archive; some images are described as having circulated on Facebook. We could not verify an official public Facebook or Instagram account dedicated to Father Nicolas. This site does not attribute accounts to his family, supporters or the cause; it links to the published stories that reproduced the images.</p>
<h2>Discrepancies we state openly</h2>
<ul><li>Sources differ on when his Barqa ministry began; we use “mid-1970s” and explain the difference.</li><li>We separate the reported kidnapping on 14 March 1985 from the Jesuit report that his body was found on 1 April.</li><li>We do not announce a cause stage after the diocesan opening unless we find a newer official notice.</li><li>A press report identifies a tomb at Deir Taanayel; no official confirmation of a transfer of remains or approved shrine was found.</li></ul>
<h2>Photographs and rights</h2>
<p>The five local files were supplied by the project owner; photographer, date and publication-rights details remain unknown. Barqa Archive images and the contemporary centre image load from the publishers’ servers with attribution and source links. They are not copied into this repository; rights remain with the image owners and publishers. Please contact the project owner with corrections or licensing details.</p>
</section>
""",
        },
    },
    "fr": {
        "index": {
            "title": "Une vie de foi et de service dans la Békaa",
            "eyebrow": "Biographie documentée · mémoire vivante de Barqa",
            "summary": "Le père Nicolas Kluiters était un jésuite néerlandais, artiste avant son ordination, puis prêtre et travailleur social auprès des villages du nord de la Békaa. Ces archives réunissent les faits documentés, son héritage concret et la mémoire toujours vivante à Barqa.",
            "body": """
<section class='feature-grid'>
  <a class='feature-card' href='life.html'><span class='card-number'>01</span><h2>L’homme et sa vocation</h2><p>De Delft, aux Pays-Bas, à la formation jésuite, au sacerdoce et à la mission au Liban.</p><span class='text-link'>Lire la biographie →</span></a>
  <a class='feature-card' href='barqa.html'><span class='card-number'>02</span><h2>Barqa : la foi en actes</h2><p>Pastorale, eau et accès aux terres, agriculture, éducation et santé : les partenaires sont nommés.</p><span class='text-link'>Découvrir Barqa →</span></a>
  <a class='feature-card' href='cause.html'><span class='card-number'>03</span><h2>Que signifie la cause de béatification ?</h2><p>L’enquête diocésaine s’est ouverte en 2022. Nous distinguons la dévotion locale des décisions officielles de l’Église.</p><span class='text-link'>Voir les faits établis →</span></a>
</section>
<section class='home-feature'>
  <div><p class='eyebrow'>La mémoire exige de la rigueur</p><h2>Conserver ce qui est connu. Dire ce qui ne l’est pas.</h2>
  <p>Les sources divergent sur l’année où le père Nicolas a commencé sa mission à Barqa. Les récits de ses derniers jours et de sa sépulture varient également. Nous citons les sources à proximité et distinguons les faits publiés des témoignages et de la dévotion populaire.</p>
  <a class='text-link' href='sources.html'>Comment ces archives ont été constituées →</a></div>
  <aside class='fact-box'><span class='fact-year'>22 · 01 · 2022</span><h3>Ouverture de l’enquête diocésaine</h3><p>La Conférence des provinciaux jésuites d’Europe a annoncé l’ouverture de la cause à Beyrouth. Cette ouverture n’est ni une béatification ni une canonisation.</p><a href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Lire l’annonce jésuite ↗</a></aside>
</section>
<section class='section-block'>
  <p class='eyebrow'>Un héritage qui se poursuit</p><h2>Le centre de santé de Barqa aujourd’hui</h2>
  <p>L’Association de l’Ordre de Malte au Liban indique que le centre de Barqa a été créé en 1985 en mémoire du père Nicolas et qu’il fonctionne avec les Sœurs de Jésus et de Marie. Cette institution a été créée après sa mort : nous ne la présentons pas comme son œuvre personnelle.</p>
  <a class='button-link' href='barqa.html#centre'>Informations et visite du centre</a>
</section>
<section class='editorial-note'><p>Ce projet documentaire est indépendant. Il ne représente ni la Compagnie de Jésus ni la cause de béatification. Les termes « Serviteur de Dieu » et ouverture d’une cause ne signifient pas que l’Église l’a béatifié ou canonisé.</p></section>
""",
        },
        "life": {
            "title": "De Delft à la Békaa",
            "eyebrow": "Biographie · 1940–1985",
            "summary": "Un artiste néerlandais entre dans la Compagnie de Jésus, se forme au Liban, puis exerce son ministère sacerdotal et social dans les villages du nord de la Békaa.",
            "body": """
<section class='prose-layout'><div class='prose'>
<h2>Art, formation et vocation</h2>
<p>Nicolas Kluiters naît à Delft, aux Pays-Bas, le 25 mai 1940. Il étudie les beaux-arts avant d’entrer chez les jésuites. Les récits jésuites décrivent un homme resté artiste après son choix du sacerdoce. Ces archives ne reproduisent pas de citations qui lui sont attribuées sans source publiée et vérifiable.</p>
<p>Une biographie jésuite situe son entrée dans la Compagnie de Jésus en 1966, année de son arrivée au Liban pour sa formation. Il étudie l’arabe et le travail social à Beyrouth, puis achève sa formation sacerdotale. Il est ordonné à Amsterdam à l’été 1973. Ces étapes figurent dans des sources jésuites et journalistiques.</p>
<h2>Liban : langue, société et ministère</h2>
<p>L’Université Saint-Joseph indique que Kluiters a appris l’arabe et étudié le travail social au Liban. Cette formation aide à comprendre une mission qui ne fut pas seulement pastorale : il cherchait à connaître les conditions de vie des villages, marginalisés par le manque d’infrastructures et la guerre.</p>
<p>Au milieu des années 1970, il sert des villages de la Békaa. Les sources divergent sur l’année exacte de son arrivée à Barqa : elles évoquent 1974, 1976 et 1977, tandis qu’une autre mentionne une nomination ultérieure. La chronologie emploie donc « milieu des années 1970 » et explique cette divergence au lieu d’imposer une date incertaine.</p>
<h2>Un artiste de la réconciliation</h2>
<p>Des récits jésuites et des témoignages de personnes qui l’ont connu évoquent ses efforts pour rapprocher les habitants par des initiatives sociales et pastorales et favoriser la réconciliation entre familles et communautés voisines. Une rétrospective jésuite rapporte que le chemin de croix vivant est devenu une tradition annuelle à Barqa vers 1980. Ce sont des souvenirs publiés, non un registre administratif indépendant de chaque projet.</p>
<div class='quote-card'><p>Les sources proches de sa vie le décrivent comme prêtre, artiste et travailleur social à la fois, sans le détacher des habitants et partenaires qui ont œuvré à ses côtés.</p><span>Note éditoriale des archives</span></div>
<h2>Enlèvement et mort</h2>
<p>Le 14 mars 1985, le père Nicolas est enlevé dans la Békaa, pendant la guerre civile libanaise. La Conférence des provinciaux jésuites d’Europe rapporte que son corps a été retrouvé le 1er avril dans un ravin profond. Nous ne désignons pas les auteurs ou leur mobile : les sources consultées ne permettent pas d’établir un récit unique et confirmé.</p>
<p>Un article de presse libanais situe sa tombe au monastère de Deir Taanayel. Nous le présentons comme un reportage illustré, pas comme un registre ecclésiastique des reliques ou un lieu de pèlerinage reconnu.</p>
<p class='source-line'>Pour aller plus loin : <a class='cite' href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>biographie des jésuites néerlandais</a> · <a class='cite' href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>article de L’Orient-Le Jour</a> · <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>annonce de la cause</a></p>
</div><aside class='side-portrait'><img src='{{ASSET}}portrait-formal.jpg' alt='Portrait d’archive du père Nicolas Kluiters, fourni par le propriétaire du projet' loading='lazy'><p>Image d’archive fournie par le propriétaire du projet. La date et le nom du photographe ne sont pas établis.</p><a href='archive.html'>Parcourir les photographies →</a></aside></section>
""",
        },
        "barqa": {
            "title": "Barqa et l’œuvre qui demeure",
            "eyebrow": "Lieu · communauté · services",
            "summary": "Barqa ne se réduit pas à la biographie d’un homme. L’héritage du père Nicolas est lié au travail des habitants, des sœurs, des jésuites, de l’Ordre de Malte et d’autres soutiens.",
            "body": """
<section class='prose'>
<h2>Les villages du nord de la Békaa</h2>
<p>Kluiters a servi plusieurs villages du nord de la Békaa, Barqa occupant une place centrale dans son ministère. Les sources jésuites décrivent une région rurale et défavorisée, touchée par la guerre et le manque d’infrastructures. Le nom du village apparaît sous plusieurs graphies latines, dont Barqa et Barka. Le site privilégie Barqa et برقا pour éviter la confusion avec d’autres lieux homonymes.</p>
<h2>Des projets concrets, un travail partagé</h2>
<p>Les récits publiés évoquent l’accès aux terres agricoles, des projets d’eau et d’irrigation, des vergers, l’éducation et les soins. Des témoignages locaux décrivent des initiatives collectives associant habitants, religieuses et organismes de soutien. Nous n’attribuons donc pas chaque bâtiment ou projet à une seule personne.</p>
<p>Les rétrospectives jésuites mettent l’accent sur le travail socio-pastoral et la réconciliation. Un récit local publié par Nidaa Al Watan en 2025 ajoute des témoignages sur les routes, l’eau, les vergers, l’école, un dispensaire et des ateliers. Ces éléments sont identifiés comme témoignages locaux publiés, pas comme un registre de projets audité.</p>
<h2 id='centre'>Centre de santé communautaire de Barqa</h2>
<p>L’Association de l’Ordre de Malte au Liban indique que le centre a été créé en 1985 en mémoire du père Nicolas. Sa fiche officielle précise qu’il fonctionne en collaboration avec les Sœurs de Jésus et de Marie. Un rapport de l’Ordre daté de 2026 confirme la visite du centre et la poursuite de son activité.</p>
<p><strong>Adresse publiée :</strong> Barqa, Békaa<br><strong>Téléphone local publié :</strong> <a href='tel:28320490'>28-320490</a></p>
<p>La fiche officielle ne publie pas les horaires ni le détail des services de ce centre particulier. Appelez avant de vous déplacer ; ces archives ne remplacent pas un service d’urgence.</p>
<div class='map-actions'><a class='button-link' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Fiche officielle du centre ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Order+of+Malta+Barqa+Community+Health+Centre+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_BARQA}} ↗</a></div>
<div class='callout'><strong>Une distinction importante</strong><p>Le centre de santé a été créé après la mort du père Nicolas. Ces archives documentent son lien mémoriel sans le présenter comme son fondateur personnel.</p></div>
<h2>Le village aujourd’hui</h2>
<p>L’Ordre de Malte inclut Barqa dans son réseau de centres de santé communautaires au Liban. Les estimations publiées du nombre de villages desservis varient selon les années ; nous ne reprenons pas un chiffre ancien comme s’il était actuel sans source officielle récente.</p>
<p class='source-line'>Sources : <a class='cite' href='https://malte-liban.org/centre-de-barqa/' target='_blank' rel='noopener noreferrer'>Association Malte Liban : centre de Barqa</a> · <a class='cite' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>fiche officielle du centre</a> · <a class='cite' href='https://www.orderofmalta.int/news/grand-hospitaller-lebanon-healthcare-aid-order-of-malta-humanitarian-visit/' target='_blank' rel='noopener noreferrer'>rapport de l’Ordre en 2026</a></p>
</section><figure class='wide-photo'><img src='https://s.lorientlejour.com/storage/attachments/1498/364623_364806.jpeg/r/800/364623_364806.jpeg' alt='Équipe de l’Ordre de Malte et personnel du centre de santé de Barqa ; photo fournie par l’Ordre de Malte Liban à L’Orient-Le Jour' loading='lazy' referrerpolicy='strict-origin-when-cross-origin'><figcaption>Visite du centre de santé de Barqa, 2026. Photo fournie par l’Ordre de Malte Liban à L’Orient-Le Jour. <a href='https://www.lorientlejour.com/article/1497432/-vous-etes-un-modele-le-message-du-grand-hospitalier-a-lordre-de-malte-liban.html' target='_blank' rel='noopener noreferrer'>Lire l’article et le crédit photo ↗</a></figcaption></figure>
""",
        },
        "timeline": {
            "title": "Chronologie",
            "eyebrow": "Repères documentés et divergences signalées",
            "summary": "Cette chronologie rassemble les événements appuyés par des sources publiées. En cas de divergence, elle indique une période ou expose le désaccord au lieu d’afficher une précision artificielle.",
            "body": """
<ol class='timeline-list'>
<li><time>25 mai 1940</time><div><h2>Naissance à Delft</h2><p>Nicolas Kluiters naît à Delft, aux Pays-Bas. <a class='cite' href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>Biographie jésuite néerlandaise</a></p></div></li>
<li><time>1966</time><div><h2>Entrée chez les jésuites et arrivée au Liban</h2><p>Des sources jésuites et journalistiques datent son entrée dans la Compagnie et son arrivée au Liban de cette année, après des études de beaux-arts. Il étudie l’arabe et le travail social à Beyrouth. <a class='cite' href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour</a></p></div></li>
<li><time>Été 1973</time><div><h2>Ordination sacerdotale</h2><p>Il est ordonné à Amsterdam, selon la biographie des jésuites néerlandais. <a class='cite' href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>Jésuites néerlandais</a></p></div></li>
<li><time>Milieu des années 1970</time><div><h2>Ministère pastoral dans le nord de la Békaa</h2><p>Les sources publiées divergent sur le début de son ministère à Barqa : 1974, 1976 ou 1977 ; un récit cite une nomination ultérieure. Les sources jésuites s’accordent sur environ dix années de service dans des villages de la Békaa. Nous ne retenons pas une seule date sans réserve. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jésuites d’Europe</a></p></div></li>
<li><time>Vers 1980</time><div><h2>Chemin de croix vivant</h2><p>Des récits jésuites évoquent une représentation annuelle du chemin de croix avec les habitants de Barqa à partir de 1980 environ. <a class='cite' href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>Rétrospective jésuite</a></p></div></li>
<li><time>14 mars 1985</time><div><h2>Enlèvement</h2><p>Le père Nicolas est enlevé dans la Békaa pendant la guerre civile libanaise. Les sources consultées ne désignent pas un auteur unique sur la base d’un jugement confirmé. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jésuites d’Europe</a></p></div></li>
<li><time>1 avril 1985</time><div><h2>Découverte de son corps</h2><p>La source jésuite indique que son corps a été retrouvé dans un ravin profond. Un article ultérieur situe sa tombe à Deir Taanayel. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jésuites d’Europe</a> · <a class='cite' href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>Nidaa Al Watan</a></p></div></li>
<li><time>1985</time><div><h2>Création du centre de santé en sa mémoire</h2><p>L’Association de l’Ordre de Malte au Liban date la création du centre de cette année, après sa mort. <a class='cite' href='https://malte-liban.org/centre-de-barqa/' target='_blank' rel='noopener noreferrer'>Association Malte Liban</a></p></div></li>
<li><time>22 janvier 2022</time><div><h2>Ouverture de l’enquête diocésaine</h2><p>L’évêque César Essayan ouvre la phase diocésaine de la cause à Beyrouth. Cette étape ne constitue pas une béatification. <a class='cite' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Annonce jésuite</a></p></div></li>
</ol>
<p class='editorial-note'>Les principales dates reposent sur des sources publiées. Le début exact de sa nomination à Barqa, les détails de sa dernière journée et toute évolution de la cause après l’ouverture nécessitent d’autres documents de première main.</p>
""",
        },
        "cause": {
            "title": "La cause de béatification : les faits connus",
            "eyebrow": "Procédure ecclésiale · dernières sources publiques vérifiées",
            "summary": "La phase diocésaine de la cause du père Nicolas s’est ouverte le 22 janvier 2022. Toute étape ultérieure doit être étayée par une annonce de l’Église, et non par une rumeur ou une attente.",
            "body": """
<section class='prose'>
<div class='status-panel'><span class='status-dot'></span><div><strong>Étape publique documentée dans les sources consultées</strong><p>Ouverture de l’enquête diocésaine à Beyrouth en 2022. Page vérifiée le 5 novembre 2026.</p></div></div>
<h2>Ce qui s’est passé en 2022</h2>
<p>La Conférence des provinciaux jésuites d’Europe rapporte que l’évêque libanais César Essayan a ouvert la cause le 22 janvier 2022. Elle indique qu’un tribunal ecclésiastique devait examiner si Kluiters était mort en martyr selon la définition de l’Église. L’ouverture lance une enquête ; elle n’en préjuge pas le résultat.</p>
<h2>Ce que ce site ne prétend pas</h2>
<ul><li>Nous ne le qualifions ni de bienheureux ni de saint. Nous n’avons trouvé aucun décret officiel de béatification ou de canonisation dans les sources consultées.</li><li>Nous n’affirmons pas que le dossier a été transmis à Rome ou qu’un miracle a été reconnu ; aucun document officiel accessible ne l’atteste.</li><li>Nous distinguons la dévotion chrétienne locale et l’emploi du mot « martyr » dans la mémoire de la décision ecclésiale que la cause examine.</li></ul>
<h2>Que signifient ces termes ?</h2>
<p>Le Dicastère du Vatican pour les Causes des Saints explique que l’évêque diocésain instruit la cause selon une procédure définie ; les étapes ultérieures relèvent de l’examen du Dicastère. Le titre de « Serviteur de Dieu », employé par les sources jésuites après l’ouverture de la cause, n’équivaut pas à une béatification.</p>
<p class='source-line'><a class='button-link' href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Annonce jésuite de l’ouverture ↗</a> <a class='quiet-link' href='https://www.vatican.va/content/romancuria/en/dicasteri/dicastero-cause-santi/profilo.html' target='_blank' rel='noopener noreferrer'>Présentation de la procédure du Vatican ↗</a></p>
<div class='callout'><strong>En cas d’annonce officielle</strong><p>Cette page devra être mise à jour en indiquant l’annonce et sa date, sans déduire une nouvelle étape de formulations générales.</p></div>
</section>
""",
        },
        "places": {
            "title": "Lieux de mémoire et visite",
            "eyebrow": "Barqa · centre de santé · Taanayel",
            "summary": "Le centre de santé de Barqa est vérifiable. Un article de presse situe la tombe du père Nicolas à Deir Taanayel. Nous n’avons trouvé aucune annonce désignant officiellement un sanctuaire ou un lieu de pèlerinage reconnu.",
            "body": """
<section class='place-grid'>
<article class='place-card'><p class='eyebrow'>Barqa · Békaa</p><h2>Centre de santé communautaire</h2><p>L’Association de l’Ordre de Malte au Liban indique que le centre a été créé en 1985 en mémoire du père Nicolas et qu’il fonctionne avec les Sœurs de Jésus et de Marie.</p><p><strong>Adresse publiée :</strong> Barqa, Békaa<br><strong>Téléphone local publié :</strong> <a href='tel:28320490'>28-320490</a></p><p>La fiche officielle ne publie pas d’horaires de visite. Appelez avant de vous déplacer ; ces archives ne sont pas un annuaire d’urgence.</p><div class='map-actions'><a class='button-link' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Fiche de l’Ordre de Malte Liban ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Order+of+Malta+Barqa+Community+Health+Centre+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_BARQA}} ↗</a></div></article>
<article class='place-card'><p class='eyebrow'>Taanayel · vallée de la Békaa</p><h2>Deir Taanayel et la tombe rapportée</h2><p>En 2025, Nidaa Al Watan a publié une photo légendée « tombe du père martyr à Deir Taanayel ». L’article évoque aussi une demande locale de transfert de sa dépouille à Barqa. Nous n’avons trouvé aucune source officielle confirmant l’acceptation ou la réalisation d’un transfert.</p><p>Nous présentons donc Taanayel comme le lieu de sépulture identifié dans un reportage, et non comme un sanctuaire reconnu par l’Église. Aucun horaire de visite ou accès public n’a été trouvé.</p><div class='map-actions'><a class='button-link' href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>Lire l’article et voir la photo ↗</a><a class='quiet-link' href='https://www.google.com/maps/search/?api=1&amp;query=Jesuit+Monastery+Taanayel+Lebanon' target='_blank' rel='noopener noreferrer'>{{MAP_TAANAYEL}} ↗</a></div></article>
</section>
<section class='prose'><h2>Existe-t-il un sanctuaire officiel ?</h2><p>Nous n’avons trouvé aucune communication jésuite ou de l’Ordre de Malte désignant un sanctuaire officiel consacré au père Nicolas. Les photos présentes dans les foyers de Barqa et la dévotion locale décrite par des journalistes témoignent d’une mémoire communautaire, mais n’établissent ni statut ecclésial ni organisation de pèlerinage.</p>
<h2>Brève réflexion</h2><div class='prayer-card'><p>Dieu de paix, souviens-toi des habitants de Barqa et de tous ceux qui servent des communautés délaissées. Donne-nous le courage d’écouter et d’agir ensemble ; protège les victimes de la violence et leurs familles. Amen.</p><span>Texte éditorial original pour ce site ; prière non officielle, sans demande d’intercession approuvée.</span></div>
<p>Pour les soins ou pour organiser une visite du centre, utilisez les coordonnées publiées par l’<a class='cite' href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Ordre de Malte Liban</a>. Pour une visite religieuse, contactez à l’avance la communauté ecclésiale concernée ; nous ne pouvons confirmer l’ouverture du monastère au public.</p></section>
""",
        },
        "archive": {
            "title": "Archives photographiques",
            "eyebrow": "Images originales · archives publiées · création contemporaine",
            "summary": "La galerie conserve les photographies fournies pour le projet, ajoute des images historiques créditées à l’« Archive de Barqa » dans la presse et une photographie récente du centre de santé. Chaque image comporte une source et une note sur ses limites.",
            "body": """
<div class='gallery-intro'><p>Les images historiques ci-dessous figurent dans le reportage 2025 de Nidaa Al Watan, qui en attribue plusieurs à l’Archive de Barqa. Elles sont chargées depuis le serveur du journal et liées à l’article original ; elles ne sont pas copiées dans ce dépôt. Les droits restent à leurs propriétaires ou à l’éditeur. Les noms des photographes, dates et licences peuvent être ajoutés s’ils sont connus.</p><p>Les images « projet » sont les cinq fichiers fournis avec le site. Nous n’avons pas les informations de photographe ou de date pour chaque fichier.</p></div>
<div id='gallery' class='photo-grid'>{{GALLERY}}</div>
<section class='editorial-note'><p><strong>Distinctions visuelles :</strong> le portrait colorisé est une restauration numérique, non une photographie couleur originale. L’œuvre commémorative est contemporaine, pas une scène historique. Aucune image générée par IA n’est présentée comme archive.</p></section>
""",
        },
        "sources": {
            "title": "Sources et méthode de recherche",
            "eyebrow": "Archives ouvertes · revues le 5 novembre 2026",
            "summary": "Les affirmations renvoient aux sources près du texte. Nous privilégions les sources jésuites, universitaires et sanitaires ainsi que la presse reconnue, en identifiant les témoignages locaux comme tels.",
            "body": """
<section class='prose'><h2>Registre des sources</h2><p>Cette liste rassemble les principales références utilisées. Leur valeur documentaire diffère : annonce institutionnelle, biographie jésuite, reportage, notice d’autorité ou témoignage local. Nous ne les traitons pas comme des preuves interchangeables.</p></section>
<div class='source-list'>
<article><span class='source-type'>Jésuites · annonce institutionnelle</span><h3>Beatification process of Dutch Jesuit started</h3><p>Annonce l’ouverture diocésaine à Beyrouth, la durée approximative du ministère dans la Békaa, l’enlèvement et la découverte du corps.</p><a href='https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started' target='_blank' rel='noopener noreferrer'>Jesuits in Europe ↗</a></article>
<article><span class='source-type'>Jésuites néerlandais · biographie</span><h3>Nico Kluiters SJ</h3><p>Biographie institutionnelle de sa formation et de sa mission au Liban.</p><a href='https://www.jezuieten.org/person/nico-kluiters-sj/' target='_blank' rel='noopener noreferrer'>Jezuïeten ↗</a></article>
<article><span class='source-type'>Jésuites néerlandais · témoignage et histoire</span><h3>Martelaar voor geloof, gerechtigheid en vrede</h3><p>Récit jésuite des initiatives de réconciliation et du chemin de croix vivant. Ces détails sont présentés comme une rétrospective et des témoignages, non comme un registre administratif indépendant de chaque projet.</p><a href='https://www.jezuieten.org/nieuws/nico-kluiters-sj-martelaar-voor-geloof-gerechtigheid-en-vrede/' target='_blank' rel='noopener noreferrer'>Jezuïeten ↗</a></article>
<article><span class='source-type'>Université Saint-Joseph · actualité</span><h3>Enquête diocésaine à Beyrouth</h3><p>Couverture universitaire de la célébration et de l’ouverture de la cause en janvier 2022.</p><a href='https://www.usj.edu.lb/news.php?id=11479' target='_blank' rel='noopener noreferrer'>Université Saint-Joseph ↗</a></article>
<article><span class='source-type'>Ordre de Malte · fiche actuelle</span><h3>Centre de santé communautaire de Barqa</h3><p>Adresse et téléphone publiés, ainsi que le partenariat avec les Sœurs de Jésus et de Marie.</p><a href='https://orderofmaltalebanon.org/center/barqa-bekaa' target='_blank' rel='noopener noreferrer'>Order of Malta Lebanon ↗</a></article>
<article><span class='source-type'>Ordre de Malte · mise à jour 2026</span><h3>Visite du Grand Hospitalier au Liban</h3><p>Confirme une visite à Barqa en 2026 et situe la création du centre en 1985 en mémoire du père Nicolas.</p><a href='https://www.orderofmalta.int/news/grand-hospitaller-lebanon-healthcare-aid-order-of-malta-humanitarian-visit/' target='_blank' rel='noopener noreferrer'>Ordre de Malte ↗</a></article>
<article><span class='source-type'>Presse libanaise · histoire illustrée</span><h3>Quand le prêtre est devenu une patrie pour Barqa</h3><p>Reportage arabe de 2025 fondé sur des témoignages locaux et des archives. Les légendes créditent l’Archive de Barqa ; nous conservons ce crédit et renvoyons vers l’éditeur.</p><a href='https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7' target='_blank' rel='noopener noreferrer'>Nidaa Al Watan ↗</a></article>
<article><span class='source-type'>L’Orient-Le Jour · reportage 2022</span><h3>Passion et martyre</h3><p>Article en français sur ses études, son arrivée au Liban et sa formation en travail social ; il contient des photographies de sources diverses.</p><a href='https://www.lorientlejour.com/article/1290267/passion-et-martyre-du-pretre-jesuite-nicolas-kluiters-enleve-et-tue-en-1985-dans-la-bekaa.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour ↗</a></article>
<article><span class='source-type'>L’Orient-Le Jour · photographie 2026</span><h3>Visite du centre de Barqa</h3><p>Photo contemporaine prise au centre de santé, créditée à l’Ordre de Malte Liban.</p><a href='https://www.lorientlejour.com/article/1497432/-vous-etes-un-modele-le-message-du-grand-hospitalier-a-lordre-de-malte-liban.html' target='_blank' rel='noopener noreferrer'>L’Orient-Le Jour ↗</a></article>
<article><span class='source-type'>Ignis · documentaire audio</span><h3>Het levensverhaal van Nico Kluiters SJ</h3><p>Documentaire audio néerlandais fondé sur des lettres, témoignages et entretiens.</p><a href='https://igniswebmagazine.nl/kerk/audio-documentaire-nico-kluiters/' target='_blank' rel='noopener noreferrer'>Écouter le documentaire ↗</a></article>
<article><span class='source-type'>Livre</span><h3>Carole Dagher, <em>Passion pour une terre délaissée</em></h3><p>Biographie publiée en 2013 ; une traduction néerlandaise paraît en 2023. Le livre est une source importante, mais son texte intégral n’est pas disponible gratuitement sur le web.</p><a href='https://www.abdijvanberne.nl/nieuws/boekpresentatie-nicolaas-kluiters/' target='_blank' rel='noopener noreferrer'>Présentation de l’édition 2023 ↗</a></article>
<article><span class='source-type'>Livre et papiers personnels</span><h3>Frans Berkemeijer SJ, <em>Verzoeningsartiest in het gebroken Libanon</em></h3><p>Sélection de lettres, journaux et témoignages publiée en 2025. Les documents originaux sont une piste importante pour vérifier les détails de son action.</p><a href='https://www.otheo.be/artikel/verzoeningsartiest-nicolaas-kluiters-stierf-40-jaar-geleden-marteldood-portret' target='_blank' rel='noopener noreferrer'>Livre et contexte ↗</a></article>
<article><span class='source-type'>Notice de référence · données limitées</span><h3>Wikidata et fichier d’autorité allemand</h3><p>Enregistrent les données de naissance principales. L’élément Wikidata n’a pas de lien vers une biographie Wikipédia indépendante ; il n’est pas utilisé ici pour les détails biographiques.</p><a href='https://www.wikidata.org/wiki/Q133745483' target='_blank' rel='noopener noreferrer'>Wikidata ↗</a></article>
<article><span class='source-type'>Vatican · présentation institutionnelle</span><h3>Dicastère pour les Causes des Saints</h3><p>Présentation générale du rôle du Dicastère ; ce n’est pas une mise à jour sur le dossier du père Nicolas.</p><a href='https://www.vatican.va/content/romancuria/en/dicasteri/dicastero-cause-santi/profilo.html' target='_blank' rel='noopener noreferrer'>Vatican.va ↗</a></article>
</div>
<section class='prose'>
<h2>Wikipédia et réseaux sociaux</h2>
<p>Wikidata n’affiche actuellement aucun lien vers une biographie Wikipédia indépendante en anglais, en arabe ou en français, et sa notice reste succincte. Certaines pages Wikipédia consacrées à des événements plus larges mentionnent Kluiters, mais elles ne constituent pas une biographie suffisante.</p>
<p>Des médias reproduisent des photos de l’Archive de Barqa ; certaines sont décrites comme ayant circulé sur Facebook. Nous n’avons pas pu vérifier de compte public officiel consacré au père Nicolas sur Facebook ou Instagram. Ce site n’attribue aucun compte à sa famille, aux personnes qui le soutiennent ou à la cause ; il renvoie vers les publications qui ont diffusé les images.</p>
<h2>Divergences signalées</h2>
<ul><li>Les sources divergent sur le début de sa mission à Barqa ; nous employons « milieu des années 1970 » et expliquons la divergence.</li><li>Nous distinguons l’enlèvement du 14 mars 1985 de la découverte du corps le 1er avril.</li><li>Nous n’annonçons aucune étape ultérieure à l’ouverture diocésaine sans notice officielle plus récente.</li><li>Un reportage situe une tombe à Deir Taanayel ; aucun transfert de dépouille ni sanctuaire reconnu n’a été confirmé officiellement.</li></ul>
<h2>Photographies et droits</h2>
<p>Les cinq fichiers locaux ont été fournis par le propriétaire du projet ; leurs photographes, dates et droits de publication restent inconnus. Les images de l’Archive de Barqa et la photo contemporaine du centre sont chargées depuis les serveurs des éditeurs, avec crédit et lien vers la source. Elles ne sont pas copiées dans ce dépôt ; les droits restent à leurs propriétaires et éditeurs. Le propriétaire du projet peut transmettre corrections ou informations de licence.</p>
</section>
""",
        },
    },
}

GALLERY = [
    {
        "src": "portrait-archive.jpg", "alt": {
            "ar": "صورة أرشيفية بالأبيض والأسود للأب نيكولا كلويترز",
            "en": "Black-and-white archival portrait of Father Nicolas Kluiters",
            "fr": "Portrait d’archive en noir et blanc du père Nicolas Kluiters"},
        "caption": {"ar": "بورتريه أرشيفي أبيض وأسود — من ملفات المشروع", "en": "Black-and-white archival portrait — supplied with the project", "fr": "Portrait d’archive en noir et blanc — fourni avec le projet"},
        "credit": {"ar": "المصوّر والتاريخ غير معروفين", "en": "Photographer and date unknown", "fr": "Photographe et date inconnus"}, "source": None,
    },
    {
        "src": "portrait-formal.jpg", "alt": {
            "ar": "بورتريه تاريخي رسمي للأب نيكولا كلويترز",
            "en": "Formal archival portrait of Father Nicolas Kluiters",
            "fr": "Portrait d’archive officiel du père Nicolas Kluiters"},
        "caption": {"ar": "بورتريه رسمي — من ملفات المشروع", "en": "Formal portrait — supplied with the project", "fr": "Portrait officiel — fourni avec le projet"},
        "credit": {"ar": "المصوّر والتاريخ غير معروفين", "en": "Photographer and date unknown", "fr": "Photographe et date inconnus"}, "source": None,
    },
    {
        "src": "barqa-community.jpg", "alt": {
            "ar": "صورة أرشيفية للأب نيكولا بين أهالي برقا",
            "en": "Archival photograph of Father Nicolas with people from Barqa",
            "fr": "Photographie d’archive du père Nicolas avec des habitants de Barqa"},
        "caption": {"ar": "الأب نيكولا مع أهالي برقا — من ملفات المشروع", "en": "Father Nicolas with Barqa residents — supplied with the project", "fr": "Le père Nicolas avec des habitants de Barqa — fourni avec le projet"},
        "credit": {"ar": "المصوّر والتاريخ غير معروفين", "en": "Photographer and date unknown", "fr": "Photographe et date inconnus"}, "source": None,
    },
    {
        "src": "portrait-restored.jpg", "alt": {
            "ar": "نسخة ملوّنة رقميًا من بورتريه أرشيفي للأب نيكولا",
            "en": "Digitally colorized version of an archival portrait of Father Nicolas",
            "fr": "Version colorisée numériquement d’un portrait d’archive du père Nicolas"},
        "caption": {"ar": "نسخة ملوّنة رقميًا — ليست صورة ملوّنة أصلية", "en": "Digitally colorized — not an original color photograph", "fr": "Colorisation numérique — pas une photographie couleur originale"},
        "credit": {"ar": "الصورة الملوّنة من ملفات المشروع", "en": "Colorized image supplied with the project", "fr": "Image colorisée fournie avec le projet"}, "source": None,
    },
    {
        "src": "memorial-art.jpg", "alt": {
            "ar": "عمل فني تذكاري معاصر للأب نيكولا",
            "en": "Contemporary memorial artwork for Father Nicolas",
            "fr": "Œuvre commémorative contemporaine pour le père Nicolas"},
        "caption": {"ar": "عمل فني معاصر — ليس مشهدًا تاريخيًا", "en": "Contemporary memorial artwork — not a historical scene", "fr": "Œuvre commémorative contemporaine — pas une scène historique"},
        "credit": {"ar": "عمل فني مقدّم ضمن المشروع", "en": "Artwork supplied with the project", "fr": "Œuvre fournie avec le projet"}, "source": None,
    },
]

ARCHIVE_SOURCE = "https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7"
for src, captions, alts in [
    ("https://s2.nidaalwatan.com/storage/attachments/356/472692833_577764571555839_4245693544345986385_n_313234_367115.jpg",
     {"ar": "خادم الله الأب نيكولا كلويترز", "en": "Father Nicolas Kluiters, credited to the Barqa Archive", "fr": "Le père Nicolas Kluiters, crédité à l’Archive de Barqa"},
     {"ar": "بورتريه أرشيفي للأب نيكولا", "en": "Archival portrait of Father Nicolas", "fr": "Portrait d’archive du père Nicolas"}),
    ("https://s2.nidaalwatan.com/storage/attachments/356/496771511_3861055524155916_3685919946687135725_n_185266_816423.jpg",
     {"ar": "الأب نيكولا مع أهل برقا — أرشيف برقا", "en": "Father Nicolas with Barqa residents — Barqa Archive", "fr": "Le père Nicolas avec des habitants de Barqa — Archive de Barqa"},
     {"ar": "الأب نيكولا مع أفراد من مجتمع برقا", "en": "Father Nicolas with members of the Barqa community", "fr": "Le père Nicolas avec des membres de la communauté de Barqa"}),
    ("https://s2.nidaalwatan.com/storage/attachments/356/494378919_3850535191874616_6577962576275224122_n_480590_144968.jpg",
     {"ar": "الأب نيكولا مع أهل برقا — أرشيف برقا", "en": "Father Nicolas with Barqa residents — Barqa Archive", "fr": "Le père Nicolas avec des habitants de Barqa — Archive de Barqa"},
     {"ar": "صورة جماعية أرشيفية في برقا", "en": "Archival group photograph in Barqa", "fr": "Photo de groupe d’archive à Barqa"}),
    ("https://s2.nidaalwatan.com/storage/attachments/356/493719462_3847399625521506_8597988129800384968_n_382882_871408.jpg",
     {"ar": "الأب كلويترز يحتفل بعيد الميلاد — أرشيف برقا", "en": "Father Kluiters celebrating Christmas — Barqa Archive", "fr": "Le père Kluiters célébrant Noël — Archive de Barqa"},
     {"ar": "الأب نيكولا خلال احتفال بعيد الميلاد", "en": "Father Nicolas during a Christmas celebration", "fr": "Le père Nicolas lors d’une célébration de Noël"}),
    ("https://s2.nidaalwatan.com/storage/attachments/356/473765231_582686537730309_6187923513685613451_n_680496_398571.jpg",
     {"ar": "من مراحل درب الصليب الحيّ — أرشيف برقا", "en": "A scene from the live Stations of the Cross — Barqa Archive", "fr": "Scène du chemin de croix vivant — Archive de Barqa"},
     {"ar": "مشهد تمثيلي من درب الصليب في برقا", "en": "A reenactment from the Stations of the Cross in Barqa", "fr": "Représentation du chemin de croix à Barqa"}),
    ("https://s2.nidaalwatan.com/storage/attachments/356/473680062_582706584394971_3297996482130918404_n_679353_731109.jpg",
     {"ar": "مشهد من خميس الأسرار — أرشيف برقا", "en": "A Holy Thursday scene — Barqa Archive", "fr": "Scène du Jeudi saint — Archive de Barqa"},
     {"ar": "مشهد طقسي في برقا يوم خميس الأسرار", "en": "A Holy Thursday ritual scene in Barqa", "fr": "Scène rituelle du Jeudi saint à Barqa"}),
    ("https://s2.nidaalwatan.com/storage/attachments/356/480340708_606445855354377_6835993966216667492_n_891061_329654.jpg",
     {"ar": "مشهد من خميس الأسرار — أرشيف برقا", "en": "A Holy Thursday scene — Barqa Archive", "fr": "Scène du Jeudi saint — Archive de Barqa"},
     {"ar": "صورة أرشيفية لمشهد طقسي في برقا", "en": "Archival image of a ritual scene in Barqa", "fr": "Image d’archive d’une scène rituelle à Barqa"}),
    ("https://s2.nidaalwatan.com/storage/attachments/356/472456604_577764541555842_8814495587850553525_n_904332_630866_108061.jpg",
     {"ar": "الأب كلويترز مع أخويات فرسان العذراء — أرشيف برقا", "en": "Father Kluiters with the Marian sodalities — Barqa Archive", "fr": "Le père Kluiters avec des confréries mariales — Archive de Barqa"},
     {"ar": "الأب نيكولا مع مجموعة من أبناء برقا", "en": "Father Nicolas with a group from Barqa", "fr": "Le père Nicolas avec un groupe d’habitants de Barqa"}),
    ("https://s2.nidaalwatan.com/storage/attachments/356/tomb-of-father-nicolas_575915_716579.png",
     {"ar": "صورة الضريح المنشورة في نداء الوطن بعنوان «ضريح الأب الشهيد في دير تعنايل»", "en": "Tomb image published by Nidaa Al Watan, captioned as Father Nicolas’s tomb at Deir Taanayel", "fr": "Photo publiée par Nidaa Al Watan, légendée comme la tombe du père Nicolas à Deir Taanayel"},
     {"ar": "ضريح منسوب للأب نيكولا في دير تعنايل بحسب تسمية الصحيفة", "en": "A tomb identified as Father Nicolas’s at Deir Taanayel in the newspaper caption", "fr": "Tombe attribuée au père Nicolas à Deir Taanayel selon la légende du journal"}),
]:
    GALLERY.append({"src": src, "alt": alts, "caption": captions,
                    "credit": {"ar": "أرشيف برقا كما نشرته نداء الوطن، 2025", "en": "Barqa Archive, published by Nidaa Al Watan, 2025", "fr": "Archive de Barqa, publiée par Nidaa Al Watan, 2025"},
                    "source": ARCHIVE_SOURCE})

GALLERY.append({
    "src": "https://s.lorientlejour.com/storage/attachments/1498/364623_364806.jpeg/r/800/364623_364806.jpeg",
    "alt": {"ar": "وفد جمعية مالطا وفريق المركز الصحي في برقا عام 2026", "en": "Order of Malta delegation and health-centre team in Barqa in 2026", "fr": "Délégation de l’Ordre de Malte et équipe du centre de santé à Barqa en 2026"},
    "caption": {"ar": "زيارة مركز برقا الصحي، 2026", "en": "Visit to Barqa Community Health Centre, 2026", "fr": "Visite du centre de santé de Barqa, 2026"},
    "credit": {"ar": "الصورة مقدّمة من جمعية مالطا لبنان إلى L’Orient-Le Jour", "en": "Photo supplied by the Order of Malta Lebanon to L’Orient-Le Jour", "fr": "Photo fournie par l’Ordre de Malte Liban à L’Orient-Le Jour"},
    "source": "https://www.lorientlejour.com/article/1497432/-vous-etes-un-modele-le-message-du-grand-hospitalier-a-lordre-de-malte-liban.html",
})

def safe_external(s):
    return s.replace("&", "&amp;")

def locale_path(lang, page):
    filename = "index.html" if page == "index" else page + ".html"
    if lang == "ar":
        return "/" + filename
    return f"/{lang}/{filename}"

def gallery_html(lang, asset_prefix):
    T = TEXT[lang]
    blocks = []
    for i, item in enumerate(GALLERY):
        src = asset_prefix + item["src"] if item["source"] is None else item["src"]
        full_link = item["source"] or src
        label = item["caption"][lang]
        credit = item["credit"][lang]
        source_link = ""
        if item["source"]:
            source_link = f"<a class='photo-source' href='{item['source']}' target='_blank' rel='noopener noreferrer'>{T['source_label']}: {credit} ↗</a>"
        else:
            source_link = f"<span class='photo-source'>{T['photo_label']}: {credit}</span>"
        blocks.append(
            f"<figure class='photo-card'><a class='photo-image-link' href='{full_link}' target='_blank' rel='noopener noreferrer' aria-label='{escape(T['open_image'])}: {escape(item['alt'][lang], quote=True)}'><img src='{src}' alt='{escape(item['alt'][lang], quote=True)}' loading='lazy' referrerpolicy='strict-origin-when-cross-origin' {'fetchpriority=high' if i == 0 else ''}></a><figcaption><strong>{label}</strong>{source_link}</figcaption></figure>"
        )
    return "\n".join(blocks)

def nav_href(lang, slug, current_lang):
    filename = "index.html" if slug == "index" else slug + ".html"
    if lang == current_lang:
        return filename
    if current_lang == "ar":
        return f"{lang}/{filename}"
    if lang == "ar":
        return "../" + filename
    return f"../{lang}/{filename}"

def render(lang, slug):
    data, T = CONTENT[lang][slug], TEXT[lang]
    root_level = lang == "ar"
    asset_prefix = "assets/" if root_level else "../assets/"
    rtl = lang == "ar"
    filename = "index.html" if slug == "index" else slug + ".html"
    canonical = BASE + locale_path(lang, slug)
    nav_links = []
    for i, item in enumerate(PAGES):
        target = nav_href(lang, item, lang)
        nav_links.append(f"<a href='{target}' {'aria-current=page' if item == slug else ''}>{NAV[lang][i]}</a>")
    language_links = []
    for target_lang in LOCALES:
        language_links.append(
            f"<a href='{nav_href(target_lang, slug, lang)}' lang='{target_lang}' hreflang='{target_lang}' {'aria-current=true' if target_lang == lang else ''}>{'ع' if target_lang == 'ar' else target_lang.upper()}</a>"
        )
    body = data["body"].replace("{{ASSET}}", asset_prefix)
    body = body.replace("{{GALLERY}}", gallery_html(lang, asset_prefix))
    body = body.replace("{{MAP_BARQA}}", T["map_barqa"])
    body = body.replace("{{MAP_TAANAYEL}}", T["map_taanayel"])
    page_nav = f"<nav class='main-nav' aria-label='{escape(T['menu'], quote=True)}'>{''.join(nav_links)}</nav>"
    return f"""<!doctype html>
<html lang='{lang}' dir='{'rtl' if rtl else 'ltr'}'>
<head>
<meta charset='utf-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<meta name='theme-color' content='#17241f'>
<meta name='description' content='{escape(data['summary'], quote=True)}'>
<meta property='og:type' content='website'>
<meta property='og:title' content='{escape(data['title'], quote=True)} · {escape(T['site'], quote=True)}'>
<meta property='og:description' content='{escape(data['summary'], quote=True)}'>
<meta property='og:image' content='{BASE}/assets/portrait-archive.jpg'>
<link rel='canonical' href='{canonical}'>
<link rel='alternate' hreflang='ar' href='{BASE}{locale_path('ar', slug)}'>
<link rel='alternate' hreflang='en' href='{BASE}{locale_path('en', slug)}'>
<link rel='alternate' hreflang='fr' href='{BASE}{locale_path('fr', slug)}'>
<link rel='alternate' hreflang='x-default' href='{BASE}{locale_path('en', slug)}'>
<link rel='preconnect' href='https://fonts.googleapis.com'>
<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>
<link href='https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Naskh+Arabic:wght@400;500;600;700&display=swap' rel='stylesheet'>
<link rel='stylesheet' href='{asset_prefix}site.css'>
<title>{escape(data['title'])} · {escape(T['site'])}</title>
</head>
<body>
<a class='skip-link' href='#main'>{T['skip']}</a>
<header class='site-header'>
  <div class='header-top'>
    <a class='brand' href='{nav_href(lang, 'index', lang)}'><span class='brand-mark'>NK</span><span><strong>{T['site']}</strong><small>{T['tagline']}</small></span></a>
    <div class='language-switch' aria-label='{T['langname']}'>{''.join(language_links)}</div>
  </div>
  {page_nav}
</header>
<main id='main'>
  <section class='page-hero {'home-hero' if slug == 'index' else ''}'>
    <div class='page-hero-copy'>
      <p class='eyebrow'>{data['eyebrow']}</p>
      <h1>{data['title']}</h1>
      <p class='page-summary'>{data['summary']}</p>
      {f"<a class='hero-link' href='life.html'>{'ابدأ بالسيرة' if lang == 'ar' else ('Start with the biography' if lang == 'en' else 'Commencer par la biographie')} <span aria-hidden='true'>↗</span></a>" if slug == 'index' else ''}
    </div>
    {f"<div class='hero-image'><img src='{asset_prefix}portrait-archive.jpg' alt='{'صورة أرشيفية بالأبيض والأسود للأب نيكولا كلويترز' if lang == 'ar' else ('Black-and-white archival portrait of Father Nicolas Kluiters' if lang == 'en' else 'Portrait d’archive en noir et blanc du père Nicolas Kluiters')}' fetchpriority='high'><span>{'صورة أرشيفية' if lang == 'ar' else ('Archival photograph' if lang == 'en' else 'Photographie d’archive')}</span></div>" if slug == 'index' else ''}
  </section>
  <article class='page-content'>{body}</article>
</main>
<footer class='site-footer'>
  <div><a class='footer-brand' href='{nav_href(lang, 'index', lang)}'>{T['site']}</a><p>{T['footer_note']}</p></div>
  <div class='footer-meta'><a href='{nav_href(lang, 'sources', lang)}'>{T['source_note']}</a><span>{T['updated']}</span><span>1940–1985 · Barqa · Lebanon</span></div>
</footer>
</body>
</html>
"""

def main():
    for lang in ("en", "fr"):
        folder = ROOT / lang
        folder.mkdir(exist_ok=True)
        for slug in PAGES:
            (folder / (("index.html") if slug == "index" else slug + ".html")).write_text(render(lang, slug), encoding="utf-8")
    for slug in PAGES:
        (ROOT / (("index.html") if slug == "index" else slug + ".html")).write_text(render("ar", slug), encoding="utf-8")
    url_list = []
    for lang in LOCALES:
        for slug in PAGES:
            url_list.append(f"<url><loc>{BASE}{locale_path(lang, slug)}</loc><lastmod>{UPDATED}</lastmod></url>")
    sitemap = "<?xml version='1.0' encoding='UTF-8'?>\n<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n" + "\n".join(url_list) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    print(f"Built {len(PAGES) * len(LOCALES)} localized pages and Arabic root pages.")

if __name__ == "__main__":
    main()
