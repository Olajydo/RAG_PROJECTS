from crewai import Crew, Process
from tasks import research_task, write_task
from agent import news_researcher, news_writer

#forming the tech focused crew with some enhanced configuration

crew = Crew(
    agent =[news_researcher,news_writer],
    tasks =[research_task,write_task],
    process=Process.sequential,
)


#starting execution process

result = crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)