from services.ollama_client import OllamaClient
from utils.prompt_templates import BEHAVIORAL_PROMPT

class BehavioralAgent:
    def __init__(self, model="llama3"):
        self.llm = OllamaClient(model)

    def generate(self):
        return self.llm.ask(BEHAVIORAL_PROMPT)
