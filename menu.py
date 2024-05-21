import streamlit as st

def menu():
    st.sidebar.page_link("pages/login.py",label="LOGIN")
    st.sidebar.page_link("pages/register.py",label="REGISTER")