#importing required libraries
import requests
import json
import streamlit as st

with st.form("my_form"):
        st.header("Intent Classification")

        st.write("The following will show how to extract Intent from data")

        st.caption("---- A Dataset could already include: ----")        

        few_shot = """I want to start coding tomorrow because it seems to be so fun!
            Intent: start coding
            ###
            Show me the last pictures you have please.
            Intent: show pictures
            ###
            Search all these files as fast as possible.
            Intent: search files
            ###
            """

        st.code(few_shot)

        st.header("Now try it yourself!")

        st.caption("Or copy this and manipulate it to your needs")

        st.caption("Teach me how to ride a surfboard")


        text_val = st.text_input("Enter the textual description here")

        request= few_shot + text_val
        # Every form must have a submit button.
        submitted = st.form_submit_button("Get Intent")
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