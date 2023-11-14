from langchain.document_loaders import CSVLoader
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from langchain.callbacks import StdOutCallbackHandler



import os
llm=OpenAI(temperature=0.2,api_key=os.environ["OPENAI_API_KEY"])


vectordb_file_path = "vectordb"
instructor_embeddings = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])
def load_data():
    loader = CSVLoader(file_path="data_2.csv",source_column="Sentence")
    documents = loader.load()
    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(documents=documents,
                                    embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)

def get_response():
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings)
    retriever = vectordb.as_retriever(score_threshold=0.8,k=3)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.  You are about to find any offers available for the question from the user and list the required content.
    You are searching for the best coupons available for the products
    you are looking for offers on the following products:

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )


    response = RetrievalQA.from_chain_type(llm=llm, 
                                         chain_type="stuff", 
                                         input_key="query",
                                         retriever=retriever, 
                                         return_source_documents=True,
                                         chain_type_kwargs={"prompt": PROMPT},
                                         callbacks=[StdOutCallbackHandler()],
                                         verbose=True,
                                         )

    return response

def getid(s_doc):
    df=pd.read_csv("data_2.csv")
    return [df.iloc[t.metadata["row"],-1]  for t in s_doc] 


import re

def output_format(input_string):
    # Extract words from the input string

    words = re.findall(r'\b[\w\']+\b', input_string)

    # Join the extracted words into a single string
    result = ' '.join(words)
    return result



def results(query):
    response = get_response()
    out=response(query)
    return output_format(out["result"]),getid(out["source_documents"])


if __name__=="__main__":
    # load_data()
    res,source=results("do you have any products in apple and samsung?")
    # print(res)
    if not (re.search(" I don't know",res)):
        print(res)
        print("\n\n")
        print("You can look into other offers from the following results:\n")
        print(source)
    else:
        print("I don't know.")
        print("I cant suggest you other suggestions for your search")