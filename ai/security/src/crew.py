import os
from dotenv import load_dotenv
from functools import cached_property
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.chat_models import ChatOpenAI


load_dotenv()


class OpenAIConfig:

	@cached_property
	def config(self) -> ChatOpenAI:
		"""Lazily initializes and returns OpenAI config."""
		return ChatOpenAI(
			model="gpt-4o",
			openai_api_key=os.getenv("OPENAI_API_KEY"),
			openai_api_base="https://api.openai.com/v1")


@CrewBase
class SecurityBase(OpenAIConfig):

	agents = None
	tasks = None
	agents_config: dict = 'config/agents.yaml'
	tasks_config: dict = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm=self.config
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Python crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=2)
