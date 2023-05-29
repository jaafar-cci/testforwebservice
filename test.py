import streamlit as st
import requests
import json
import time
import os
from PIL import Image



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
# question = st.text_input("how can I help you today?", "")
# payload = json.dumps({
#         "query":question
#         })
# if question != '':
#     response = requests.request("GET",url,headers=headers,data=payload)
# # time.sleep(30)
#     json_data = json.loads(response.content)
#     st.write(json_data['answer'])
# text = response.text.encode('latin1').decode('unicode_escape')
# t = t.text.encode('latin1').decode('unicode_escape')
# a = response.json
# st.write(a['answer'])
# st.write(text)

# time.sleep(30)
# st.write(type(response))
# st.write(type(text))
# st.write(response.json())
# st.write(text{1})
# st.write(text)

# import http.client

# import json




# conn=http.client.HTTPSConnection("funcappccitest.azurewebsites.net")

# payload=json.dumps({

# "query":q2

# })

# headers={

#  'x-functions-key':'wqe8NEIDgd3f1PpQgCoipQ4SclAiWNdD_wgng8J5Jz7UAzFusvfkcQ==',

#  'Content-Type':'application/json'

# }

# conn.request("GET","/api/BotQnAHTTPFunc",payload,headers)

# res=conn.getresponse()

# data=res.read()

# # print(data.decode("utf-8"))

# st.write(data.decode("utf-8"))
       
