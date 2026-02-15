from agno.agent import Agent
from agno.models.google import Gemini
from agno.media import Image
from dotenv import load_dotenv
from pathlib import Path
import os
import json

load_dotenv()

def generate_image_id(image_type):
    """
    Generate a numeric identifier for different image types.
    This function maps image type categories to their corresponding numeric IDs,
    useful for categorizing and processing images in multimodal agent workflows.
    Args:
        image_type (str): The type of image. Supported values are:
            - "original": Original unmodified images
            - "anime": Anime or stylized images
            - "screenshot": Screenshots or screen captures
    Returns:
        int: A numeric identifier for the image type
    """
    
    if image_type == "original":
        return 1
    if image_type == "anime":
        return 2
    if image_type == "screenshot":
        return 3
    return None

agent = Agent(
    name="Categorization Agent",
    # model=Gemini(id="gemini-2.5-flash-lite", temperature=0.7),

    # Gemini 3.0 flash preview has better image understanding capabilities, but is more expensive. 
    # You can switch to it if you have access and want better performance.

    model=Gemini(id="gemini-3-flash-preview", temperature=0.7), 
    tools=[generate_image_id],
)

response = agent.run(
    input=""" For each image, generate a json record that should look like this:
        {
            'image_id': 91289,
            'image_type': 'anime',
            'image_description': 'this image is about...'
        }
    
        image type should be one of the following: ['original','anime','screenshot']
        image description should be a 2 line description of the content of the image. it should not include any information about the style of the image. it should only describe what is in the image.
        output must be a json string without any preamble like json etc.
        it should be such that python can parse it easily.
    """,
    images=[
        Image(filepath=os.path.join(Path(__file__).parent, "images", "image_1.png")),
        Image(filepath=os.path.join(Path(__file__).parent, "images", "image_2.jpeg")),
        Image(filepath=os.path.join(Path(__file__).parent, "images", "image_3.jpg"))
        ]
)


# response_json = json.load(response.content)
# print(response_json)

response_json = response.content

print(response_json)

try:
    json_response = json.loads(response_json)
    with open("json_categorized_images.json", "w") as f:
        json.dump(json_response, f, indent=4)
except json.JSONDecodeError as e:
    print("Failed to parse JSON response:", e)

    
with open("categorized_images.json", "w") as f:
    json.dump(response_json, f, indent=4)