import streamlit as st
import pandas as pd
import numpy as np
from menu import menu
import psycopg2
import os

# Get database connection details from environment variables
DATABASE_URL = os.getenv('postgresql://postgres:JZlgqZuqUxtdEiGKAIzgOUDpMQqKRtSQ@viaduct.proxy.rlwy.net:59496/railway')

# Function to connect to the PostgreSQL database
def get_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn



# Example function to create a table
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        password INTEGER NOT NULL
    )
    """)
    conn.commit()
    cur.close()
    conn.close()



# Create table
create_table()





menu()







"""
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)
"""