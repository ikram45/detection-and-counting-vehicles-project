import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re


def sign_up():
    with st.form(key='signup',clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email = st.text_input('Email', placeholder='Enter your email')
        Username = st.text_input('Username', placeholder='Enter your username')
        password = st.text_input('Password', placeholder='Enter your password',type='password')
        passconfirm = st.text_input('Confirm Password', placeholder='Confirm your password',type='password')
