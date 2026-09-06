import os
import requests
from typing import Type

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

load_dotenv()


class SearchToolInput(BaseModel):
    """Input schema for the web search tool."""

    query: str = Field(
        ...,
        description="The search query to search on the web."
    )


class SearchTool(BaseTool):
    name: str = "Web Search"

    description: str = (
        "Search the web using the Serper API. "
        "Use this tool to find current and relevant information "
        "about a topic."
    )

    args_schema: Type[BaseModel] = SearchToolInput

    def _run(self, query: str) -> str:
        api_key = os.getenv("SERPER_API_KEY")

        if not api_key:
            return "SERPER_API_KEY is not configured in the .env file."

        url = "https://google.serper.dev/search"

        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json",
        }

        payload = {
            "q": query,
            "num": 5,
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30,
            )

            response.raise_for_status()

            data = response.json()

            organic_results = data.get("organic", [])

            if not organic_results:
                return f"No web results found for: {query}"

            results = []

            for i, item in enumerate(organic_results[:5], 1):
                title = item.get("title", "No title")
                snippet = item.get("snippet", "No snippet")
                link = item.get("link", "")

                results.append(
                    f"{i}. {title}\n"
                    f"   {snippet}\n"
                    f"   URL: {link}"
                )

            return "\n\n".join(results)

        except requests.RequestException as e:
            return f"Search failed: {e}"