from crewai import Agent, LLM
from tools import tool
from langchain.llms import Cohere
import os
from langchain.memory import ConversationBufferMemory


from dotenv import load_dotenv
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")


from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Initialize Cohere LLM
llm = LLM(
    model="cohere/command-r",  
    api_key=COHERE_API_KEY,  
    temperature=0.5,
    verbose=True
)


#creating a senior research agent

news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True),
    backstory= (
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

## creating writer agent with custom tools responsible in writing news blog

news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    backstory= (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)






