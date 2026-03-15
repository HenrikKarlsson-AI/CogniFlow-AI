"""
Smart Factory Simulation
Demonstrates the CogniFlow-AI framework orchestrating sensor and decision agents.
"""

from core.orchestrator import CogniFlowOrchestrator
from agents.sensor_agent import SensorAgent
from agents.decision_agent import DecisionAgent

def run_simulation():
    print("--- CogniFlow-AI: Smart Factory Orchestration Simulation ---\n")

    # 1. Initialize Orchestrator
    orchestrator = CogniFlowOrchestrator("factory_alpha")

    # 2. Initialize and Register Agents
    temp_agent = SensorAgent(agent_id="temp_monitor", threshold=85.0)
    pressure_agent = SensorAgent(agent_id="pressure_monitor", threshold=120.0)
    decision_agent = DecisionAgent(agent_id="commander")

    orchestrator.register_agent("temp_monitor", temp_agent)
    orchestrator.register_agent("pressure_monitor", pressure_agent)
    orchestrator.register_agent("commander", decision_agent)

    # 3. Simulate Environment Context (Cycle 1: Normal)
    print("\n[CYCLE 1: Normal Operations]")
    context_cycle_1 = {
        "sensor_readings": {"temperature": 70.0, "pressure": 100.0},
        "system_status": "NORMAL"
    }
    orchestrator.run_cycle(context_cycle_1)

    # 4. Simulate Environment Context (Cycle 2: Critical Overheating)
    print("\n[CYCLE 2: Critical Overheating Event]")
    context_cycle_2 = {
        "sensor_readings": {"temperature": 95.0, "pressure": 105.0},
        "system_status": "CRITICAL"
    }
    orchestrator.run_cycle(context_cycle_2)

    print("\n--- Simulation Complete ---")

if __name__ == "__main__":
    run_simulation()
