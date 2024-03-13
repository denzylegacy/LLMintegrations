# -*- coding: utf-8 -*-
"""
Gemini API: https://ai.google.dev/tutorials/python_quickstart
Get an Google API Key: https://aistudio.google.com/app/apikey

Create a .env file in the root directory of the project with the following content: GOOGLE_API_KEY="YOUR_API_KEY"
run: python install -r requirements.txt
"""

import google.generativeai as genai
import os
from dotenv import load_dotenv
from local_io import JSONHandler


options = JSONHandler.read_options_json(r"./options.json")  # Google/options.json
load_dotenv()

class GeminiApiConnector:
    """Google Gemini API Implementation"""

    @staticmethod
    def gemini_models() -> None:
        print("Available models:")
        for m in genai.list_models():
            if "generateContent" in m.supported_generation_methods:
                print(m.name)
        return

    def __init__(self, model: str):
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        self.model = model

    def gemini_chat(self, prompt: str) -> str:
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        return response.text


if __name__ == "__main__":
    gemini_api_connector = GeminiApiConnector(options["models"][0])
    # gemini_api_connector.gemini_models() 
    print(gemini_api_connector.gemini_chat(prompt="Olá!"))
