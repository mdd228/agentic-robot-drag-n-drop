from .base_agent import Agent

class ReverseWordsAgent(Agent):
    @property
    def id(self):
        return "reverse_words"

    @property
    def description(self):
        return "Reverses the order of words in the input string."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        words = input_data.strip().split()
        return ' '.join(reversed(words))

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 