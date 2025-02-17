import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

def summarize_with_llm(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize the following text in 3-5 sentences: {text}")
    return response.text  


text = "Machine learning is a method of data analysis that automates analytical model building..."
summary = summarize_with_llm(text)
print(summary)
