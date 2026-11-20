import streamlit as st
import streamlit.components.v1 as components
from html import escape

# ==============================================================
# إعدادات الصفحة وعنوان التبويب
# ==============================================================
st.set_page_config(
    page_title="الخدمات و الاستشارات الفلكية",
    page_icon="✨",
    layout="centered"
)

# ==============================================================
# كود CSS: ثيم داكن احترافي + دعم العربية (يمين لليسار)
# ==============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

:root {
    --bg-main: #0a0e1a;
    --bg-card: #121829;
    --bg-input: #161d33;
    --bg-hover: #222b4d;
    --border: #2a3356;
    --text-main: #eef1f9;
    --text-soft: #b4bcd6;
    --gold: #f5c46b;
    --gold-soft: #ffe1a1;
    --violet: #8b5cf6;
    --violet-soft: #a78bfa;
    --tg: #229ed9;
}

/* ---------- الخلفية العامة والخطوط ---------- */
html, body, [class*="css"], .stApp, .stMarkdown, p, li, span, label, div, button, input {
    font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif !important;
}

.stApp {
    direction: rtl;
    text-align: right;
    color: var(--text-main);
    background:
        radial-gradient(1200px 600px at 85% -10%, rgba(139, 92, 246, 0.22), transparent 60%),
        radial-gradient(900px 500px at 5% 10%, rgba(245, 196, 107, 0.10), transparent 60%),
        radial-gradient(800px 600px at 50% 120%, rgba(34, 158, 217, 0.10), transparent 60%),
        linear-gradient(180deg, #0a0e1a 0%, #0c1122 100%);
    background-attachment: fixed;
}

/* إخفاء عناصر ستريمليت الافتراضية */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
    max-width: 820px;
}

h1, h2, h3, p, li, label, .stMarkdown {
    text-align: right !important;
    color: var(--text-main);
}

/* ---------- رأس الصفحة (Hero) ---------- */
.hero {
    position: relative;
    text-align: center;
    padding: 38px 24px 30px 24px;
    border-radius: 24px;
    background:
        linear-gradient(135deg, rgba(139, 92, 246, 0.18), rgba(18, 24, 41, 0.85) 55%, rgba(245, 196, 107, 0.10));
    border: 1px solid var(--border);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.05);
    overflow: hidden;
    margin-bottom: 28px;
}
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(1.5px 1.5px at 12% 22%, rgba(255,255,255,0.8), transparent),
        radial-gradient(1px 1px at 28% 70%, rgba(255,255,255,0.6), transparent),
        radial-gradient(1.5px 1.5px at 47% 18%, rgba(255,225,161,0.9), transparent),
        radial-gradient(1px 1px at 63% 62%, rgba(255,255,255,0.7), transparent),
        radial-gradient(1.5px 1.5px at 78% 30%, rgba(255,255,255,0.8), transparent),
        radial-gradient(1px 1px at 90% 78%, rgba(255,225,161,0.8), transparent),
        radial-gradient(1px 1px at 6% 85%, rgba(255,255,255,0.6), transparent);
    pointer-events: none;
}
.hero-icon {
    font-size: 44px;
    line-height: 1;
    margin-bottom: 8px;
    filter: drop-shadow(0 0 18px rgba(245, 196, 107, 0.55));
}
.hero h1 {
    position: relative;
    margin: 0 0 10px 0;
    padding: 0;
    font-size: 2.1rem;
    font-weight: 800;
    text-align: center !important;
    background: linear-gradient(90deg, var(--gold-soft), var(--gold), var(--violet-soft));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
}
.hero p {
    position: relative;
    margin: 0;
    font-size: 1.02rem;
    color: var(--text-soft) !important;
    text-align: center !important;
    line-height: 1.9;
}
.hero-badges {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-top: 20px;
}
.hero-badge {
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--gold-soft);
    background: rgba(245, 196, 107, 0.08);
    border: 1px solid rgba(245, 196, 107, 0.30);
}

/* ---------- الفواصل ---------- */
.divider {
    height: 1px;
    margin: 28px 0;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
}

