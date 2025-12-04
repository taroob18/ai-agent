from services.ollama_client import OllamaClient
from utils.prompt_templates import SCENARIO_PROMPT

class ScenarioAgent:
    def __init__(self, model="llama3"):
        self.llm = OllamaClient(model)

    def generate(self, role):
        prompt = SCENARIO_PROMPT.format(role=role)
        return self.llm.ask(prompt)
