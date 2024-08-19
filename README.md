# 🚀 Talk-Brief AI: Interact with YouTube or Website
<div align="center">
<h2>https://talkbriefai.streamlit.app/ </h2>
</div>

Welcome to the **Talk-Brief AI** repository! This project leverages LangChain and Google's gemini-1.5-flash LLM to provide users with concise overviews of content from YouTube videos or websites. The application is built using Streamlit, making it easy to deploy as a web app for summarizing lengthy or complex online content.
<div align="center">
  <img src="talk_brief_ai_summarize_youtube_videos_and_websites_with_ease.jpeg" alt="Project Image" width="500">

<br>
  <p>
  <img src="https://img.shields.io/badge/Python-black?logo=python&logoSize=auto&labelColor=%23f7f7f7&color=%233776AB&link=https%3A%2F%2Fwww.python.org%2F" alt="Python Badge">
  <img src="https://img.shields.io/badge/Streamlit-black?logo=streamlit&logoSize=auto&labelColor=%23f7f7f7&color=%23FF4B4B&link=https%3A%2F%2Fstreamlit.io%2F" alt="Streamlit Badge">
  <img src="https://img.shields.io/badge/LangChain-black?logo=langchain&logoColor=%231C3C3C&logoSize=auto&labelColor=%23f7f7f7&color=%231C3C3C&link=https%3A%2F%2Fwww.langchain.com%2F" alt="LangChain Badge">
  <img src="https://img.shields.io/badge/MIT-black?logoColor=%23f55036&logoSize=auto&label=license&labelColor=grey&color=%20%233da639&link=https%3A%2F%2Fopensource.org%2Flicense%2FMIT" alt="MIT Badge">
  </p>
</div>

## 🔗 Project Deployment
The project is currently hosted with the help of Streamlit. You can access the live version of the application through this link: https://talkbriefai.streamlit.app/.


## 📚 Table of Contents
- [🚀 Talk-Brief AI: Interact with YouTube or Website](#-talk-brief-ai-interact-with-youtube-or-website)
- [🔗 Project Deployment](#-project-deployment)
- [✨ Features](#-features)
- [🛠️ Installation](#-installation)
- [📄 Usage](#-usage)
- [🔄 Summarization Methods](#-summarization-methods)
- [🖼️ Example](#-example)
- [📜 License](#-license)
- [📄 References](#-references)


## ✨ Features

- **Google API Integration**: Securely integrates with Google's Generative AI models using your API key.
- **YouTube and Website Support**: Handles both YouTube video URLs and regular website URLs for content summarization.
- **Automatic Best Summarization Technique Recommendation**: Automatically calculates the number of tokens in the text to recommend the most appropriate summarization method.
- **Multiple Summarization Techniques**:
  - **Stuff Chain**: Ideal for short texts, providing a straightforward summary.
  - **Map-Reduce**: Best for medium-length texts, breaking down the content into chunks before combining the results.
  - **Refine**: Suitable for long texts, refining the summary iteratively to ensure accuracy and coherence.
- **User-Friendly Interface**: Simple, interactive UI built with Streamlit.

## 🛠️ Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/neuromindlabs/TalkBriefAI.git
   ```
2. Navigate to the project directory.
   ```bash
   cd talk-brief-ai
   ```
3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```
   
## 📄 Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
2. **Provide Your Google API Key**:
   - Enter your Google API Key in the sidebar. If you don’t have one, follow the provided link to obtain it.
3. **Enter a URL**:
   - Input a YouTube video URL or any website URL in the main input field.
4. **Select Summarization Type**:
   - Based on the calculated token count, a suggested summarization type will be displayed. You can select it or choose another method.
5. **Generate Summary**:
   - Click on the "Get an overview of the Content from YT or Website" button to generate the summary.
  
## 🔄 Summarization Methods

- **Stuff Chain**: Best suited for short documents or small text content. It runs a simple summarization on the provided text.
- **Map-Reduce**: Breaks down large texts into smaller chunks, summarizes them individually, and then combines them into a cohesive summary.
- **Refine**: Iteratively refines the summary, ensuring that key details are not lost, even in lengthy documents.

## 🖼️ Example 
<div align="center">
  <img src="Screenshot 2024-08-17 at 8.02.18 PM.png" alt="Project Image" width="1000">
</div>
<div align="center">
  <img src="Screenshot 2024-08-17 at 8.02.35 PM.png" alt="Project Image" width="1000">
</div>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📄 References

- **[LangChain](https://www.langchain.com/)**: For providing the tools to create advanced summarization chains.
- **[Streamlit](https://streamlit.io/)**: For making it easy to build and deploy interactive web apps.
- **[Google Generative AI](https://ai.google.dev/aistudio)**: For powering the language models used in the summarization process.
