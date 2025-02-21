import os
from dotenv import load_dotenv
from phi.agent import Agent
from groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


#web search agent
websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id='llama3-70b-8192'),
    tools = [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

#financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id='llama3-70b-8192'),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)


multi_ai_agent = Agent(
    team=[websearch_agent, finance_agent],
    model=Groq(id='llama3-70b-8192'),
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)



multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)