/* ---------- قائمة الاختيار (Selectbox) : خلفية داكنة + نص فاتح ---------- */
.stSelectbox label,
.stSelectbox label p,
[data-testid="stWidgetLabel"] p {
    color: var(--gold-soft) !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    text-align: right !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: var(--bg-input) !important;
    color: var(--text-main) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    min-height: 54px;
    padding: 4px 8px;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.stSelectbox div[data-baseweb="select"] > div:hover {
    border-color: var(--violet-soft) !important;
}
.stSelectbox div[data-baseweb="select"] > div:focus-within {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(245, 196, 107, 0.18) !important;
}

/* النص الظاهر داخل الاختيار : فاتح وواضح ويلتف على أكثر من سطر */
.stSelectbox div[data-baseweb="select"] span,
.stSelectbox div[data-baseweb="select"] div,
.stSelectbox div[data-baseweb="select"] input {
    color: var(--text-main) !important;
    -webkit-text-fill-color: var(--text-main) !important;
    caret-color: var(--gold);
}
.stSelectbox div[data-baseweb="select"] span {
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
    line-height: 1.7;
    font-weight: 600;
}
.stSelectbox svg {
    fill: var(--gold) !important;
    color: var(--gold) !important;
}

/* القائمة المنسدلة (الخيارات) */
div[data-baseweb="popover"],
div[data-baseweb="popover"] > div {
    background-color: transparent !important;
}
div[data-baseweb="popover"] ul,
ul[role="listbox"],
div[data-baseweb="menu"] {
    background-color: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.6) !important;
    padding: 6px !important;
    direction: rtl;
}
li[role="option"],
ul[role="listbox"] li {
    background-color: transparent !important;
    color: var(--text-main) !important;
    -webkit-text-fill-color: var(--text-main) !important;
    border-radius: 10px !important;
    white-space: normal !important;
    text-align: right !important;
    line-height: 1.8;
    padding: 10px 14px !important;
    margin-bottom: 2px;
    font-weight: 500;
}
li[role="option"] *,
ul[role="listbox"] li * {
    color: var(--text-main) !important;
    -webkit-text-fill-color: var(--text-main) !important;
    white-space: normal !important;
}
li[role="option"]:hover,
li[role="option"][aria-selected="true"],
ul[role="listbox"] li:hover {
    background-color: var(--bg-hover) !important;
    color: var(--gold-soft) !important;
}
li[role="option"]:hover *,
li[role="option"][aria-selected="true"] * {
    color: var(--gold-soft) !important;
    -webkit-text-fill-color: var(--gold-soft) !important;
}

/* ---------- بطاقة تفاصيل الباقة ---------- */
.pkg-card {
    position: relative;
    margin-top: 22px;
    padding: 26px 26px 22px 26px;
    border-radius: 22px;
    background: linear-gradient(160deg, rgba(139, 92, 246, 0.10), var(--bg-card) 40%);
    border: 1px solid var(--border);
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.40);
    overflow: hidden;
}
.pkg-card::before {
    content: "";
    position: absolute;
    top: 0; right: 0; left: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--violet), var(--gold), var(--violet));
}
.pkg-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.1rem;
    font-weight: 800;
    color: var(--gold-soft);
    padding-bottom: 14px;
    margin-bottom: 14px;
    border-bottom: 1px dashed var(--border);
}
.pkg-list {
    list-style: none;
    margin: 0;
    padding: 0;
}
.pkg-list li {
    position: relative;
    padding: 8px 30px 8px 0;
    color: var(--text-main) !important;
    line-height: 1.95;
    font-size: 0.98rem;
}
.pkg-list li::before {
    content: "✦";
    position: absolute;
    right: 0;
    top: 8px;
    color: var(--gold);
    font-size: 0.9rem;
}

/* شرائح البرامج الفرعية */
.chips {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 14px 0 6px 0;
}
.chip {
    padding: 8px 16px;
    border-radius: 12px;
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--text-main);
    background: var(--bg-input);
    border: 1px solid var(--border);
    transition: transform 0.15s ease, border-color 0.15s ease;
}
.chip:hover {
    transform: translateY(-2px);
    border-color: var(--violet-soft);
}

/* صندوق السعر */
.price-box {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px;
    margin-top: 18px;
    padding: 14px 18px;
    border-radius: 16px;
    background: linear-gradient(90deg, rgba(245, 196, 107, 0.14), rgba(245, 196, 107, 0.04));
    border: 1px solid rgba(245, 196, 107, 0.40);
}
.price-label {
    font-weight: 800;
    color: var(--gold);
    font-size: 1.05rem;
}
.price-text {
    color: var(--text-main);
    font-weight: 600;
    line-height: 1.8;
}

