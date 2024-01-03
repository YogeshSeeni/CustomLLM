from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import WebBaseLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from dotenv import dotenv_values
from langchain.retrievers.multi_query import MultiQueryRetriever

def initialize_llm():
    config = dotenv_values(".env")

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=config["CHATGPT_KEY"])

    return llm

def initialize_vector_database():
    config = dotenv_values(".env")

    embeddings = OpenAIEmbeddings(openai_api_key=config["CHATGPT_KEY"])
    vectorstore = Chroma("langchain_store", embeddings)

    return vectorstore

def add_website(url, db):
    loader = WebBaseLoader(url)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    db.add_documents(all_splits)

def add_pdf(doc, db):
    loader = PyPDFLoader(doc)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    db.add_documents(all_splits)

def add_text(texts, db):
    db.add_texts(texts)

def pass_prompt_similarity(llm, query, db):
    # Prompt
    prompt = PromptTemplate.from_template("""
        You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise: 
        Question: {question}
        Context: {documents}
        Answer:
    """)

    # Chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    # Run
    docs = db.similarity_search(query)
    print(docs)
    result = llm_chain({"documents": docs, "question": query})

    return result["text"]

def pass_prompt_similarity(llm, query, db):
    # Prompt
    prompt = PromptTemplate.from_template("""
        You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise: 
        Question: {question}
        Context: {documents}
        Answer:
    """)

    # Chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    # Run
    docs = db.similarity_search(query)
    print(docs)
    result = llm_chain({"documents": docs, "question": query})

    return result["text"]

def pass_prompt_mmr(llm, query, db):
    # Prompt
    prompt = PromptTemplate.from_template("""
        You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise: 
        Question: {question}
        Context: {documents}
        Answer:
    """)

    # Chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    # Run
    retriever = db.as_retriever(search_type="mmr")
    docs = retriever.get_relevant_documents(query)
    result = llm_chain({"documents": docs, "question": query})

    return result["text"]

def pass_prompt_mmr(llm, query, db):
    # Prompt
    prompt = PromptTemplate.from_template("""
        You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise: 
        Question: {question}
        Context: {documents}
        Answer:
    """)

    # Chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    # Run
    retriever = db.as_retriever(search_type="mmr")
    docs = retriever.get_relevant_documents(query)
    result = llm_chain({"documents": docs, "question": query})

    return result["text"]

def pass_prompt_multi_query(query, db):
    try:
        # Prompt
        prompt = PromptTemplate.from_template("""
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise: 
            Question: {question}
            Context: {documents}
            Answer:
        """)

        # Chain
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        
        # Run
        retriever_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        retriever_from_llm = MultiQueryRetriever.from_llm(
            retriever=db.as_retriever(), llm=retriever_llm
        )
        docs = retriever_from_llm.get_relevant_documents(query)
        result = llm_chain({"documents": docs, "question": query})

        return result["text"]
    except:
        # Prompt
        prompt = PromptTemplate.from_template("""
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise: 
            Question: {question}
            Context: {documents}
            Answer:
        """)

        # Chain
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        
        # Run
        retriever_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        retriever_from_llm = MultiQueryRetriever.from_llm(
            retriever=db.as_retriever(), llm=retriever_llm
        )
        docs = retriever_from_llm.get_relevant_documents(query)
        result = llm_chain({"documents": docs[:2], "question": query})

        return result["text"]