from crewai import Crew, Process
from langchain_community.llms import Ollama
from agents import AINewsLetterAgents
from task import AINewsletterTask
from file_io import save_markdown

lama = Ollama(
    model='mixtral'
)

agents = AINewsLetterAgents()
task = AINewsletterTask()

# setting up agents
editor = agents.editor_agent()
news_fetcher = agents.news_fetch_agent()
news_analyzer = agents.news_analyzer_agent()  # Fixed method name
newsletter_compiler = agents.newsletter_compiler_agent()

# setting up tasks
fetch_news_task = task.fetch_news_task(news_fetcher)
analyzed_news_task = task.analyze_news_task(news_analyzer, [fetch_news_task])
compiled_news_task = task.compile_newsletter_task(newsletter_compiler, [analyzed_news_task], save_markdown)

# setting up tools

crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyzed_news_task, compiled_news_task],
    process=Process.hierarchical,
    manager_llm=lama,
    verbose=2
)

results = crew.kickoff()

print("final result")
print(results)
