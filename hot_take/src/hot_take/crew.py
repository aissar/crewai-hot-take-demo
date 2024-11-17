from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from hot_take.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
# from pydantic import BaseModel, Field

@CrewBase
class HotTake():
	"""HotTake crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def thought_tree_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['thought_tree_generator'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			# verbose=True,
			# memory=False,
		)

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			# verbose=True,
			# memory=False,
		)
	
	@agent
	def reporter(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			# verbose=True,
			# memory=False,
		)
	
	@task
	def generate_thought_tree(self) -> Task:
		return Task(
			config=self.tasks_config['generate_thought_tree'],
			output_file='./tmp/thought_tree_branches.json'
		)
	
	@task
	def research_consensus_perspective(self) -> Agent:
		return Task(
			config=self.tasks_config['research_consensus_perspective'],
			output_file='./tmp/thought_tree_branch_1.json'
		)
	
	@task
	def research_counterfactual_perspective(self) -> Agent:
		return Task(
			config=self.tasks_config['research_counterfactual_perspective'],
			output_file='./tmp/thought_tree_branch_2.json'
		)
	
	@task
	def research_nuance_perspective(self) -> Agent:
		return Task(
			config=self.tasks_config['research_nuance_perspective'],
			output_file='./tmp/thought_tree_branch_3.json'
		)
	
	@task
	def generate_report(self) -> Agent:
		return Task(
			config=self.tasks_config['generate_report'],
			output_file='./tmp/report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the HotTake crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
