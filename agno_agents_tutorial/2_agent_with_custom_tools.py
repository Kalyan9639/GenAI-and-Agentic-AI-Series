from agno.models import google
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import time

load_dotenv()

agent = Agent(
    name="Finance Agent",
    model = google.Gemini(id="gemini-2.5-flash-lite",temperature=0.7),
    tools=[YFinanceTools()],
    description="You are a finance agent that provides stock market information to users. You can fetch stock prices, analyst recommendations, and company information to help users make informed financial decisions.",
    instructions=["Use tables to display data when appropriate.","Provide concise and accurate information."],
    markdown=True,
    # debug_mode=True
)

start = time.time()
agent.print_response("what is the current stock price of NVIDIA")
print(f"Time taken: {time.time() - start:.2f} seconds")