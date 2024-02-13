from llama_index.readers import SimpleDirectoryReader
from llama_index import VectorStoreIndex
import llama_index  
import os
from dotenv import load_dotenv

load_dotenv()

def main(url:str)->None:
    document = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(document)
    query_engine =  index.as_query_engine()
    response = query_engine.query("What is the article,plz summarize it")
    print(response)

if __name__ == "__main__":
    main(url=r"C:\Users\DELL\Downloads\Data")
