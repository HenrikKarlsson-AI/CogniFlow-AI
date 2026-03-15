"""
Decision Agent
Evaluates alerts from other agents and determines the operational response.
"""

from typing import Dict, Any

class DecisionAgent:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id

    def observe(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Checks the context for recent alerts or system status."""
        return {"current_status": context.get("system_status", "UNKNOWN")}

    def decide_and_act(self, observations: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Determines the operational response based on system status."""
        status = observations.get(self.agent_id, {}).get("current_status", "UNKNOWN")
        
        if status == "CRITICAL":
            return "ACTION: Initiating Emergency Shutdown Protocol"
        elif status == "WARNING":
            return "ACTION: Adjusting parameters to safe mode"
        
        return "ACTION: Continuing standard operations"
