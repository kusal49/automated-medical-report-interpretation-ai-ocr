import streamlit as st

def init_session():
    if "user" not in st.session_state:
        st.session_state.user = None

def set_user(user):
    st.session_state.user = user

def logout():
    st.session_state.clear()
