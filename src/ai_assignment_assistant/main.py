#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from ai_assignment_assistant.crew import AiAssignmentAssistant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the AI Assignment Assistant.
    """

    topic = input("Enter your assignment topic: ")

    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year)
    }

    try:
        AiAssignmentAssistant().crew().kickoff(inputs=inputs)
        print("\n✅ Assignment generated successfully!")
        print("📄 Check the file: assignment.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """

    topic = input("Enter your assignment topic: ")

    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year)
    }

    try:
        AiAssignmentAssistant().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """

    try:
        AiAssignmentAssistant().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """

    topic = input("Enter your assignment topic: ")

    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year)
    }

    try:
        AiAssignmentAssistant().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """

    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided.")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": trigger_payload.get("topic", ""),
        "current_year": str(datetime.now().year)
    }

    try:
        result = AiAssignmentAssistant().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")