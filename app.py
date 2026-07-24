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
st.subheader("اختر الباقة المناسبة لك و احصل على تحليلك الفلكي , يمكن الحصول على هدية بأحد المؤلفات الخاصة بي في حال اخترت المتجر المحلي للدفع")
st.markdown("---")

# اختيار الباقة من قبل الزبون
service_choice = st.selectbox(
    "يرجى تحديد الباقة المطلوبة:",
    [
        "اختر الباقة...",
        "باقة تقرير PDF",
        "باقة الاستشارة الصوتية",
        "الباقة الشاملة الكبرى (تقرير + استشارة)"
    ]
)

# روابط الدفع للمتجر المحلي (بالدرهم الإماراتي) و روابط بايبال (بالدولار الأمريكي) مرتبطة بمفاتيح دقيقة
store_links = {
    "باقة تقرير PDF": "https://alfan.link/mulham.ahmad?digital=6g9QtB",
    "باقة الاستشارة الصوتية": "https://alfan.link/mulham.ahmad?digital=zQqznW",
    "الباقة الشاملة الكبرى (تقرير + استشارة)": "https://alfan.link/mulham.ahmad?digital=qRGhTJ"
}

paypal_links = {
    "باقة تقرير PDF": "https://paypal.me/MulhamHalabieh/25",
    "باقة الاستشارة الصوتية": "https://paypal.me/MulhamHalabieh/110",
    "الباقة الشاملة الكبرى (تقرير + استشارة)": "https://paypal.me/MulhamHalabieh/125"
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

if service_choice == "باقة تقرير PDF":
    st.info("📄 **تفاصيل باقة تقرير الـ PDF:**")
    st.markdown("""
    * يتضمن التقرير توقعات سنوية شاملة.
    * **💰 السعر:** 125 درهم (عبر المتجر المحلي) أو $25 (عبر بايبال).
    * **🎁 هدية إضافية في حال الدفع بالمتجر المحلي:** كتاب **"الصادات الحيويّة عند الدواجن"**.
    """)
    show_local_html_sample("PDF_Example.html")

elif service_choice == "باقة الاستشارة الصوتية":
    st.info("🎙️ **تفاصيل باقة الاستشارة الصوتية:**")
    st.markdown("""
    * جلسة حوارية صوتية مباشرة خاصة معك عبر مكالمة تلغرام (مدتها 45 دقيقة).
    * مناقشة مفصلة ودقيقة للمعطيات الفلكية الخاصة بك والإجابة على كافة استفساراتك بشكل شخصي.
    * **💰 السعر:** 400 درهم (عبر المتجر المحلي) أو $110 (عبر بايبال).
    * **🎁 هدية إضافية في حال الدفع بالمتجر المحلي:** كتاب **"نص الختم البابلي و الكود 9.3 السينمائي"**.
    """)

elif service_choice == "الباقة الشاملة الكبرى (تقرير + استشارة)":
    st.info("✨ **تفاصيل الباقة الشاملة الكبرى (الأفضل والأكثر قيمة):**")
    st.markdown("""
    * تتضمن التقرير الفلكي الكامل + جلسة حوارية صوتية مباشرة (مدتها 45 دقيقة).
    * مناقشة مفصلة ودقيقة للمعطيات الفلكية والإجابة على كافة استفساراتك.
    * **💰 السعر:** 500 درهم (عبر المتجر المحلي) أو $125 (عبر بايبال).
    * **🎁 هدية إضافية في حال الدفع بالمتجر المحلي:** كتاب **"نظرية هوميا إيريس المؤسسية"**.
    """)
    show_local_html_sample("PDF_Example.html")

# --- أزرار الدفع وخطوات ما بعد الدفع ---
if service_choice != "اختر الباقة...":
    st.markdown("---")
    st.subheader("💳 اختر طريقة الدفع المناسبة لك:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            f"""
            <div style="text-align: center; margin: 10px 0;">
                <a href="{store_links[service_choice]}" target="_blank">
                    <button style="background-color: #28a745; color: white; padding: 12px 20px; border: none; border-radius: 5px; font-size: 15px; cursor: pointer; font-weight: bold; width: 100%;">
                        الدفع بالبطاقة عبر المتجر المحلي 🛍️
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col2:
        st.markdown(
            f"""
            <div style="text-align: center; margin: 10px 0;">
                <a href="{paypal_links[service_choice]}" target="_blank">
                    <button style="background-color: #0070ba; color: white; padding: 12px 20px; border: none; border-radius: 5px; font-size: 15px; cursor: pointer; font-weight: bold; width: 100%;">
                        الدفع عبر PayPal 💳
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    st.subheader("خطوات ما بعد الدفع:")
    st.markdown("""
    1. **أتمم عملية الدفع** بالطريقة التي تفضلها (عبر المتجر المحلي بالبطاقة أو عبر بايبال).
    2. **خذ لقطة شاشة (Screenshot)** لإيصال الدفع الناجح.
    3. تواصل معي مباشرة عبر تيليجرام وأرسل لقطة الشاشة مع البريد الإلكتروني أو التفاصيل.
    4. فور التحقق اليدوي من وصول المبلغ، سأقوم بتفعيل الخدمة أو إرسال الملفات (PDF / حجز موعد الاستشارة).
    """)
    
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://t.me/me8mo8" target="_blank">
                <button style="background-color: #0088cc; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 15px; cursor: pointer;">
                    تواصل معي عبر تيليجرام لإرسال الإيصال وتأكيد الاستلام ✈️
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
