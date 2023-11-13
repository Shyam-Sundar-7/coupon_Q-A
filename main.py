import streamlit as st
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings 
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
import os
import re

from langchain_helper import load_data, get_response, getid, output_format, results

"🦜🔗 Coupon Suggestions App"

llm=OpenAI(temperature=0.2,api_key=os.environ["OPENAI_API_KEY"])


vectordb_file_path = "vectordb"
instructor_embeddings = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])
# Load the CSV file
data = pd.read_csv('data_2.csv')



text = st.text_area('What kind of products you are looking for offers?')
# Display the data in a table
#   st.write(data)
submitted = st.button('Submit')
clear = st.button('Clear')
if submitted:
    res,source=results("Do you have offers in apparal brand?")
    # print(res)
    if not (re.search("I don't know",res)):
        res
        "You can look into other offers from the following results:\n"
        for i in source:
            i
    else:
        "I don't know."
        "I cant suggest you other suggestions for your search"
if clear:
    st.write("")