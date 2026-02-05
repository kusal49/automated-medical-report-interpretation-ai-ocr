import streamlit as st

from components.analysis_form import analysis_form
from components.style import load_css
from services.db_service import init_db


# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="AI Medical Report Analyzer",
    page_icon="🧬",
    layout="wide"
)

# -------------------------------
# INITIAL SETUP
# -------------------------------
load_css()      # load dark UI styles
init_db()       # initialize SQLite DB


# -------------------------------
# LOCAL USER SESSION (NO AUTH)
# -------------------------------
if "user" not in st.session_state:
    st.session_state.user = {
        "email": "local_user"
    }


# -------------------------------
# MAIN UI
# -------------------------------
st.markdown("""
<h1 style="text-align:center;">🧬 AI Medical Report Analyzer</h1>
<p class="subtitle">
Upload any medical test report (PDF or Image) and get AI-powered health insights
</p>
""", unsafe_allow_html=True)

analysis_form(st.session_state.user)

st.caption(
    "⚠️ This application provides educational insights only and is not a substitute for professional medical advice."
)
