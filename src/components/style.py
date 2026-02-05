import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* ===== GLOBAL BACKGROUND ===== */
    .stApp {
        background-color: #0b0f19;
        color: #e5e7eb;
    }

    /* ===== MAIN CENTER CONTAINER ===== */
    .main-container {
        max-width: 760px;
        margin: auto;
        padding: 2.5rem 1.5rem;
    }

    /* ===== CARDS ===== */
    .card {
        background: #111827;
        padding: 1.8rem;
        border-radius: 14px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.6);
        margin-bottom: 1.8rem;
        border: 1px solid #1f2937;
    }

    /* ===== HEADINGS ===== */
    h1, h2, h3 {
        color: #f9fafb;
        font-weight: 700;
    }

    /* ===== SUBTITLE ===== */
    .subtitle {
        text-align: center;
        color: #9ca3af;
        margin-bottom: 2.5rem;
        font-size: 1rem;
    }

    /* ===== FILE UPLOADER ===== */
    .stFileUploader {
        border: 2px dashed #2563eb;
        border-radius: 14px;
        background-color: #020617;
        padding: 1.3rem;
        color: #e5e7eb;
    }

    /* ===== BUTTONS ===== */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        border-radius: 12px;
        padding: 0.7rem;
        font-size: 16px;
        border: none;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
    }

    /* ===== INFO / SUCCESS / WARNING ===== */
    .stAlert {
        background-color: #020617 !important;
        border: 1px solid #1f2937;
        color: #e5e7eb;
    }

    /* ===== FOOTER TEXT ===== */
    .stCaption {
        color: #9ca3af;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
