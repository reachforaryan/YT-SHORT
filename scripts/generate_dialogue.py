import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()
# Configure the Gemini API key
try:
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash')
except KeyError:
    print("API_KEY environment variable not set.")
    exit(1)


# Create a directory to store the dialogues
if not os.path.exists("dialogues"):
    os.makedirs("dialogues")

# Load the topics from the JSON file
with open("../json/topics.json", "r") as f:
    topics = json.load(f)



# Read the prompt template
with open("../prompts/diaogue.txt", "r") as f:
    prompt_template = f.read()

# Generate a dialogue for each topic
for topic in topics:
    prompt = prompt_template.format(topic=topic)
    response = model.generate_content(prompt)

    # Save the dialogue to a file
    with open(f"../dialogues/{topic}.txt", "w") as f:
        f.write(response.text)

    print(f"Generated dialogue for topic: {topic}")
