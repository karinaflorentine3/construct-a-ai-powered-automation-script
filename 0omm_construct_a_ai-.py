import random
from abc import ABC, abstractmethod

# Data Model: AI Simulator
class AISimulator:
    def __init__(self, name, automation_script):
        self.name = name
        self.automation_script = automation_script
        self.state = "Idle"
        self.output = ""

    def run_simulation(self):
        self.state = "Running"
        self.execute_script()
        self.state = "Finished"

    def execute_script(self):
        for command in self.automation_script:
            if command.get("type") == "print":
                self.output += command.get("message") + "\n"
            elif command.get("type") == "delay":
                self.delay(command.get("duration"))
            elif command.get("type") == "conditional":
                if self.evaluate_condition(command.get("condition")):
                    self.execute_script_fragment(command.get("true_script"))
                else:
                    self.execute_script_fragment(command.get("false_script"))

    def delay(self, duration):
        print(f"Delaying for {duration} seconds...")
        # Simulate delay
        import time
        time.sleep(duration)

    def evaluate_condition(self, condition):
        # Simulate condition evaluation
        return random.choice([True, False])

    def execute_script_fragment(self, script_fragment):
        for command in script_fragment:
            if command.get("type") == "print":
                self.output += command.get("message") + "\n"
            elif command.get("type") == "delay":
                self.delay(command.get("duration"))

# Example Usage:
automation_script = [
    {"type": "print", "message": "Starting simulation..."},
    {"type": "delay", "duration": 2},
    {"type": "conditional", 
     "condition": "x > 5", 
     "true_script": [
         {"type": "print", "message": "Condition is true!"},
     ], 
     "false_script": [
         {"type": "print", "message": "Condition is false!"},
     ]},
    {"type": "print", "message": "Simulation finished."},
]

simulator = AISimulator("My AI Simulator", automation_script)
simulator.run_simulation()
print(simulator.output)