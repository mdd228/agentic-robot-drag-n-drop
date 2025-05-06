import logging
from typing import Dict, List, Any
from agents import Agent

class Router:
    """Manages agent discovery and execution."""
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.logger = logging.getLogger(__name__)
    
    def discover_agents(self) -> List[Dict[str, Any]]:
        """
        Discover all available agents and their capabilities.
        Returns a list of agent capability descriptions.
        """
        agent_capabilities = []
        for agent in self.agents.values():
            try:
                capabilities = agent.capabilities
                agent_capabilities.append(capabilities)
            except Exception as e:
                self.logger.error(f"Error getting capabilities for agent {agent}: {e}")
        return agent_capabilities
    
    def register_agent(self, agent: Agent) -> None:
        """Register a new agent with the router."""
        self.agents[agent.id] = agent
        self.logger.info(f"Registered agent: {agent.id}")
    
    def get_agent(self, agent_id: str) -> Agent:
        """Get an agent by its ID."""
        if agent_id not in self.agents:
            raise ValueError(f"Unknown agent: {agent_id}")
        return self.agents[agent_id]
    
    def execute(self, agent_id: str, input_data: Any) -> Any:
        """Execute a task using the specified agent."""
        agent = self.get_agent(agent_id)
        try:
            result = agent.execute(input_data)
            self.logger.info(f"Successfully executed {agent_id} with result: {result}")
            return result
        except Exception as e:
            self.logger.error(f"Error executing {agent_id}: {e}")
            raise
    
    def test_agent(self, agent_id: str, test_input: Any) -> Dict[str, Any]:
        """Test an agent's capability with the given input."""
        agent = self.get_agent(agent_id)
        try:
            result = agent.test_capability(test_input)
            self.logger.info(f"Successfully tested {agent_id}")
            return result
        except Exception as e:
            self.logger.error(f"Error testing {agent_id}: {e}")
            raise 