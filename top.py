from typing import List, Dict, Any
from router import Router
from agents import ReverseTextAgent, UppercaseAgent, LowercaseAgent, RemoveSpacesAgent, AddExclamationAgent, DuplicateAgent, ReplaceVowelsAgent, FirstWordAgent, LastWordAgent, AddPrefixAgent, AddSuffixAgent, ReplaceSpacesWithUnderscoresAgent, RemoveVowelsAgent, SortLettersAgent, SortWordsAgent, TitleCaseAgent, Repeat3xAgent, Duplicate2Agent, ReverseWordsAgent, AddQuotesAgent

class TOP:
    """Task-Oriented Protocol System."""
    
    def __init__(self):
        self.router = Router()
        self._register_default_agents()
    
    def _register_default_agents(self):
        """Register the default set of agents."""
        default_agents = [
            ReverseTextAgent(),
            UppercaseAgent(),
            LowercaseAgent(),
            RemoveSpacesAgent(),
            AddExclamationAgent(),
            DuplicateAgent(),
            ReplaceVowelsAgent(),
            FirstWordAgent(),
            LastWordAgent(),
            AddPrefixAgent(),
            AddSuffixAgent(),
            ReplaceSpacesWithUnderscoresAgent(),
            RemoveVowelsAgent(),
            SortLettersAgent(),
            SortWordsAgent(),
            TitleCaseAgent(),
            Repeat3xAgent(),
            Duplicate2Agent(),
            ReverseWordsAgent(),
            AddQuotesAgent(),
        ]
        for agent in default_agents:
            self.router.register_agent(agent)
    
    def get_agents(self) -> List[Dict[str, Any]]:
        """Get list of all available agents and their capabilities."""
        return self.router.discover_agents()
    
    def execute(self, agent_id: str, input_data: Any) -> Any:
        """Execute a task using the specified agent."""
        return self.router.execute(agent_id, input_data)
    
    def test_agent(self, agent_id: str, test_input: Any) -> Dict[str, Any]:
        """Test an agent's capability."""
        return self.router.test_agent(agent_id, test_input)

def main():
    # Create TOP instance
    top = TOP()
    
    # Discover available agents
    print("Discovering agents...", flush=True)
    agents = top.get_agents()
    print(f"Found {len(agents)} agents:", flush=True)
    for agent in agents:
        print(f"- {agent['id']}: {agent['description']}", flush=True)
    
    # Test ReverseTextAgent
    print("\nTesting ReverseTextAgent...", flush=True)
    test_input = "Hello, World!"
    result = top.execute("reverse_text", test_input)
    print(f"Input: {test_input}")
    print(f"Reversed: {result}", flush=True)

if __name__ == "__main__":
    main() 