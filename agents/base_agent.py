from abc import ABC, abstractmethod
from typing import Any, Dict

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