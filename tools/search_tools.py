from langchain_community.tools import DuckDuckGoSearchResults
from langchain.tools import tool

class SearchTools:

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a given topic and return relevant results"""
        print("Searching the internet...")
        search = DuckDuckGoSearchResults()
        results = search.run(query)
        top_result_to_return = 5
        formatted_results = []

        if not results:
            return "Sorry, I couldn't find anything about that."

        for result in results[:top_result_to_return]:
            try:
                # Attempt to extract the date if available
                date = result.get('date', 'Date not available')
                formatted_results.append('\n'.join([
                    f"Title: {result['title']}",
                    f"Link: {result['link']}",
                    f"Date: {date}",
                    f"Snippet: {result['snippet']}",
                    "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(formatted_results)
