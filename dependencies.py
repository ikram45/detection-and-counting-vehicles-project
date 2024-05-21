import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from influxdb_client import InfluxDBClient, Point
import os



# Get InfluxDB connection details from environment variables
INFLUXDB_UR = os.getenv('https://us-west-2-1.aws.cloud2.influxdata.com')
INFLUXDB_TOKEN = os.getenv('azer')
INFLUXDB_ORG = os.getenv('dashboards')
INFLUXDB_BUCKET = os.getenv('auth')




# Initialize InfluxDB client
client = InfluxDBClient(url=INFLUXDB_UR, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = client.write_api()
query_api = client.query_api()



def sign_up():
    with st.form(key='signup',clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email = st.text_input('Email', placeholder='Enter your email')
        Username = st.text_input('Username', placeholder='Enter your username')
        password = st.text_input('Password', placeholder='Enter your password',type='password')
        passconfirm = st.text_input('Confirm Password', placeholder='Confirm your password',type='password')
        submit = st.form_submit_button('Sign Up')

        if submit:
            if password != passconfirm:
                st.error("Passwords do not match!")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("Invalid email format!")
            else:
                # Insert user data into InfluxDB
                point = Point("users").tag("username", Username).field("email", email).field("password", password)
                write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
                st.success("User signed up successfully!")