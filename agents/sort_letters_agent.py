from .base_agent import Agent

class SortLettersAgent(Agent):
    @property
    def id(self):
        return "sort_letters"

    @property
    def description(self):
        return "Sorts all characters in the input string alphabetically."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return ''.join(sorted(input_data))

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 