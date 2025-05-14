
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
        """
        Save the provided data to a text file with a timestamp.

        This function appends the given data to a specified text file, 
        prefixed with a timestamp and a header indicating it is research output.

        Parameters:
        - data (str): The research data to be saved.
        - filename (str): The name of the file to save the data to. Defaults to 'research_output.txt'.

        Returns:
        - str: A confirmation message indicating the data was successfully saved.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_data = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
        with open(filename, "a") as f:
                f.write(formatted_data)
        return f"Data successfully saved to {filename}"

save_tool = Tool(
        name="save_text_to_file",
        func=save_to_txt,
        description="Saves the research data to a text file",
        )

search = DuckDuckGoSearchRun()
search_tool = Tool(
        name="search",
        func=search.run,
        description="Search the web for information",
        )

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
