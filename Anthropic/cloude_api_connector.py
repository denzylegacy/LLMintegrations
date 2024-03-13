# -*- coding: utf-8 -*-
"""
Anthropic API: https://www.anthropic.com/api
Get an Anthropic API Key: https://console.anthropic.com/settings/keys

Create a .env file in the root directory of the project with the following content: ANTHROPIC_API_KEY="YOUR_API_KEY"
run: python -m  pip install -r requirements.txt
"""

import anthropic
from anthropic import HUMAN_PROMPT, AI_PROMPT
import os
from dotenv import load_dotenv
from local_io import JSONHandler


options = JSONHandler.read_options_json(r"./options.json")  # Anthropic/options.json
load_dotenv()

class CloudApiConnector:
    """Anthropic Cloude API Implementation"""
     
    def __init__(self, model: str) -> None:
        self.model = model
        self.api_key = os.environ.get("ANTHROPIC_API_KEY")

    def cloude_completions(self, prompt: str) -> str:
        response = anthropic.Anthropic(api_key=self.api_key).completions.create(
            model=self.model,
            max_tokens_to_sample=1024,
            prompt=f"{HUMAN_PROMPT}{prompt}{AI_PROMPT}",
        )
        print(response, "\n----------\n")
        return response.completion

    def cloude_messages(self, content: str) -> str:
        response = anthropic.Anthropic(api_key=self.api_key).messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[
                {"role": "user", "content": f"{content}"}
            ]
        )
        print(response, "\n")
        return response.content[0].text


if __name__ == "__main__":
    Cloud_api_connector = CloudApiConnector(options["models"][2])
    # print(Cloud_api_connector.cloude_completions("Era uma vez"))
    print(Cloud_api_connector.cloude_messages("Oi! Qual é o teu nome?"))
