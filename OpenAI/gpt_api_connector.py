# -*- coding: utf-8 -*-
"""
OpenAI API: https://openai.com/blog/openai-api
Get an OpenAI API Key: https://platform.openai.com/api-keys

Create a .env file in the root directory of the project with the following content: OPENAI_API_KEY="YOUR_API_KEY"
run: python -m  pip install -r requirements.txt
"""
from typing import Union
from openai import OpenAI
import tiktoken
import os
from dotenv import load_dotenv
from local_io import JSONHandler


options = JSONHandler.read_options_json(r"./options.json")  # OpenAI/options.json
load_dotenv()

class OpenAiApiConnector:
    """OpenAi GPT API Implementation"""
    
    def __init__(
            self,
            model: str,
            personality: str = None,
            temperature: float = None,
            training_data: list = None
        ):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
        self.model = model
        self.temperature = temperature
        self.personality = personality
        self.training_data = training_data
        self.token_limit = 4097

    def gpt_chat(self, prompt: str) -> Union[str, None]:
        enc = tiktoken.get_encoding("cl100k_base")
        assert enc.decode(enc.encode("olá mundo")) == "olá mundo"  # hello world
        enc = tiktoken.encoding_for_model(self.model)  # "gpt-3.5-turbo"
        token_count = len(enc.encode(prompt))

        print("tokens:", token_count)

        if token_count > self.token_limit:
            # prompt = prompt[:4095]
            print(f"Hey... The prompt contains more tokens than the stipulated limit ({self.token_limit})!")
            return None

        messages = [
            {"role": "system", "content": self.personality},
            {"role": "user", "content": prompt},
        ]

        parameters = {
            "model": self.model, "messages": messages
        }

        if self.temperature:
            parameters["temperature"] = self.temperature

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
        )

        if completion:
            return completion.choices[0].message.content
        else:
            return None


if __name__ == "__main__":
    openai_api = OpenAiApiConnector(
        model=options["models"][4],
        personality="O seu nome é Dark, e você é uma pessoa muito deprimida!"
    )
    print(openai_api.gpt_chat("Oi! Qual é o teu nome? E que tipo de pessoa você é?"))
