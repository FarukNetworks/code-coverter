from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool
from pathlib import Path
from code_doc_ai.tools import FileReadTool

def ensure_directory_exists(directory_path):
	Path(directory_path).mkdir(parents=True, exist_ok=True)

@CrewBase
class CodeDocAi():
	"""Migration expert crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self, inputs=None):
		self.inputs = inputs or {}
		super().__init__()
	
	@agent
	def code_converter(self) -> Agent:
		return Agent(
			config=self.agents_config['code_converter'],
			context="""
				Use the output from the code scanning task as input for the conversion.
				After converting the code:
				1. Get the original filename
				2. Replace the extension with .cs
				3. Use the FileWriterTool to save the converted code to the output-app directory
			""",
			tools=[
				FileReadTool(file_path=self.inputs['selected_file']),
				FileWriterTool(
					directory=self.inputs['code_directory'],
					filename_pattern='{filename}',
					before_write=lambda: ensure_directory_exists(self.inputs['code_directory'])
				),
			],
			verbose=True,
			temperature=0.1
		)
	
	@task
	def code_conversion_task(self) -> Task:
		return Task(
			config=self.tasks_config['code_conversion_task'],
			agent=self.code_converter(),
			expected_output="After converting the code, save it to a file in the output-app directory with the same name but .cs extension"
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CodeDocAi crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=[
				self.code_converter()
			],
			tasks=[
				self.code_conversion_task()
			],
			process=Process.sequential,
			verbose=True,
		)