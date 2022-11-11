#importing required libraries
import requests
import json
import streamlit as st

with st.form("my_form"):
        st.header("Advanced Entity Extraction")

        st.write("The following will show how use the advanced entity extraction feature")

        st.caption("---- A Dataset could already include: ----")        

        few_shot = """[Text]: Fred is a serial entrepreneur. Co-founder and CEO of Platform.sh, he previously co-founded Commerce Guys, a leading Drupal ecommerce provider. His mission is to guarantee that as we continue on an ambitious journey to profoundly transform how cloud computing is used and perceived, we keep our feet well on the ground continuing the rapid growth we have enjoyed up until now. 
        [Name]: Fred [/Name]
        [Position]: Co-founder and CEO [/Position]
        [Company]: Platform.sh [/Company]
        ###        
        [Text]: Microsoft (the word being a portmanteau of microcomputer software) was founded by Bill Gates on April 4, 1975, to develop and sell BASIC interpreters for the Altair 8800. Steve Ballmer replaced Gates as CEO in 2000, and later envisioned a devices and services strategy.
        [Name]:  Steve Ballmer [/Name]
        [Position]: CEO [/Position]
        [Company]: Microsoft [/Company]
        ###        
        [Text]: Franck Riboud was born on 7 November 1955 in Lyon. He is the son of Antoine Riboud, the previous CEO, who transformed the former European glassmaker BSN Group into a leading player in the food industry. He is the CEO at Danone.
        [Name]:  Franck Riboud [/Name]
        [Position]: CEO [/Position]
        [Company]: Danone [/Company]
        ###        
        """

        st.code(few_shot)

        st.header("Now try it yourself!")

        st.caption("Or copy this and manipulate it to your needs")

        st.caption("David Melvin is an investment and financial services professional at CITIC CLSA with over 30 years’ experience in investment banking and private equity. He is currently a Senior Adviser of CITIC CLSA.")


        text_val = st.text_input("Enter the textual description here")

        request= few_shot + "[Text]: " + text_val
        # Every form must have a submit button.
        submitted = st.form_submit_button("Extract Features")
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