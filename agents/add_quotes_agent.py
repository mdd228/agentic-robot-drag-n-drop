from .base_agent import Agent

class AddQuotesAgent(Agent):
    @property
    def id(self):
        return "add_quotes"

    @property
    def description(self):
        return "Adds double quotes around the input string."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return f'"{input_data}"'

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 