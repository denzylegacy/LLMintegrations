import openai
import tiktoken
import os
from dotenv import load_dotenv

load_dotenv()


class OpenAiConnector:

    def __init__(self, key: str, temperature: float = None, personality: str = None, sources: str = None,
                 training_data: list = None):
        self.gpt_key = key
        self.temperature = temperature
        self.personality = personality
        self.sources = sources
        self.training_data = training_data
        self.token_limit = 4097

    def run_gpt(self):
        openai.api_key = os.environ.get("GPT_KEY")

        enc = tiktoken.get_encoding("cl100k_base")
        assert enc.decode(enc.encode("olá mundo")) == "olá mundo"  # hello world
        enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
        token_count = len(enc.encode(self.sources))

        if token_count > self.token_limit:
            self.sources = self.sources[:4095]

        messages = [
            {"role": "system", "content": self.personality},
            {"role": "user", "content": self.sources},
        ]

        models = {
            "GPT4_KEY": "gpt-4",  # Able to do more complex tasks, and optimized for chat
            "GPT4_KEY_32k": "gpt-4-32k",  # Same capabilities as the base gpt-4 mode but with 4x the context length
            "GPT3_KEY": "gpt-3.5-turbo",  # Can perform any task the other models can do, with higher quality
            "GPT3_KEY_16k": "gpt-3.5-turbo-16k",  # 4 times the context than standard gpt-3.5-turbo
            "gpt-4-1106-preview": "gpt-4-1106-preview",
            "gpt-3.5-turbo-1106": "gpt-3.5-turbo-1106",
        }

        parameters = {
            "model": models[self.gpt_key], "messages": messages,  # "max_tokens": 16000
        }

        if self.temperature is not None:
            parameters["temperature"] = self.temperature

        response = openai.ChatCompletion.create(**parameters)

        if response:
            return response, token_count
        else:
            return None


if __name__ == "__main__":
    ...
