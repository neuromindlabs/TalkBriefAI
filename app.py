import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken  # Importing the tiktoken library
from langchain.chains import LLMChain

# from langchain.llms import openai


# import nltk

# nltk.download("punkt")
# # Download the NLTK data to the current directory
# nltk.download(
#     "averaged_perceptron_tagger_eng",
#     download_dir=".",
# )

# # Add the current directory to NLTK's data search paths
# nltk.data.path.append(".")


from langchain.document_loaders import WebBaseLoader, PyPDFLoader
import requests
from urllib.parse import urlparse


# from langchain import RunnableSequence
from langchain.prompts import PromptTemplate


## Streamlit APP
st.set_page_config(page_title="Talk-Brief AI", page_icon="👴")
st.title("👴 Talk-Brief AI: Interact with YT or Website")
st.subheader("Get an Overview of URL")

## Get the google_api_key and url(YT or website) to be summarized
with st.sidebar:
    google_api_key = st.text_input("Google API Key", value="", type="password")
    # Display a button
    if st.button("Get your Google API Key"):
        st.write("Go to Google AI Studio...")
        st.markdown(
            "[Click here to go to Google AI Studio](https://ai.google.dev/aistudio)"
        )

## Call the gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=google_api_key,
)


def calculate_tokens(text):
    """
    Calculate the number of tokens in the given text using the tiktoken tokenizer.
    """
    encoding = tiktoken.encoding_for_model(
        "gpt-3.5-turbo"
    )  # Specify the model encoding
    token_count = len(encoding.encode(text))
    return token_count


# Stuff-chain
def stuff_chain(docs):
    prompt_template = """
    Provide a summary of the following content in 300 words:
    Content:{text}
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
    output_summary = chain.run(docs)
    return output_summary


def map_reduce(docs):
    final_documents = RecursiveCharacterTextSplitter(
        chunk_size=2000, chunk_overlap=100
    ).split_documents(docs)

    chunks_prompt = """
    Please summarize the below speech:
    Speech:`{text}'
    Summary:
    """
    map_prompt_template = PromptTemplate(
        input_variables=["text"], template=chunks_prompt
    )

    final_prompt = """
    Provide the final summary of the entire speech with these important points.
    Add a Motivation Title, Start the precise summary with an introduction, and provide the summary in numbered 
    points for the speech.
    Speech:{text}
    """
    final_prompt_template = PromptTemplate(
        input_variables=["text"], template=final_prompt
    )

    summary_chain = load_summarize_chain(
        llm=llm,
        chain_type="map_reduce",
        map_prompt=map_prompt_template,
        combine_prompt=final_prompt_template,
        verbose=True,
    )

    output_summary = summary_chain.run(final_documents)
    return output_summary


# Old less efficient version but this one is actually how refine works
# def refine(docs):
#     final_documents = RecursiveCharacterTextSplitter(
#         chunk_size=2000, chunk_overlap=100
#     ).split_documents(docs)

#     chain = load_summarize_chain(llm=llm, chain_type="refine", verbose=True)
#     output_summary = chain.run(final_documents)
#     return output_summary


# Enhanced version of refine
def refine(docs):
    # Split the documents into chunks for processing
    final_documents = RecursiveCharacterTextSplitter(
        chunk_size=2000, chunk_overlap=100
    ).split_documents(docs)

    # Load the summarize chain with the "refine" method
    chain = load_summarize_chain(llm=llm, chain_type="refine", verbose=True)

    # Run the chain on the final documents
    output_summary = chain.run(final_documents)

    # Prepare the final prompt with the output summary
    final_prompt = f"""
    Provide the final summary of the entire speech with these important points.
    Add a Title, start the precise summary with an introduction and provide the summary in numbered 
    points for the speech.
    
    Speech: {output_summary}
    """

    # Create a LLMChain using PromptTemplate
    prompt_template = PromptTemplate(input_variables=["summary"], template=final_prompt)
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # Run the chain and get the response
    final_output = chain.run({"summary": output_summary})

    return final_output


generic_url = st.text_input("URL", label_visibility="collapsed")

if generic_url:
    ## Validate the URL
    if not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YT video URL or website URL")
    else:
        try:
            with st.spinner("Analyzing the content..."):
                ## loading the website or YT video data
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                        generic_url, add_video_info=True
                    )

                else:

                    # loader = UnstructuredURLLoader(
                    #     urls=[generic_url],
                    #     ssl_verify=False,
                    #     headers={
                    #         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                    #     },
                    # )
                    response = requests.head(generic_url, allow_redirects=True)
                    content_type = response.headers.get("Content-Type", "").lower()

                    if "application/pdf" in content_type:
                        print("PDF detected. Using PyPDFLoader...")
                        loader = PyPDFLoader(generic_url)
                        # documents = pdf_loader.load()
                    else:
                        print("Web page detected. Using WebBaseLoader...")
                        loader = WebBaseLoader(generic_url)
                        # documents = web_loader.load()

                docs = loader.load()

                # Calculate token count
                token_count = calculate_tokens(str(docs))
                st.info(f"Total Tokens: {token_count}")

                # Suggest summarization type based on token count
                if token_count < 1000:
                    suggested_type = "Stuffchain"
                elif 1000 <= token_count < 3000:
                    suggested_type = "Map-reduce"
                else:
                    suggested_type = "Refine"

                st.info(f"Suggested Summarization Type: {suggested_type}")

                # Dropdown menu for selecting summarization type
                summarization_type = st.selectbox(
                    "Select Summarization Type",
                    ["Stuffchain", "Map-reduce", "Refine"],
                    index=["Stuffchain", "Map-reduce", "Refine"].index(suggested_type),
                )

        except Exception as e:
            st.exception(f"Exception: {e}")

if st.button("Get an overview of the Content from YT or Website"):
    ## Validate all the inputs
    if not google_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YT video URL or website URL")
    else:
        try:
            with st.spinner("Summarizing..."):
                ## loading the website or YT video data
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                        generic_url, add_video_info=True
                    )

                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                        },
                    )

                # docs = loader.load()
                try:
                    docs = loader.load()
                except Exception as e:
                    st.error(f"Error loading the URL: {str(e)}")

                # Perform the summarization
                if summarization_type == "Stuffchain":
                    output_summary = stuff_chain(docs)
                elif summarization_type == "Map-reduce":
                    output_summary = map_reduce(docs)
                else:
                    output_summary = refine(docs)

                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception: {e}")
