from .base_agent import Agent

class AddSuffixAgent(Agent):
    @property
    def id(self):
        return "add_suffix"

    @property
    def description(self):
        return "Adds the suffix '-SUF' to the input string."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return input_data + '-SUF'

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 