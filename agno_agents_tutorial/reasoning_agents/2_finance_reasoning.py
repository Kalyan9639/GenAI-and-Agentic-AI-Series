from agno.models import google
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv
import time

load_dotenv()

agent = Agent(
    name="Reasoning Agent",
    # model = google.Gemini(id="gemini-2.5-flash"),
    model = google.Gemini(id="gemini-3-flash-preview"),
    tools=[
        YFinanceTools(), 
        ReasoningTools(add_instructions=True)
           ],
    instructions=["Use tables to display data when appropriate.",
                ],
    markdown=True,
    # debug_mode=True
)


agent.print_response("Write a report on NVIDIA", show_full_reasoning=True)
