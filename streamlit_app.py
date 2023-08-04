from langchain.document_loaders import UnstructuredCSVLoader
from langchain.chat_models import ChatOpenAI
from langchain.indexes import VectorstoreIndexCreator
import os


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
    openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
    if openai_api_key !=None:
        os.enviorn['OPENAI_API_KEY']= openai_api_key
        # Load the model and data
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        data = UnstructuredCSVLoader('final.csv')
        index = VectorstoreIndexCreator().from_loaders([data])
        st.title("LangChain Chat with your Data App")
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
