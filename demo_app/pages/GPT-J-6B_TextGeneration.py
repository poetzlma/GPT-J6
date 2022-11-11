#importing required libraries
import requests
import json
import streamlit as st

with st.form("my_form"):
        st.write("GPT-J-6B TEXT GENERATOR")
        st.write("This Slider controls the number of new tokens to be generated")
        slider_val = st.slider("new tokens * 100")
        text_val = st.text_input("input text here, This is a starting point for the text generation")

   # Every form must have a submit button.
        submitted = st.form_submit_button("Generate Text")
        if submitted:
                        #connect both strings
                        url = 'http://127.0.0.1:5002/generate'

                        payload ="{'body': '" + str(text_val) + "', 'token': '"+ str(slider_val) +"'}"
                        payload = payload.replace("'", '"')

                        # st.write(payload)

                        r = requests.get(url, json=payload)
                        data = r.content.decode("utf-8")
                        
                        answer = json.loads(data)['result']                        

                        st.code(answer)

st.write("If i am light grey i am working")