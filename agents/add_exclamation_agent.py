from .base_agent import Agent

class AddExclamationAgent(Agent):
    @property
    def id(self):
        return "add_exclamation"

    @property
    def description(self):
        return "Adds an exclamation mark at the end of the input string."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return input_data + '!'

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 