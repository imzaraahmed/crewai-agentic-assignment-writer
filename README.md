<<<<<<< HEAD
# 🤖 CrewAI Agentic Assignment Writer

> **Research. Write. Review. — Powered by CrewAI Agents.**

CrewAI Agentic Assignment Writer is an AI-powered academic assignment generation system built using **CrewAI**.

The project uses multiple specialized AI agents that collaborate sequentially to transform an assignment topic into a structured, polished academic assignment.

The system currently uses three agents:

* 🔎 **Researcher Agent** — researches and organizes information about the given topic.
* ✍️ **Writer Agent** — transforms the research into a structured academic assignment.
* 📝 **Reviewer Agent** — reviews and improves the generated assignment for clarity, grammar, structure, and completeness.

---

## ✨ Features

* 🤖 Multi-agent AI workflow using CrewAI
* 🔎 Automated topic research
* ✍️ AI-powered academic assignment writing
* 📝 Automated assignment review and refinement
* 🔄 Sequential agent collaboration
* 📄 Generates the final assignment as a Markdown file
* 🧩 YAML-based agent and task configuration
* 🔐 Environment variable support for API keys
* 🐍 Built with Python

---

## 🏗️ Agentic Workflow

```text
                Assignment Topic
                       │
                       ▼
              ┌─────────────────┐
              │ Researcher Agent│
              └────────┬────────┘
                       │
                  Research
                       │
                       ▼
              ┌─────────────────┐
              │   Writer Agent  │
              └────────┬────────┘
                       │
                Draft Assignment
                       │
                       ▼
              ┌─────────────────┐
              │  Reviewer Agent │
              └────────┬────────┘
                       │
                 Final Review
                       │
                       ▼
              ┌─────────────────┐
              │  assignment.md  │
              └─────────────────┘
```

### How it works

1. The user provides an assignment topic.
2. The **Researcher Agent** gathers and organizes relevant information.
3. The **Writer Agent** uses the research to create a structured assignment.
4. The **Reviewer Agent** checks the assignment for grammar, clarity, structure, formatting, and completeness.
5. The final polished assignment is saved as `assignment.md`.

---

## 🛠️ Technologies Used

| Technology | Purpose                                      |
| ---------- | -------------------------------------------- |
| Python     | Core programming language                    |
| CrewAI     | Multi-agent AI framework                     |
| OpenRouter | LLM API provider                             |
| YAML       | Agent and task configuration                 |
| Markdown   | Generated assignment format                  |
| UV         | Python dependency and environment management |

---

## 👥 AI Agents

### 🔎 Researcher Agent

The Researcher Agent is responsible for:

* Understanding the assignment topic
* Gathering relevant information
* Identifying important concepts and facts
* Organizing research
* Providing research material for the Writer Agent

### ✍️ Writer Agent

The Writer Agent transforms the research into an academic assignment containing:

* Title
* Introduction
* Main sections
* Subheadings
* Examples
* Explanations
* Conclusion

### 📝 Reviewer Agent

The Reviewer Agent reviews the generated assignment for:

* Grammar
* Spelling
* Punctuation
* Sentence structure
* Clarity
* Logical flow
* Formatting
* Completeness
* Academic structure

It then produces the final polished version.

---

## 📁 Project Structure

```text
crewai-agentic-assignment-writer/
│
├── .gitignore
├── AGENTS.md
├── README.md
├── assignment.md
├── pyproject.toml
├── rag_test.py
├── uv.lock
│
├── knowledge/
│
└── src/
    └── ai_assignment_assistant/
        ├── __init__.py
        ├── crew.py
        ├── main.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

> API keys and environment variables are stored in `.env` and are excluded from Git using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/crewai-agentic-assignment-writer.git
cd crewai-agentic-assignment-writer
```

### 2. Create a virtual environment

```bash
py -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

If using the CrewAI project environment:

```bash
crewai install
```

Or install the project dependencies according to `pyproject.toml`.

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENROUTER_API_KEY=your_api_key_here
MODEL=openai/gpt-4.1-mini
```

**Never commit your `.env` file or expose your API key publicly.**

---

## ▶️ Run the Project

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Run the CrewAI project:

```bash
crewai run
```

The application will ask:

```text
Enter your assignment topic:
```

For example:

```text
Artificial Intelligence
```

The CrewAI agents will then work sequentially to generate the assignment.

---

## 📄 Output

After successful execution, the final assignment is generated as:

```text
assignment.md
```

Example workflow:

```text
Input:
Generative AI

        ↓

Researcher Agent

        ↓

Writer Agent

        ↓

Reviewer Agent

        ↓

Output:
assignment.md
```

---

## 🧪 Example

### Input

```text
Generative AI
```

### Output

The system generates a structured academic assignment containing sections such as:

```text
# Generative AI

## Introduction

## Understanding Generative AI

## Applications

## Advantages

## Challenges and Ethical Considerations

## Future Outlook

## Conclusion
```

---

## 🎯 Project Goal

The goal of this project is to demonstrate how **agentic AI and multi-agent collaboration** can be used to automate academic assignment creation.

Instead of relying on a single AI agent, the system divides the work between specialized agents, with each agent responsible for a specific stage of the workflow.

```text
Research → Writing → Reviewing
```

This approach demonstrates:

* Multi-agent collaboration
* Role-based AI agents
* Task orchestration
* Sequential workflows
* Automated content generation
* AI-assisted academic writing

---

## 🚀 Future Improvements

* 🔎 Add web search tools for real-time research
* 📚 Add citation and reference generation
* 📄 Support PDF and DOCX assignment export
* 💬 Add an interactive Streamlit interface
* 🧰 Give agents external tools and APIs
* 👤 Add personalized assignment preferences
* 🧠 Improve fact verification
* 📊 Add assignment quality scoring

---

## 👩‍💻 Author

**Zara Ahmed**

BSCS Final Semester Student | Aspiring AI & Data Science Engineer

### Skills Demonstrated

`Python` `CrewAI` `Agentic AI` `Multi-Agent Systems` `LLMs` `Prompt Engineering` `YAML` `OpenRouter`

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

=======
# AiAssignmentAssistant Crew

Welcome to the AiAssignmentAssistant Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/ai_assignment_assistant/config/agents.yaml` to define your agents
- Modify `src/ai_assignment_assistant/config/tasks.yaml` to define your tasks
- Modify `src/ai_assignment_assistant/crew.py` to add your own logic, tools and specific args
- Modify `src/ai_assignment_assistant/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the ai_assignment_assistant Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The ai_assignment_assistant Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the AiAssignmentAssistant Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
>>>>>>> 4d518e2 (Initial working CrewAI assignment writer)
