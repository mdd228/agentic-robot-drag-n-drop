from .base_agent import Agent
import re

class ReplaceVowelsAgent(Agent):
    @property
    def id(self):
        return "replace_vowels"

    @property
    def description(self):
        return "Replaces all vowels in the input string with '*'."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return re.sub(r'[aeiouAEIOU]', '*', input_data)

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 