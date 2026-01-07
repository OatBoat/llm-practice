from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def translate_to_french(text):
  llm = OpenAI()
  response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=1,
    input=f"put a positve twist on anything the user inputs: {text}"
  )

  return response.output_text

user_input = input("Let me make you day: \n")

print(translate_to_french(user_input))