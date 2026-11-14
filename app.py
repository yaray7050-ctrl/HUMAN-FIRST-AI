import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(
    page_title="HUMAN FIRST AI",
    page_icon="🛡️",
    layout="wide"
)

# تنسيق الواجهة
st.markdown("""
<style>
.stApp {
    direction: rtl;
    text-align: right;
}
.main-title {
    text-align: center;
    color: #2563eb;
    font-size: 36px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# العنوان
st.markdown(
    '<div class="main-title">HUMAN FIRST AI (HFA)</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Governance | Human Protection | Responsible AI</div>',
    unsafe_allow_html=True
)

st.divider()

st.header("نظام تقييم وحوكمة الذكاء الاصطناعي")

st.write(
    "أدخل بيانات نظام الذكاء الاصطناعي لتقييم "
    "مؤشرات المخاطر والحصول على توصيات أولية."
)

# إدخال البيانات
with st.form("hfa_assessment"):

    system_name = st.text_input(
        "اسم نظام الذكاء الاصطناعي"
    )

    purpose = st.text_area(
        "ما الغرض من استخدام النظام؟"
    )

    st.subheader("تقييم عوامل المخاطر")

    data_sensitivity = st.selectbox(
        "مدى حساسية البيانات المستخدمة",
        ["منخفضة", "متوسطة", "مرتفعة"]
    )

    bias_testing = st.selectbox(
        "هل يتم اختبار النظام لاكتشاف التحيز؟",
        ["نعم", "جزئيًا", "لا"]
    )

    human_oversight = st.selectbox(
        "مستوى الرقابة البشرية",
        ["مستمرة", "جزئية", "لا توجد"]
    )

    transparency = st.selectbox(
        "مدى وضوح قرارات النظام",
        ["واضحة", "واضحة جزئيًا", "غير واضحة"]
    )

    security = st.selectbox(
        "مستوى إجراءات حماية البيانات",
        ["قوية", "أساسية", "ضعيفة"]
    )

    submitted = st.form_submit_button(
        "ابدأ تقييم HFA",
        use_container_width=True
    )

# تحليل النتائج
if submitted:

    if not system_name.strip():
        st.error("من فضلك أدخل اسم النظام.")
        st.stop()

    score = 0
    recommendations = []

    # حساسية البيانات
    if data_sensitivity == "متوسطة":
        score += 1
    elif data_sensitivity == "مرتفعة":
        score += 2
        recommendations.append(
            "تعزيز حماية البيانات الحساسة وتقليل الوصول غير الضروري إليها."
        )

    # اختبار التحيز
    if bias_testing == "جزئيًا":
        score += 1
        recommendations.append(
            "تحسين اختبارات التحيز ومراجعة نتائجها."
        )
    elif bias_testing == "لا":
        score += 2
        recommendations.append(
            "إنشاء اختبارات دورية للكشف عن التحيز."
        )

    # الرقابة البشرية
    if human_oversight == "جزئية":
        score += 1
        recommendations.append(
            "زيادة الرقابة البشرية على القرارات عالية التأثير."
        )
    elif human_oversight == "لا توجد":
        score += 2
        recommendations.append(
            "إضافة آلية رقابة بشرية ومراجعة القرارات المهمة."
        )

    # الشفافية
    if transparency == "واضحة جزئيًا":
        score += 1
        recommendations.append(
            "تحسين توضيح طريقة عمل النظام وأسباب قراراته."
        )
    elif transparency == "غير واضحة":
        score += 2
        recommendations.append(
            "توفير معلومات أوضح عن قرارات النظام."
        )

    # الأمن
    if security == "أساسية":
        score += 1
        recommendations.append(
            "تعزيز إجراءات الأمن وحماية البيانات."
        )
    elif security == "ضعيفة":
        score += 2
        recommendations.append(
            "مراجعة إجراءات الأمن ومعالجة نقاط الضعف."
        )

    # تحديد مستوى الخطورة
    if score <= 3:
        risk = "LOW"
        color = "success"

    elif score <= 6:
        risk = "MEDIUM"
        color = "warning"

    elif score <= 8:
        risk = "HIGH"
        color = "error"

    else:
        risk = "CRITICAL"
        color = "error"

    st.divider()
    st.header("نتائج تقييم HFA")

    st.subheader(system_name)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Risk Score", f"{score} / 10")

    with col2:
        st.metric("Risk Level", risk)

    if color == "success":
        st.success(f"مستوى المخاطر: {risk}")
    elif color == "warning":
        st.warning(f"مستوى المخاطر: {risk}")
    else:
        st.error(f"مستوى المخاطر: {risk}")

    st.subheader("تفاصيل التقييم")

    results = pd.DataFrame({
        "عامل التقييم": [
            "حساسية البيانات",
            "اختبار التحيز",
            "الرقابة البشرية",
            "الشفافية",
            "الأمن"
        ],
        "النتيجة": [
            data_sensitivity,
            bias_testing,
            human_oversight,
            transparency,
            security
        ]
    })

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("التوصيات المقترحة")

    if recommendations:
        for i, recommendation in enumerate(
            recommendations, 1
        ):
            st.write(f"{i}. {recommendation}")
    else:
        st.success(
            "لم تظهر مؤشرات تستدعي توصيات إضافية وفق المدخلات الحالية."
        )

    st.info(
        "هذا تقييم أولي مبني على إجابات المستخدم وقواعد تقييم محددة، "
        "ولا يمثل إثباتًا نهائيًا للامتثال أو اكتشافًا آليًا للتحيز."
    )

    st.caption(
        "HFA | Human First AI - Human-Centered AI Governance"
    )

else:
    st.info(
        "أدخل بيانات النظام واضغط على ابدأ تقييم HFA لعرض النتائج."
    )
