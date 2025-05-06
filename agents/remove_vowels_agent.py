from .base_agent import Agent
import re

class RemoveVowelsAgent(Agent):
    @property
    def id(self):
        return "remove_vowels"

    @property
    def description(self):
        return "Removes all vowels from the input string."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return re.sub(r'[aeiouAEIOU]', '', input_data)

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 