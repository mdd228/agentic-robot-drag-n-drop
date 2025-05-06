from .base_agent import Agent

class SortWordsAgent(Agent):
    @property
    def id(self):
        return "sort_words"

    @property
    def description(self):
        return "Sorts words in the input string alphabetically."

    def execute(self, input_data):
        if not isinstance(input_data, str):
            return "Input must be a string."
        words = input_data.strip().split()
        return ' '.join(sorted(words))

    def test_capability(self, test_input):
        return {
            "input": test_input,
            "output": self.execute(test_input)
        } 