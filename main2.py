import streamlit as st
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv
import pandas as pd
import os
import re
from langchain_helper import load_data, get_response, getid, output_format, results

# Load environment variables from a .env file
load_dotenv()

# Initialize the OpenAI LLM
llm = OpenAI(temperature=0.2, api_key=os.environ["OPENAI_API_KEY"])

# Initialize the OpenAI Embeddings
vectordb_file_path = "vectordb"
instructor_embeddings = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])

# Load the CSV file
data = pd.read_csv('data_2.csv')

# Streamlit UI
st.title("🦜🔗 Coupon Suggestions App")

text = st.text_area('What kind of products are you looking for offers on?')
submitted = st.button('Submit')

# Create a session state to keep track of the output
if 'output_text' not in st.session_state:
    st.session_state.output_text = ""

# Display the data in a table
# st.write(data)

# Handle the "Submit" button click
if submitted:
    res, source = results("Do you have offers in apparel brand?")
    # Check if the response contains "I don't know"
    if not (re.search("I don't know", res)):
        # Display the results
        st.session_state.output_text += res+f"\nYou can look into other offers from the following results:\n"
        for i in source:
            st.session_state.output_text += f"{i}\n"
    else:
        # Display "I don't know" message
        st.session_state.output_text += "I don't know.\nI can't suggest you other suggestions for your search.\n"
    

# Create a "Clear" button to clear the output
clear = st.button('Clear')

# Handle the "Clear" button click
if clear:
    st.session_state.output_text = ""
    text=""

# Display the output
st.text_area("Output:", st.session_state.output_text, key="output_text")
