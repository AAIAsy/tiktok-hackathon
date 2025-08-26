# Enter API key to access OpenAI models and embedding models

import getpass
import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass(os.getenv("OPENAI_API_KEY"))





# Embed them with embedding model and store in vector store with FAISS. Save the vectorstore afterwards.

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# choose embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")




# Choose LLM model

from langchain.chat_models import init_chat_model
llm = init_chat_model("gpt-4o-mini", model_provider="openai")


from langchain_core.prompts import ChatPromptTemplate

new_vector_store = FAISS.load_local(
    "faiss_index", 
    embeddings, 
    allow_dangerous_deserialization=True
)

retriever = new_vector_store.as_retriever()


while True:
    print("\n\n")
    print("==="*50)
    query = input("Enter your query ('q' to quit): ")
    
    if query.lower() == "q":
        break
    
    
    template = ChatPromptTemplate([
        ("system", """You are a helpful AI bot that summarizes answers regarding user queries. 
         Here is the context: {context}. If you don't know the answer, tell the user that you actually don't know, don't make up facts. 
         After telling your answer, finish it off with 'Is there anything else you would like to know?
         
         """),
        ("human", "{query}")
    ])

    prompt_value = template.invoke(
        {
            "query": query,
            "context": retriever.invoke(query)
        }
    )

    response = llm.invoke(prompt_value)
    print("\n\n")
    print(response.pretty_print())

