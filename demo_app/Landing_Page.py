# Contents of ~/my_app/streamlit_app.py
import streamlit as st

# to hide the hamburger menu use /?embed=true at the end of url

st.markdown("# NLP Transformer Few Shot Demo Space")

st.write("""A Few Shot Learning is based on the idea of “one shot learning”
 where an algorithm is trained to predict a category for an input.""")

st.write("""  This algorithm is then used to make predictions on unseen inputs.
  In the case of Few shot learning, the algorithm is trained on a small number of labeled data
   and the model is expected to work on a new problem.""")

st.write("""The idea behind this is that the model learns to generalize the knowledge gained from a few labeled examples. """)

st.write("This space is to demonstrate the power of this and show differnt use cases")

st.subheader("<-- Use the Menu left to select a Demo Use Case")