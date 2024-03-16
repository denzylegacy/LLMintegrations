# -*- coding: utf-8 -*-
"""
Mistral API: https://docs.mistral.ai
Get an Mistral API Key: https://console.mistral.ai/api-keys/

Create a .env file in the root directory of the project with the following content: MISTRAL_API_KEY="YOUR_API_KEY"
run: python install -r requirements.txt
"""

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
from local_io import JSONHandler
import os


options = JSONHandler.read_options_json(r"Mistral/options.json")  # Mistral/options.json
load_dotenv()

class MistralApiConnector:
    """Mistral API Implementation"""

    def __init__(self, model: str):
        self.client = MistralClient(api_key=os.environ.get("MISTRAL_API_KEY"))
        self.model = model

    def mistral_chat(self, prompt: str) -> str:
        messages = [
            ChatMessage(role="user", content=prompt)
        ]
        response = self.client.chat(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    mistral_api_connector = MistralApiConnector(options["models"][2])
    print(mistral_api_connector.mistral_chat("What is the best French cheese?"))
