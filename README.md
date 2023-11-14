# coupon_Q&A: Question and Answer System Based on OpeanAI and Langchain.

This is an end to end LLM project based on openai and Langchain. We are building a Q&A system for an e-commerce to provide coupons and offers using llm. This system will provide a streamlit based user interface for students where they can ask questions and get answers. 

## Project Highlights

- Use a real CSV file of offers that the company has right now.[dummy data which we have generated from the generate_data.py and have stored in the vectorstore FAISS.]
- We will build an LLM based question and answer system that can reduce the screen time of the user for prolonging to search for the offers.
- Users should be able to use this system to ask questions directly and get answers within seconds

## You will learn following,
  - Langchain + OpenAI: LLM based Q&A
  - Streamlit: UI
  - embeddings: OpenAIEmbeddings
  - FAISS: Vector databse

## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/Shyam-Sundar-7/coupon_Q-A.git
```


3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through openai and store the key in .env file as 

```bash
  OPENAI_API_KEY="sk-**********************************"
```

## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py
```

## Project Structure

- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.


## Issues and Recommendations:

- The model struggles to comprehend questions that involve multiple products. Its performance is noticeably better when dealing with single-product inquiries.
- Implementing a chatbot to handle checkout details and help users finalize their product selections from the suggested list could enhance customer engagement with the app.


## Local Setup Output in Streamlit

<div style="text-align: center;">
  <video src="video.mp4" controls width="400" height="300">
    Your browser does not support the video tag.
  </video>
</div>
