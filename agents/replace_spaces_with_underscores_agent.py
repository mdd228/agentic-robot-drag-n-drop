from .base_agent import Agent

class ReplaceSpacesWithUnderscoresAgent(Agent):
    @property
    def id(self):
        return "replace_spaces_with_underscores"

    @property
    def description(self):
        return "Replaces all spaces with underscores in the input string."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        return input_data.replace(' ', '_')

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 