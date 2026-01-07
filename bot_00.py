from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


llm = OpenAI()
# creates an instance of the OpenAI client class so we can communicate with OpenAI's API
# Similar to how we initialize a class in ruby with person = Person.new


response = llm.responses.create(
   model="gpt-4.1-mini",
   temperature=0,
   input="What is the Sherwin Williams Color of the year for 2025?"
)
# see OpenAI's docs for where we get the llm.responses.create - https://github.com/openai/openai-python


print(response.output_text)