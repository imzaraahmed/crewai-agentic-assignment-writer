#from crewai import Agent, Crew, Process, Task
import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class AiAssignmentAssistant:
    """AI Assignment Assistant Crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    llm = LLM(
        model="openai/gpt-4.1-mini",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        max_tokens=4096,
    )

    # -------------------------
    # Agents
    # -------------------------

    @agent
    def researcher(self) -> Agent:
      return Agent(
    config=self.agents_config["researcher"],
    llm=self.llm,
    verbose=True
)

    @agent
    def writer(self) -> Agent:
      return Agent(
    config=self.agents_config["writer"],
    llm=self.llm,
    verbose=True
)

    @agent
    def reviewer(self) -> Agent:
     return Agent(
    config=self.agents_config["reviewer"],
    llm=self.llm,
    verbose=True
)

    # -------------------------
    # Tasks
    # -------------------------

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["writing_task"],
            context=[self.research_task()]
        )

    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_task"],
            context=[self.writing_task()],
            output_file="assignment.md"
        )

    # -------------------------
    # Crew
    # -------------------------

    @crew
    def crew(self) -> Crew:
        """Creates the AI Assignment Assistant crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )