from .base_agent import Agent

class Repeat3xAgent(Agent):
    @property
    def id(self):
        return "repeat_3x"

    @property
    def description(self):
        return "Repeats the input string three times."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return input_data * 3

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 