import streamlit as st
import streamlit.components.v1 as components # استدعاء مكتبة المكونات لعرض HTML

# إعدادات الصفحة وعنوان التبويب
st.set_page_config(
    page_title="الخدمات و الاستشارات الفلكية",
    page_icon="✨",
    layout="centered"
)
# إضافة كود CSS لجعل الاتجاه من اليمين إلى اليسار (RTL) وتنسيق الخطوط
st.markdown(
    """
    <style>
    /* تطبيق الاتجاه من اليمين إلى اليسار على كامل التطبيق */
    .stApp {
        direction: rtl;
        text-align: right;
    }
    /* تعديل محاذاة العناصر المنسدلة والعناوين لتتناسب مع اللغة العربية */
    .stSelectbox label, .stMarkdown, h1, h2, h3, p {
        text-align: right !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# العنوان الرئيسي
st.title("خدمات التحليلات والاستشارات الفلكية لـ الفلكي Astro Radar")

# العنوان الفرعي الجديد
st.subheader("اختر الباقة المناسبة لك واحصل على تحليلك الفلكي بدقة متناهية")

st.markdown("---")

# اختيار الباقة من قبل الزبون
service_choice = st.selectbox(
    "يرجى تحديد الخدمة المطلوبة:",
    [
        "اختر الخدمة...",
        "تقرير PDF فقط ($25)",
        "استشارة صوتية فقط ($110)",
        "الباقة الشاملة: تقرير + استشارة ($125)"
    ]
)

# روابط PayPal.Me الخاصة بك مع المبالغ المحددة مسبقاً
links = {
    "تقرير PDF فقط ($25)": "https://paypal.me/MulhamHalabieh/25",
    "استشارة صوتية فقط ($110)": "https://paypal.me/MulhamHalabieh/110",
    "الباقة الشاملة: تقرير + استشارة ($125)": "https://paypal.me/MulhamHalabieh/125"
}

# --- دالة مساعدة لعرض نموذج HTML من GitHub ---
def show_local_html_sample(file_name="PDF_Example.html"):
    # بناء رابط الـ Raw المباشر لملف الـ HTML على GitHub
    # (افتراض أن الفرع الافتراضي هو main، وإذا كان master استبدله بها)
    html_url = f"https://raw.githubusercontent.com/UranosScorpioMulhamEquation/astroradar/main/{file_name}"
    
    # وضعه داخل قائمة منسدلة (Expander) لترتيب شكل الصفحة
    with st.expander("👀 اضغط هنا لمعاينة نموذج التقرير الفلكي (تفاعلي)"):
        try:
            # عرض محتوى HTML عبر الـ iframe باستخدام رابط GitHub المباشر
            components.iframe(html_url, height=600, scrolling=True)
        except Exception as e:
            st.warning(f"عذراً، لم نتمكن من تحميل نموذج المعاينة حالياً. تأكد من رفع الملف '{file_name' إلى مستودع GitHub.")

# --- تفاصيل الخدمات التي تظهر حسب الاختيار ---

if service_choice == "تقرير PDF فقط ($25)":
    st.info("📄 **تفاصيل تقرير الـ PDF:**")
    st.markdown("""
    * يتضمن التقرير توقعات سنوية شاملة.
    """)
# استدعاء دالة عرض النموذج
    show_local_html_sample("PDF_Example.html")

elif service_choice == "استشارة صوتية فقط ($110)":
    st.info("🎙️ **تفاصيل الاستشارة الصوتية:**")
    st.markdown("""
    * جلسة حوارية صوتية مباشرة خاصة معك عبر مكالمة تلغرام (مدتها 45 دقيقة).
    * مناقشة مفصلة ودقيقة للمعطيات الفلكية الخاصة بك والإجابة على كافة استفساراتك بشكل شخصي.
    """)

elif service_choice == "الباقة الشاملة: تقرير + استشارة ($125)":
    st.info("✨ **تفاصيل الباقة الشاملة (الأفضل والأكثر طلباً):**")
    st.markdown("""
    1. **تقرير الـ PDF الكامل:** تحصل على التقرير التحليلي المكتوب والمفصل فوراً.
    2. **جلسة الاستشارة الصوتية:** جلسة مباشرة خاصة لمناقشة نتائج التقرير والإجابة على أسئلتك بعمق.
    """)
    show_local_html_sample("PDF_Example.html")


# --- زر الدفع وخطوات ما بعد الدفع ---
if service_choice != "اختر الخدمة...":
    selected_link = links[service_choice]
    
    st.markdown("---")
    st.markdown(
        f"""
        <div style="text-align: center; margin: 20px 0;">
            <a href="{selected_link}" target="_blank">
                <button style="background-color: #0070ba; color: white; padding: 12px 24px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; font-weight: bold;">
                    إتمام الدفع عبر بايبال 💳
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )   
    st.markdown("---")
    st.subheader("خطوات ما بعد الدفع:")
    st.markdown("""
    1. **قم بالدفع** عبر الرابط أعلاه بالمبلغ المحدد.
    2. **خذ لقطة شاشة (Screenshot)** لإيصال الدفع الناجح.
    3. تواصل معي مباشرة عبر تيليجرام وأرسل لقطة الشاشة مع البريد الإلكتروني أو التفاصيل.
    4. فور التحقق اليدوي من وصول المبلغ، سأقوم بتفعيل الخدمة أو إرسال الملفات (PDF / حجز موعد الاستشارة).
    """)
    
    # معرف تيليجرام
    telegram_username = "http://t.me/me8mo8"
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://t.me/http://t.me/me8mo8" target="_blank">
                <button style="background-color: #0088cc; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 15px; cursor: pointer;">
                    تواصل معي عبر تيليجرام لإرسال الإيصال ✈️
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
