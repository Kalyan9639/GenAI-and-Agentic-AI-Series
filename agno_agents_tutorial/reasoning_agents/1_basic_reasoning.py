from agno.agent import Agent
from agno.models import google
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=google.Gemini(id='gemini-2.5-flash-lite',temperature=0.7),
    reasoning=True  # To use this feature, you have to download openai module
)

agent.print_response("How much time it will take cheetah to travel from New Delhi to Mumbai?",stream=True)