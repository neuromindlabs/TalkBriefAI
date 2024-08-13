import pkg_resources

# List of libraries you use
libraries = [
    "validators",
    "streamlit",
    "langchain",
    "langchain_google_genai",
    "langchain_community",
    "tiktoken",
]

# Open the requirements.txt file in write mode
with open("requirements.txt", "w") as file:
    for library in libraries:
        try:
            # Get the version of the library
            version = pkg_resources.get_distribution(library).version
            # Write the library and its version to the file
            file.write(f"{library}=={version}\n")
        except pkg_resources.DistributionNotFound:
            print(f"{library} is not installed.")
