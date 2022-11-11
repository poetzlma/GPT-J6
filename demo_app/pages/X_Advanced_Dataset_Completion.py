#importing required libraries
import requests
import json
import streamlit as st
import pandas as pd


st.title("Dataset Completion - Scoring")

st.write("This whill show how to complete missing Classifications Values in a Dataset")

st.caption(" A Survey was taken where score was not mandatory:")

df = pd.read_csv("pages/files/data_completion.csv")

st.write(df)

@st.experimental_memo
def convert_df(df):
     return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button(
"Press to Download",
csv,
"file.csv",
"text/csv",
key='download-csv'
)

st.write("You may now download the Data as CSV and upload it again, or do some modifications and upload it again")

st.header("Upload Your Dataset")
file = st.file_uploader("Upload Your Dataset")
if file: 
     df = pd.read_csv(file, index_col=None)
     #df.to_csv('dataset.csv', index=None)
     # st.dataframe(df)

     result = st.button("Start Completion")

     if result:
          if not file:
               #connect both strings
               st.write("Upload a Dataset first")
          else:
               #st.write(df.columns.tolist())

               empty_columns = df[df[' score'] == " "]
               full_columns = df[df[' score'] != " "]


               st.write("The following Survey Scores are missing:")
               st.dataframe(empty_columns)

               st.write("Creating Missing Values...")

               few_shot = ""

               for index, row in full_columns.iterrows():

                    few_shot = few_shot + "[Comment]: " + row[' comment'] + " [Score]: " + str(row[' score']) + " ###"

               #st.write(few_shot)                            

               for index, row in empty_columns.iterrows():

                    text_val = few_shot + row[' comment'] + " [Score]: "

                    #connect both strings
                    url = 'http://127.0.0.1:5002/generate'

                    payload ="{'body': '" + str(text_val) + "', 'token': '15'}"
                    payload = payload.replace("'", '"')

                    # st.write(payload)

                    r = requests.get(url, json=payload)
                    data = r.content.decode("utf-8")
                    
                    answer = json.loads(data)['result'].split("###")[len(full_columns.index)] 

                    update = empty_columns[' comment'] == row[' comment']
                    empty_columns.loc[update, ' score'] = answer.split("[Score]: ")[1]

                    st.write(answer)

               st.header("Download the completed Dataset")
               
               combined = pd.concat([full_columns, empty_columns])

               st.dataframe(combined)

               @st.experimental_memo
               def convert_df(combined):
                    return combined.to_csv(index=False).encode('utf-8')

               csv = convert_df(combined)

               st.download_button(
               "Press to Download filled CSV",
               csv,
               "filled_file.csv",
               "text/csv",
               key='download-filled-csv'
               )

               