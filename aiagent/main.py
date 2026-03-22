import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("The api key is not available")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

client = genai.Client(api_key=api_key)

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
my_response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

if my_response.usage_metadata is not None: 
    if args.verbose:
         print(f'User prompt: {args.user_prompt}')
         print(f'Prompt tokens: {my_response.usage_metadata.prompt_token_count}')
         print(f'Response tokens: {my_response.usage_metadata.candidates_token_count}')
else:
    raise RuntimeError("No usage_metadata object in the response")

print(my_response.text)
