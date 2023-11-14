import streamlit as st
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings 
import os
# from dotenv import load_dotenv
# load_dotenv()
import pandas as pd
import os
import re
import openai
from langchain_helper import load_data, get_response, getid, output_format, results

st.title("🦜🔗 Coupon Q&A")

with st.sidebar:
    brands_per_category = {
        "electronics": ["Sony", "Samsung", "LG", "Apple", "Dell"],
        "jewelry": ["Tiffany", "Cartier", "Pandora", "Swatch", "Bvlgari"],
        "apparel": ["Nike", "Adidas", "Zara", "H&M", "Gucci"],
        "accessories": ["Ray-Ban", "Fossil", "Kate Spade", "Michael Kors", "Coach"]
    }
    context="""You are searching for the best coupons available for the products in the ****.com website.
     you are looking for offers on the following products: """
    st.write(context+"\n\n")
    brands_per_category

llm=OpenAI(temperature=0.2,api_key=openai.api_key)


vectordb_file_path = "vectordb"
instructor_embeddings = OpenAIEmbeddings(api_key=openai.api_key)
# Load the CSV file
data = pd.read_csv('data_2.csv')



text = st.text_area('What kind of products you are looking for offers? Please refer the slidebar to the brands and categories. ')
# Display the data in a table
#   st.write(data)
submitted = st.button('Submit')
# clear = st.button('Clear')
if submitted:
    res,source=results(text)
    # print(res)
    if not (re.search("I don't know",res)):
        res
        "You can look into other offers from the following results:\n"
        for i in source:
            i
    else:
        "I don't know."
        "I cant suggest you other suggestions for your search"
