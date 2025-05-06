from .base_agent import Agent

class DuplicateAgent(Agent):
    @property
    def id(self):
        return "duplicate"

    @property
    def description(self):
        return "Duplicates the input string."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return input_data + input_data

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 