/* ---------- المعاينة (Expander) ---------- */
[data-testid="stExpander"] {
    margin-top: 18px;
    background: var(--bg-card);
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    overflow: hidden;
}
[data-testid="stExpander"] details {
    background: var(--bg-card) !important;
    border: none !important;
}
[data-testid="stExpander"] summary {
    color: var(--gold-soft) !important;
    font-weight: 700;
    padding: 14px 18px !important;
    direction: rtl;
}
[data-testid="stExpander"] summary:hover {
    background: var(--bg-hover) !important;
}
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] summary svg {
    color: var(--gold-soft) !important;
    fill: var(--gold-soft) !important;
}
iframe {
    border-radius: 12px;
    border: 1px solid var(--border);
}

/* ---------- تنبيه / تحذير ---------- */
[data-testid="stAlert"] {
    background-color: rgba(245, 196, 107, 0.10) !important;
    border: 1px solid rgba(245, 196, 107, 0.35) !important;
    border-radius: 14px !important;
    color: var(--gold-soft) !important;
}
[data-testid="stAlert"] * { color: var(--gold-soft) !important; }

/* ---------- قسم الدفع ---------- */
.section-title {
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--text-main);
    margin: 0 0 6px 0;
    text-align: right;
}
.section-sub {
    color: var(--text-soft);
    margin: 0 0 8px 0;
    font-size: 0.95rem;
}
.tg-wrap {
    text-align: center;
    margin: 22px 0 6px 0;
}
.tg-btn {
    display: inline-block;
    padding: 15px 38px;
    border-radius: 16px;
    font-size: 1.05rem;
    font-weight: 800;
    color: #ffffff !important;
    text-decoration: none !important;
    background: linear-gradient(135deg, #2aabee, #1b7fc0);
    box-shadow: 0 10px 30px rgba(34, 158, 217, 0.35);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.tg-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 16px 40px rgba(34, 158, 217, 0.55);
    color: #ffffff !important;
}

/* ---------- خطوات الحجز ---------- */
.steps {
    margin-top: 14px;
    display: grid;
    gap: 14px;
}
.step {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 16px 18px;
    border-radius: 16px;
    background: var(--bg-card);
    border: 1px solid var(--border);
}
.step-num {
    flex: 0 0 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    color: #1a1204;
    background: linear-gradient(135deg, var(--gold-soft), var(--gold));
    box-shadow: 0 6px 18px rgba(245, 196, 107, 0.35);
}
.step-text {
    color: var(--text-main);
    line-height: 1.9;
    padding-top: 4px;
}

/* ---------- تذييل ---------- */
.footer-note {
    text-align: center;
    color: var(--text-soft);
    font-size: 0.82rem;
    margin-top: 40px;
    opacity: 0.75;
}

@media (max-width: 640px) {
    .hero h1 { font-size: 1.55rem; }
    .pkg-card { padding: 20px 16px; }
    .tg-btn { padding: 14px 22px; width: 100%; box-sizing: border-box; }
}
</style>
    """,
    unsafe_allow_html=True
)


# ==============================================================
# دوال مساعدة للعرض
# ==============================================================
def render_divider():
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


def render_package(icon, title, features, price_text, chips=None):
    """يعرض بطاقة تفاصيل الباقة بتصميم موحد (يتم بناء HTML بدون مسافات بادئة لتفادي تحويله لكود)."""
    html = '<div class="pkg-card">'
    html += f'<div class="pkg-title"><span>{icon}</span><span>{escape(title)}</span></div>'
    html += '<ul class="pkg-list">'
    for feature in features:
        html += f'<li>{escape(feature)}</li>'
    html += '</ul>'
    if chips:
        html += '<div class="chips">'
        for chip in chips:
            html += f'<span class="chip">{escape(chip)}</span>'
        html += '</div>'
    html += (
        '<div class="price-box">'
        '<span class="price-label">💰 السعر:</span>'
        f'<span class="price-text">{escape(price_text)}</span>'
        '</div>'
    )
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


# --- دالة مساعدة لعرض نموذج HTML من نفس المجلد ---
def show_local_html_sample(file_name="PDF_Example.html"):
    with st.expander("👀 اضغط هنا لمعاينة نموذج التقرير الفلكي (تفاعلي)"):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                html_content = f.read()
            components.html(html_content, height=600, scrolling=True)
        except FileNotFoundError:
            st.warning(f"عذراً، لم يتم العثور على ملف النموذج ({file_name}) في المستودع.")


# ==============================================================
# رأس الصفحة
# ==============================================================
st.markdown(
    '<div class="hero">'
    '<div class="hero-icon">🔭</div>'
    '<h1>الخدمات الاستشارية لـ الفلكي Astro Radar</h1>'
    '<p>اختر الباقة المناسبة و احصل على خدمتك ، الدفع البايبال بعد التواصل تلغرام</p>'
    '<div class="hero-badges">'
    '<span class="hero-badge">✨ تقارير فلكية PDF</span>'
    '<span class="hero-badge">🎙️ استشارات صوتية مباشرة</span>'
    '<span class="hero-badge">📊 برنامج فلكي متطور</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

# ==============================================================
# اختيار الباقة من قبل الزبون
# ==============================================================
service_choice = st.selectbox(
    "يرجى تحديد الباقة المطلوبة:",
    [
        "اختر الباقة...",
        "تقرير ملف استخراج الطالع شرط وجود ساعه تقريبية بنطاق 3 ساعات و حدث ماضي يتعلق بوفاة/ولادة/زواج/دخول مشفى فقط",
        "تقرير ملف تحليل الخارطة الميلادية الشامل مع توقعات سنوية",
        "تقرير ملف تحليل الخارطة السنوية",
        "حجز استشارة صوتية مع الفلكي للحصول على كامل خدماته",
        "حجز استشارة صوتية لشراء برنامج المنظومة الفلكية المتطورة - استرو رادار"
    ]
)

# ==============================================================
# عرض تفاصيل الباقات حسب الاختيار
# ==============================================================
if service_choice == "تقرير ملف استخراج الطالع شرط وجود ساعه تقريبية بنطاق 3 ساعات و حدث ماضي يتعلق بوفاة/ولادة/زواج/دخول مشفى فقط":
    render_package(
        icon="🎙️",
        title="تفاصيل الباقة:",
        features=[
            "يتضمن التقرير استخراج ساعة ميلادك بالساعة و الدقيقة و الثانية .",
            "مع طالعك الفلكي و درجة الطالع و رسم لخريطة الميلاد و تحليلات عملية الاستخراج من 6 خرائط فلكية .",
            "مطلوب تاريخ حدث قوي و مؤثر في الماضي لديك من أجل تصحيح ساعه الميلاد شرط ان يكون الشك في ساعه ميلادك الحقيقية بنطاق 3 ساعات فقط ."
        ],
        price_text="25 دولار (راسل تلغرام الفلكي للدفع بايبال)."
    )
    show_local_html_sample("ASC_Example.html")

elif service_choice == "تقرير ملف تحليل الخارطة الميلادية الشامل مع توقعات سنوية":
    render_package(
        icon="🎙️",
        title="تفاصيل الباقة:",
        features=[
            "يتضمن التقرير تحليل الميلادية و مواقع كواكب السنوية و اتصالاتها و توقعات شاملة لمدة خمس سنوات.",
            "و يتضمن التقرير التنجيم القياسي للميلادية و الطبي و النفسي و الاتصالات مع النجوم الثابتة."
        ],
        price_text="25 دولار (راسل تلغرام الفلكي للدفع بايبال)."
    )
    show_local_html_sample("PDF_Example.html")

elif service_choice == "تقرير ملف تحليل الخارطة السنوية":
    render_package(
        icon="🎙️",
        title="تفاصيل الباقة:",
        features=[
            "يتضمن التقرير تحليل السنوية و توضيح إن كانت سنة حرجة فيها تحولات أم عادية مع أهم التحذيرات و أهم النصائح.",
            "و شرح وضع المال و العاطفة و العمل و السفر و الصحة و الأهل/الأبناء و مواقع كواكب السنوية و اتصالاتها."
        ],
        price_text="25 دولار (راسل تلغرام الفلكي للدفع بايبال)."
    )
    show_local_html_sample("SOLAR_Example.html")

elif service_choice == "حجز استشارة صوتية مع الفلكي للحصول على كامل خدماته":
    render_package(
        icon="✨",
        title="تفاصيل الباقة الشاملة الكبرى (الأفضل والأكثر قيمة):",
        features=[
            "تتضمن جلسة حوارية صوتية مباشرة (مدتها 30 دقيقة).",
            "فيها الإجابة على كافة استفساراتك.",
            "بالإضافة لعرض كافة خدمات الفلكي لتختار حيث كل خدمة منها ب 25 دولار مثل التنجيم الجغرافي + تنجيم الحدث العاطفي .",
            "بالإضافة إلى جواب لسؤال ساعي + مصفوفة القدر + السنوات المتوقعة للارتباط العاطفي و الإنجاب - صفات الشريك العاطفي المتوقعة .",
            "بالإضافة لعلاج الهالة الطاقية لديك + السنوات المتوقعة للانفصال - المشاكل الزوجية .",
            "بالإضافة إلى التوافقية و من المسؤول عن عدم التوافق / التوافق + الأسلوب المفضل للشريك العاطفي .",
            "بالإضافة لسنوات التغيير المتوقعة حسب نظريه خاصة بالفلكي + سنوات الخطر الجسدي و النفسي حسب نظرية خاصة بالفلكي ."
        ],
        price_text="100 دولار للإجابة عن استفساراتك فيما يخص خدمة الميلادية + 25 دولار/عن كل خدمة إضافية (تواصل تلغرام للدفع بايبال)."
    )

elif service_choice == "حجز استشارة صوتية لشراء برنامج المنظومة الفلكية المتطورة - استرو رادار":
    render_package(
        icon="✨",
        title="تفاصيل باقة البرنامج (خاص بالفلكيين):",
        features=[
            "تتضمن جلسة حوارية صوتية مباشرة (مدتها 30 دقيقة).",
            "فيها شرح عن البرنامج و طريقة الشراء و تزويدك بملف تشغيل البرنامج.",
            "البرنامج هو منظومة فلكية مساعدة للفلكي تم تصميمها بلغة البايثون .",
            "و لها حماية خاصة بها منعا لانتشارها بطريقه غير مصرح بها من قبل المبرمج .",
            "و هي تحوي على عشرة برامج فرعية  :"
        ],
        chips=[
            "📊 برنامج تحليل الخريطة الساعية",
            "🔭 السنوية للأفراد و الشركات و الدول",
            "✨ التوافقية العاطفية للشخصيات",
            "📁 نظريتي لكشف سنوات الخطر أفراد/دول",
            "⚖️ كشف سنوات الأزمات الزوجية / التجارية",
            "🔭 منظومة تحليل ميلادية/سنوية/توقعات",
            "📈 برنامج التنجيم الجغرافي",
            "🔢 برنامج خريطة الحدث العاطفية",
            "🔗 كشف سنوات الزواج / الإنجاب و صفات الشريك المحتملة",
            "🌌 نظريتي لكشف سنوات التغيير أفراد/دول"
        ],
        price_text="250 دولار (راسل تلغرام الفلكي للدفع بايبال)."
    )

# ==============================================================
# زر الدفع وخطوات ما بعد الدفع
# ==============================================================
if service_choice != "اختر الباقة...":
    render_divider()

    st.markdown(
        '<div class="section-title">💳 راسل الفلكي تلغرام للدفع ب بايبال:</div>'
        '<div class="section-sub">اضغط على الزر أدناه لفتح المحادثة مباشرة.</div>'
        '<div class="tg-wrap">'
        '<a class="tg-btn" href="https://t.me/astroradarservices" target="_blank">'
        'تواصل معي عبر تيليجرام للدفع عبر بايبال ✈️'
        '</a>'
        '</div>',
        unsafe_allow_html=True
    )

    render_divider()

    st.markdown(
        '<div class="section-title">خطوات حجز و شراء الخدمة:</div>'
        '<div class="steps">'
        '<div class="step">'
        '<div class="step-num">1</div>'
        '<div class="step-text">تواصل معي مباشرة عبر تيليجرام للدفع بالبايبال.</div>'
        '</div>'
        '<div class="step">'
        '<div class="step-num">2</div>'
        '<div class="step-text">فور التحقق اليدوي من وصول المبلغ، سأقوم بتفعيل الخدمة أو إرسال الملفات (PDF / حجز موعد الاستشارة).</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="footer-note">✨ Astro Radar — الخدمات و الاستشارات الفلكية</div>',
    unsafe_allow_html=True
)
