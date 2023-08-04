# streamlit_app.py

import streamlit as st
from langchain.document_loaders import UnstructuredCSVLoader
from langchain.chat_models import ChatOpenAI
from langchain.indexes import VectorstoreIndexCreator

# Load environment variables
st.sidebar.markdown("### OpenAI API Key")
openai_api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

# Check if the API key starts with "sk-"
if openai_api_key.strip().startswith("sk-"):
    OPENAI_API_KEY = openai_api_key.strip()
    # Configure OpenAI API
    openai.api_key = OPENAI_API_KEY
    proceed = True
else:
    proceed = False
    st.sidebar.warning("OpenAI API key should start with 'sk-'")

OPENAI_API_KEY = openai_api_key


# Load the model and data
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
data = UnstructuredCSVLoader('final.csv')
index = VectorstoreIndexCreator().from_loaders([data])


def main():
    st.title("Sleek LangChain Chat App")
    st.write("Enter your query in the text box below and press Enter.")

    # Get user input
    question = st.text_input('Enter your query:', '')

    if st.button("Submit"):
        if question.strip() != '':
            # Get the response from the LangChain model
            response = index.query(llm=llm, question=question, chain_type="stuff")

            # Display the response
            st.markdown("### Response:")
            st.write(response)

if __name__ == "__main__":
    main()
