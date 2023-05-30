import streamlit as st
import requests
import json
import time
import os
from PIL import Image
import pyodbc


image = Image.open('./omananouna-logo.png')

st.set_page_config(page_title="omanouna", page_icon=image ,layout="wide")
col1, col2, col3 = st.columns([1,12,1])
with col1:
    st.image(image)
st.title('Oman services chatbot')

#url = "https://funcappccitest.azurewebsites.net/api/BotQnAHTTPFunc"


# headers= {
#  'x-functions-key':'wqe8NEIDgd3f1PpQgCoipQ4SclAiWNdD_wgng8J5Jz7UAzFusvfkcQ==',
#  'Content-Type':'application/json',
#  'Accept-Charset': 'utf-8, iso-8859-1;q=0.5, *;q=0.1'
# }
question = st.text_input("how can I help you today?", "")

# Establish a connection to the SQL Server database
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    "uid=userj;pwd=useruser;"
    'Server=Mic\MSSQLSERVER\;'
    'Port=1433;'
    'Database=testopenai;'
    'Trusted_Connection=yes;')
       
    
# conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};Server=localhost;Database=test;Trusted_Connection=yes;')
