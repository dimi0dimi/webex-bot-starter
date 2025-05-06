import argparse

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--user_message', required=True)
  args = parser.parse_args()

  # TO DO:
  # Add a system prompt of your choice or follow the proctor's instructions.

  client = OpenAI()

  response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": args.user_message}
    ]
  )

  print(response.choices[0].message.content)


main()
