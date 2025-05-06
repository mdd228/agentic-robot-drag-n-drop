from .base_agent import Agent

class LowercaseAgent(Agent):
    @property
    def id(self):
        return "lowercase"

    @property
    def description(self):
        return "Converts the input string to lowercase."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return input_data.lower()

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 