
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

try:
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash')

    with open('prompts/topic.txt', 'r') as f:
        prompt = f.read()

    response = model.generate_content(prompt)
    topics = response.text.strip().split('\n')
    cleaned_topics = [topic.split('. ', 1)[-1] for topic in topics]
    with open('topics.json', 'w') as f:
        json.dump(cleaned_topics, f, indent=4)
    print("Topics generated and saved to topics.json")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please make sure you have set up your API key in the .env file.")
