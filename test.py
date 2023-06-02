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
# pyodbc.connect(‘Driver={FreeTDS};SERVER=’+server+’;DATABASE=’+database+’;UID=’+username+’;PWD=’+password)
# pyodbc.connect('DSN=MSSQLServerDatabase;UID=myuid', password="secret{}();'P@ssw0rd}{")
# conn = pyodbc.connect(
#     'Driver={FreeTDS};'
#     "uid=userj;pwd=P@ssw0rd;"
#     'Server=devops-test;'
#     'Database=testopenai;'
#     'Trusted_Connection=yes;')
# conn = pyodbc.connect('DSN = openaisql2; Server = devops-test; Port = 1433' ) 
# conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=MIC;Database=testopenai;UID=userj;PWD=useruser;')
# conn = pyodbc.connect('DRIVER={Devart ODBC Driver for MongoDB};Server=DESKTOP-D2BR8HJ;Port=27017;Database =openaitest;')
from pymongo import MongoClient
def get_database():
   CONNECTION_STRING = "mongodb://MIC:27017/"
   client = MongoClient(CONNECTION_STRING)
   return client['openaitest']

 
dbname = get_database()
st.write(dbname)
# cursor = conn.cursor()
# sql_insert = "INSERT INTO conversation (question, answer) VALUES (?, ?)"
# data = [('how you', 'nothingjjjjjjjjjj')]
# cursor.executemany(sql_insert, data)

# # Commit the transaction to save the changes
# conn.commit()

# # Close the cursor and the database connection
# cursor.close()
# conn.close()
# conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=10.1.0.4;Database=testopenai;UID=userj;PWD=user1234;')    
# conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};Server=localhost;Database=test;Trusted_Connection=yes;')
