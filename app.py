import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة وعنوان التبويب
st.set_page_config(
    page_title="الخدمات و الاستشارات الفلكية",
    page_icon="✨",
    layout="centered"
)

# كود CSS لتنسيق اللغة العربية (من اليمين لليسار)
st.markdown(
    """
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
    }
    .stSelectbox label, .stMarkdown, h1, h2, h3, p, li {
        text-align: right !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("خدمات التحليلات والاستشارات الفلكية لـ الفلكي Astro Radar")
st.subheader("اختر الباقة المناسبة لك واحصل على تحليلك الفلكي، بالإضافة إلى هدية بأحد المؤلفات الخاصة بي عبر متجر أمازون")
st.markdown("---")

# اختيار الباقة من قبل الزبون
service_choice = st.selectbox(
    "يرجى تحديد الباقة المطلوبة:",
    [
        "اختر الباقة...",
        "تقرير ملف التحليل الشامل من خريطة ميلادية و سنوية و توقعات سنوية",
        "تصحيح الطالع و ساعه الميلاد يدوياً من قبل الفلكي",
        "حجز استشارة صوتية مطولة مع الفلكي للحصول على كامل خدماته"
    ]
)

# روابط الدفع لمتجر أمازون (بالدولار الأمريكي)
store_links = {
    "تقرير ملف التحليل الشامل من خريطة ميلادية و سنوية و توقعات سنوية": "https://www.amazon.com/dp/B0H2BZ1GX3",
    "تصحيح الطالع و ساعه الميلاد يدوياً من قبل الفلكي": "https://www.amazon.com/dp/B0H7K32VLQ",
    "حجز استشارة صوتية مطولة مع الفلكي للحصول على كامل خدماته": "https://www.amazon.com/dp/B0H4WZDGCP"
}

# --- دالة مساعدة لعرض نموذج HTML من نفس المجلد ---
def show_local_html_sample(file_name="PDF_Example.html"):
    with st.expander("👀 اضغط هنا لمعاينة نموذج التقرير الفلكي (تفاعلي)"):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                html_content = f.read()
            components.html(html_content, height=600, scrolling=True)
        except FileNotFoundError:
            st.warning(f"عذراً، لم يتم العثور على ملف النموذج ({file_name}) في المستودع.")

# --- عرض تفاصيل الباقات حسب الاختيار ---

if service_choice == "تقرير ملف التحليل الشامل من خريطة ميلادية و سنوية و توقعات سنوية":
    st.info("📄 **تفاصيل باقة تقرير الـ PDF:**")
    st.markdown("""
    * يتضمن التقرير تحليل الميلادية و السنوية توقعات شاملة.
    * **💰 السعر:** 25 دولار (عبر متجر أمازون).
    * **🎁 هدية إضافية:** كتاب إلكتروني باللغة الإنجليزية **"نظرية مصفوفة زحل"**.
    """)
    show_local_html_sample("PDF_Example.html")

elif service_choice == "تصحيح الطالع و ساعه الميلاد يدوياً من قبل الفلكي":
    st.info("🎙️ **تفاصيل الباقة:**")
    st.markdown("""
    * جلسة حوارية صوتية مباشرة خاصة معك عبر مكالمة تلغرام (مدتها 30 دقيقة).
    * مناقشة تاريخ حدث قوي و مؤثر في الماضي لديك من أجل تصحيح ساعه الميلاد شرط ان يكون الشك في ساعه ميلادك الحقيقية بنطاق 3 ساعات فقط .
    * **💰 السعر:** 99 دولار (عبر متجر أمازون).
    * **🎁 هدية إضافية:** كتاب إلكتروني باللغة الإنجليزية **"نظرية رادار نبتون هوميا ايريس"**.
    """)

elif service_choice == "حجز استشارة صوتية مطولة مع الفلكي للحصول على كامل خدماته":
    st.info("✨ **تفاصيل الباقة الشاملة الكبرى (الأفضل والأكثر قيمة):**")
    st.markdown("""
    * تتضمن جلسة حوارية صوتية مباشرة (مدتها 60 دقيقة).
    * فيها الإجابة على كافة استفساراتك.
    * عرض كافة خدمات الفلكي لتختار 4 منها مثل التنجيم الجغرافي و مصفوفة القدر و السنوات المتوقعه للارتباط العاطفي.
    * بالإضافة لعلاج الهالة الطاقية لديك و السنوات المتوقعة للانفصال أو المشاكل الزوجية .
    * بالإضافة لسنوات التغيير المتوقعه حسب نظريه خاصة بالفلكي و سنوات الخطر الجسدي و النفسي حسب نظرية خاصة بالفلكي .
    * **💰 السعر:** 119 دولار (عبر متجر أمازون).
    * **🎁 هدية إضافية:** كتاب إلكتروني باللغة الإنجليزية **"نظرية مصفوفة هوميا إيريس المؤسسية"**.
    """)

# --- زر الدفع وخطوات ما بعد الدفع ---
if service_choice != "اختر الباقة...":
    st.markdown("---")
    st.subheader("💳 أتمم عملية الدفع عبر متجر أمازون:")
    
    st.markdown(
        f"""
        <div style="text-align: center; margin: 15px 0;">
            <a href="{store_links[service_choice]}" target="_blank">
                <button style="background-color: #28a745; color: white; padding: 12px 20px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; font-weight: bold; width: 100%;">
                    الدفع بالبطاقة عبر متجر أمازون 🛍️
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    st.subheader("خطوات ما بعد الدفع:")
    st.markdown("""
    1. **أتمم عملية الدفع** عبر رابط متجر أمازون أعلاه.
    2. **خذ لقطة شاشة (Screenshot)** لإيصال الدفع الناجح.
    3. تواصل معي مباشرة عبر تيليجرام وأرسل لقطة الشاشة مع البريد الإلكتروني أو التفاصيل.
    4. فور التحقق اليدوي من وصول المبلغ، سأقوم بتفعيل الخدمة أو إرسال الملفات (PDF / حجز موعد الاستشارة).
    """)
    
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://t.me/astroradarservices" target="_blank">
                <button style="background-color: #0088cc; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 15px; cursor: pointer;">
                    تواصل معي عبر تيليجرام لإرسال الإيصال وتأكيد الاستلام ✈️
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
