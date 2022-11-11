#importing required libraries
import requests
import json
import streamlit as st

with st.form("my_form"):
    st.header("SQL Query From Description")
    st.write("The following will show how to generate a sql query from your prompt")

    st.caption("---- Some Examples are: ----")

    st.write("Show all companies along with the number of employees in each department.")
    st.code("SELECT COMPANY, COUNT(COMPANY) FROM Employee GROUP BY COMPANY;", language="SQL")

    st.write("Show the last record of the Employee table.")
    st.code("SELECT * FROM Employee ORDER BY LAST_NAME DESC LIMIT 1;", language="SQL")

    st.write("Fetch the companies that have less than five people in it.")
    st.code("SELECT COMPANY, COUNT(EMPLOYEE_ID) FROM Employee GROUP BY COMPANY HAVING COUNT(EMPLOYEE_ID) < 5;", language="SQL")


    st.header("Now try it yourself!")

    few_shot = """Question: Fetch the companies that have less than five people in it.
            Answer: SELECT COMPANY, COUNT(EMPLOYEE_ID) FROM Employee GROUP BY COMPANY HAVING COUNT(EMPLOYEE_ID) < 5;
            ---
            Question: Show all companies along with the number of employees in each department
            Answer: SELECT COMPANY, COUNT(COMPANY) FROM Employee GROUP BY COMPANY;
            ---
            Question: Show the last record of the Employee table
            Answer: SELECT * FROM Employee ORDER BY LAST_NAME DESC LIMIT 1;
            ---
            Question: """


    text_val = st.text_input("Enter your natural language description here:")

    request= few_shot + text_val + " Answer:"

    # Every form must have a submit button.
    submitted = st.form_submit_button("Generate SQL Query")
    if submitted:
            #connect both strings
            url = 'http://127.0.0.1:5002/generate'

            payload ="{'body': '" + str(request) + "', 'token': '10'}"
            payload = payload.replace("'", '"')

            # st.write(payload)

            r = requests.get(url, json=payload)
            data = r.content.decode("utf-8")
            
            s = json.loads(data)

            answer = s['result'].split("Answer:")[4].split("---")[0]

            st.code(answer)

st.write("If i am light grey i am working")