from .base_agent import Agent

class TitleCaseAgent(Agent):
    @property
    def id(self):
        return "title_case"

    @property
    def description(self):
        return "Converts the input string to title case."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return input_data.title()

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 