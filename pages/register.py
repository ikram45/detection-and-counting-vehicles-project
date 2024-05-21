import streamlit as st
import pandas as pd
import numpy as np
from menu import menu


menu()
with st.form("my_formsignup"):
    st.write("SIGN UP")
    name=st.text_input('Name','enter your name')
    email=st.text_input('Email','enter your email')
    password=st.text_input('Password','enter your password')
    st.form_submit_button('Submit')