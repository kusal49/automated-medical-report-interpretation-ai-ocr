import streamlit as st

from utils.pdf_extractor import extract_text_from_pdf
from utils.image_ocr import extract_text_from_image
from agents.agent_manager import analyze_report
from utils.risk_assessor import assess_medical_risk


def analysis_form(user):
    st.subheader("📄 Upload Medical Report")

    upload_type = st.radio(
        "Select report format",
        ["PDF document", "Image / Scanned report"],
        horizontal=True
    )

    if upload_type == "PDF document":
        uploaded_file = st.file_uploader(
            "Upload PDF medical report",
            type=["pdf"]
        )
    else:
        uploaded_file = st.file_uploader(
            "Upload image report (PNG / JPG / JPEG)",
            type=["png", "jpg", "jpeg"]
        )

    if not uploaded_file:
        st.caption("Supported formats: PDF, PNG, JPG | Image max size: 2000×2000 px")
        return

    with st.spinner("🧠 Extracting text & analyzing report…"):
        # -------- TEXT EXTRACTION --------
        if upload_type == "PDF document":
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_image(uploaded_file)

        # OCR hard-stop (image too large or failed)
        if text is None or not text.strip():
            st.warning("No readable text found in the report.")
            return

        # -------- AI ANALYSIS --------
        analysis_result = analyze_report(text)

    st.success("✅ Analysis completed")

    # -------- RISK ASSESSMENT --------
    risk_level, risk_message = assess_medical_risk(analysis_result)

    if risk_level == "HIGH":
        st.error("🚨 **Medical Attention Recommended**")
        st.markdown(risk_message)
    elif risk_level == "MEDIUM":
        st.warning("⚠️ **Some values may need medical review**")
        st.markdown(risk_message)
    else:
        st.success("🟢 **No urgent medical concerns detected**")

    # -------- FINAL OUTPUT --------
    st.markdown("---")
    st.subheader("🧾 AI Health Insights")
    st.markdown(
        f"<div class='card'>{analysis_result}</div>",
        unsafe_allow_html=True
    )

    st.caption(
        "⚠️ This tool provides educational insights only and does not replace professional medical advice."
    )
