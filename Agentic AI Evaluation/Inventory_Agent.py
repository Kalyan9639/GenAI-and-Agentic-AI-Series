from agno.agent import Agent
from agno.models.google import Gemini
import re

def inventory_tool(product_name):
    """A helpful function to fetch inventory data for a given product name.
    """
    inventory={
        "iPhone 14 pro max": "stock_status : In Stock available_items : 25",
        "samsung galaxy s23 ultra": "stock_status: Out of Stock available_items : 0",
        "google pixel 7 pro": "stock_status : In Stock available_items : 10"
    }
    return inventory.get(product_name, "Product not found in the inventory.")

def search_products(query):
    """
    A Helpful function to search for products in the inventory based on the user's query.
    """
    if re.findall(r'\b(?:iPhone|samsung|google)\b', query, re.IGNORECASE):
        if (re.search(r'iPhone', query, re.IGNORECASE) or re.search(r'apple', query, re.IGNORECASE)):
            return "iPhone 14 pro max"
        elif re.search(r'samsung', query, re.IGNORECASE):
            return "samsung galaxy s23 ultra"
        elif (re.search(r'google', query, re.IGNORECASE) or re.search(r'pixel', query, re.IGNORECASE)):
            return "google pixel 7 pro"

agent = Agent(
    name="Inventory Agent",
    model=Gemini("gemini-2.5-flash-lite",api_key="AIzaSyDYJvYGFI8J2kizYDSkfVUhJdLsgldHTOo"),
    tools=[inventory_tool,search_products],
    instructions = ["""
You are an inventory assistant.

- If a question is out of scope (not related to inventory), just say: "Sorry, I can’t help with that."
- When a user asks about a product, use the inventory_tool to fetch the inventory data.
- Always call the inventory_tool with the full product name.
- inventory_tool will return a dictionary which you need to parse to extract stock status.
- Respond with clear, concise information including:
  1. The stock status (e.g., "In Stock", "Out of Stock")
  2. The number of available items (if applicable)
- If the product is not found, say: "The product is not available in our inventory."
- Never guess or hallucinate information. Do not respond unless the inventory_tool is called.
- Keep your response short and informative.
"""],
    markdown=True
)

agent.print_response("I want to buy a google phone. is it available and which phone is avail?")