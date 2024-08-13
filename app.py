import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


## sstreamlit APP
st.set_page_config(page_title="Talk-Brief AI", page_icon="👴")
st.title("👴 Talk-Brief AI: Summarize Text From YT or Website")
st.subheader("Summarize URL")
