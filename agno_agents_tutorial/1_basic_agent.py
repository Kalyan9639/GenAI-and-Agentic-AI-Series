from agno.agent import Agent
from agno.models import google
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('GOOGLE_API_KEY')
if key:
    os.environ['GOOGLE_API_KEY'] = key
else:
    print("WARNING: GOOGLE_API_KEY not found in environment. Set it in your .env or system environment before running.")

agent = Agent(
    name="Basic Gemini Agent",
    model = google.Gemini(id="gemini-2.5-flash-lite"),
    tools=[DuckDuckGoTools()],
    description="You are a news agent that provides the latest news updates to users. You can search for news articles, summarize them, and provide insights on current events.",
    markdown=True
)

agent.print_response("Tell me the most latest ai news from india along with the web urls of the news articles.")