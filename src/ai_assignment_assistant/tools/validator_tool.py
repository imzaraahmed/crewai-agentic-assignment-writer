import os
from typing import Type

from pydantic import BaseModel, Field
from crewai.tools import BaseTool


class ValidatorToolInput(BaseModel):
    """Input schema for the assignment validator."""

    file_path: str = Field(
        default="draft_assignment.md",
        description="Path to the draft assignment Markdown file to validate."
    )


class AssignmentValidatorTool(BaseTool):
    name: str = "Assignment Validator"

    description: str = (
        "Validate a draft academic assignment Markdown file. "
        "Check whether it contains important academic sections such as "
        "a title, introduction, main sections, and conclusion."
    )

    args_schema: Type[BaseModel] = ValidatorToolInput

    def _run(self, file_path: str = "draft_assignment.md") -> str:
        if not os.path.exists(file_path):
            return f"Assignment file not found: {file_path}"

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            required_sections = {
                "Title": False,
                "Introduction": False,
                "Conclusion": False,
            }

            content_lower = content.lower()

            # Check for Markdown title
            if content.strip().startswith("#"):
                required_sections["Title"] = True

            # Check for Introduction
            if "introduction" in content_lower:
                required_sections["Introduction"] = True

            # Check for Conclusion
            if "conclusion" in content_lower:
                required_sections["Conclusion"] = True

            word_count = len(content.split())

            results = [
                f"File checked: {file_path}",
                f"Word count: {word_count}",
                "",
                "Section validation:",
            ]

            for section, found in required_sections.items():
                status = "PASS" if found else "MISSING"
                results.append(f"- {section}: {status}")

            if all(required_sections.values()):
                results.append("")
                results.append("Overall validation: PASS")
            else:
                results.append("")
                results.append("Overall validation: NEEDS IMPROVEMENT")

            return "\n".join(results)

        except Exception as e:
            return f"Validation failed: {e}"