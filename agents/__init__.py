from abc import ABC, abstractmethod
from typing import Any, Dict, Type

class Agent(ABC):
    """Base class for all agents in the system."""
    
    @property
    @abstractmethod
    def id(self) -> str:
        """Unique identifier for the agent."""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Description of what the agent does."""
        pass
    
    @property
    def capabilities(self) -> Dict[str, Any]:
        """Standardized capability description for efficient discovery."""
        return {
            "id": self.id,
            "description": self.description,
            "input_format": self._get_input_format(),
            "output_format": self._get_output_format(),
            "test_cases": self._get_test_cases()
        }
    
    def _get_input_format(self) -> Dict[str, str]:
        """Describe the expected input format."""
        return {}
    
    def _get_output_format(self) -> Dict[str, str]:
        """Describe the output format."""
        return {}
    
    def _get_test_cases(self) -> list:
        """Provide standard test cases for capability verification."""
        return []
    
    @abstractmethod
    def test_capability(self, test_input: Any) -> Dict[str, Any]:
        """
        Test the agent's capability with a given input.
        Returns a dictionary with test results.
        """
        pass
    
    @abstractmethod
    def execute(self, input_data: Any) -> Any:
        """
        Execute the agent's main functionality.
        Returns the result of the operation.
        """
        pass

from .base_agent import Agent
from .reverse_text_agent import ReverseTextAgent
from .uppercase_agent import UppercaseAgent
from .lowercase_agent import LowercaseAgent
from .remove_spaces_agent import RemoveSpacesAgent
from .add_exclamation_agent import AddExclamationAgent
from .duplicate_agent import DuplicateAgent
from .replace_vowels_agent import ReplaceVowelsAgent
from .first_word_agent import FirstWordAgent
from .last_word_agent import LastWordAgent
from .add_prefix_agent import AddPrefixAgent
from .add_suffix_agent import AddSuffixAgent
from .replace_spaces_with_underscores_agent import ReplaceSpacesWithUnderscoresAgent
from .remove_vowels_agent import RemoveVowelsAgent
from .sort_letters_agent import SortLettersAgent
from .sort_words_agent import SortWordsAgent
from .title_case_agent import TitleCaseAgent
from .repeat_3x_agent import Repeat3xAgent
from .duplicate2_agent import Duplicate2Agent
from .reverse_words_agent import ReverseWordsAgent
from .add_quotes_agent import AddQuotesAgent

__all__ = [
    'Agent',
    'ReverseTextAgent',
    'UppercaseAgent',
    'LowercaseAgent',
    'RemoveSpacesAgent',
    'AddExclamationAgent',
    'DuplicateAgent',
    'ReplaceVowelsAgent',
    'FirstWordAgent',
    'LastWordAgent',
    'AddPrefixAgent',
    'AddSuffixAgent',
    'ReplaceSpacesWithUnderscoresAgent',
    'RemoveVowelsAgent',
    'SortLettersAgent',
    'SortWordsAgent',
    'TitleCaseAgent',
    'Repeat3xAgent',
    'Duplicate2Agent',
    'ReverseWordsAgent',
    'AddQuotesAgent',
] 