from .base_agent import Agent

class FirstWordAgent(Agent):
    @property
    def id(self):
        return "first_word"

    @property
    def description(self):
        return "Returns the first word of the input string."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        words = input_data.strip().split()
        return words[0] if words else ''

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 