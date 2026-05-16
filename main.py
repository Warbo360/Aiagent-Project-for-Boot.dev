import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os


def main():
    print("Hello from aiagent!")

parser = argparse.ArgumentParser(description = "Chatbot")
parser.add_argument("user_prompt", type = str, help = "User prompt")
parser.add_argument("--verbose", action = "store_true", help = "Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text = args.user_prompt)])]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("API key not found")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages
)

if response.usage_metadata and args.verbose:
    print(
        f"\nUser prompt: {args.user_prompt}\n\n"
        f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
        f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
    )
    print(response.text)
elif response.usage_metadata:
    print(response.text)
else:
    raise RuntimeError("Failed API request, no metadata")


if __name__ == "__main__":
    main()
