# -*- coding: utf-8 -*-
"""
MariTalk API: https://github.com/maritaca-ai/maritalk-api
Get an MariTalk API Key: https://chat.maritaca.ai

Create a .env file in the root directory of the project with the following content: MARITALK_API_KEY="YOUR_API_KEY"
run: python install -r requirements.txt
"""

import maritalk
import os
from dotenv import load_dotenv
from local_io import JSONHandler


options = JSONHandler.read_options_json(r"./options.json")  # MariTalk/options.json
load_dotenv()

class MariTalkApiConnector:
    """MariTalk API Implementation"""

    def __init__(self, model: str):
        self.model = maritalk.MariTalk(
           key=os.environ.get("MARITALK_API_KEY"),
            model=model
        )

    def maritalk_chat(self, prompt: str) -> str:
        response = self.model.generate(prompt)
        answer = response["answer"]
        return answer


if __name__ == "__main__":
    maritalk_api_connector = MariTalkApiConnector(options["models"][0])
    # maritalk_api_connector.MariTalk_models() 
    print(maritalk_api_connector.maritalk_chat(prompt="Quanto é 25 + 27?"))
