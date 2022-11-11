#importing required libraries
import requests
import json
import streamlit as st

with st.form("my_form"):
        st.header("Product Description Ad Generation")

        st.write("Create some product descriptions for your products")

        st.caption("---- A Dataset could already include: ----")        

        few_shot = """Generate a product description out of keywords.

        Keywords: shoes, women, $59
        Sentence: Beautiful shoes for women at the price of $59.
        ###
        Keywords: trousers, men, $69
        Sentence: Modern trousers for men, for $69 only.
        ###
        Keywords: gloves, winter, $19
        Sentence: Amazingly hot gloves for cold winters, at $19.
        ###
        Keywords:"""

        st.code(few_shot)

        st.header("Now try it yourself!")

        st.caption("Or copy this and manipulate it to your needs")

        st.caption("socks, wool, $10")


        text_val = st.text_input("Enter the textual description here")

        request= few_shot + "Sentence: " + text_val
        # Every form must have a submit button.
        submitted = st.form_submit_button("Create Description")
        if submitted:
                #connect both strings
                url = 'http://127.0.0.1:5002/generate'

                payload ="{'body': '" + str(request) + "', 'token': '10'}"
                payload = payload.replace("'", '"')
                

                r = requests.get(url, json=payload)                

                data = r.content.decode("utf-8")

                answer = json.loads(data)

                

                answer = answer['result'].split("###")[3]                



                st.code(answer)

st.write("If i am light grey i am working")