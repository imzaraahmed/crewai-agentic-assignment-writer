import os
from typing import Type

from pydantic import BaseModel, Field
from crewai.tools import BaseTool


class FileWriterToolInput(BaseModel):
    """Input schema for the file writer tool."""

    content: str = Field(
        ...,
        description="The assignment content to save to a Markdown file."
    )

    filename: str = Field(
        default="draft_assignment.md",
        description="The name of the Markdown file to create."
    )


class FileWriterTool(BaseTool):
    name: str = "Assignment File Writer"

    description: str = (
        "Save assignment content to a Markdown file. "
        "Use this tool after writing the assignment to create a draft "
        "file that can be reviewed by another agent."
    )

    args_schema: Type[BaseModel] = FileWriterToolInput

    def _run(
        self,
        content: str,
        filename: str = "draft_assignment.md"
    ) -> str:

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)

            return f"Assignment successfully saved to {filename}"

        except Exception as e:
            return f"File writing failed: {e}"