"""
Sensor Agent
Monitors environmental data and identifies critical deviations.
"""

from typing import Dict, Any

class SensorAgent:
    def __init__(self, agent_id: str, threshold: float):
        self.agent_id = agent_id
        self.threshold = threshold

    def observe(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Reads sensor data from the shared context."""
        raw_data = context.get("sensor_readings", {})
        return {"raw": raw_data, "status": "read_complete"}

    def decide_and_act(self, observations: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Determines if an alert should be raised based on observations."""
        my_obs = observations.get(self.agent_id, {}).get("raw", {})
        
        for sensor, value in my_obs.items():
            if value > self.threshold:
                return f"ALERT: High value detected on {sensor} ({value} > {self.threshold})"
        
        return "STATUS: Normal"
