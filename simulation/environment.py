from simulation.agents import Agent

from typing import List, Tuple
import random
import numpy as np

class Building:
    def __init__(self, name: str, location: Tuple[float, float], building_type: str = None):
        """
        Initialize a building.

        Parameters:
            name (str): The name of the building.
            location (Tuple[float, float]): The location of the building as a (x, y) tuple.
        """
        self.building_type = building_type # Ejemplo: 'home', 'workplace', 'school', 'public'
        self.name = name
        self.location = location

class Environment:
    def __init__(self, x_limit: int, y_limit: int, num_agents: int):
        """
        Initialize the environment.

        Parameters:
            x_limit (int): The x-coordinate limit of the environment.
            y_limit (int): The y-coordinate limit of the environment.
            num_agents (int): The number of agents to initialize in the environment.
        """
        self.x_limit: int = x_limit
        self.y_limit: int = y_limit
        #creating a numpy map of size x_limit, y_limit
        self.map = np.zeros((x_limit,y_limit))
        self.agents: List[Agent] = []
        self.buildings: List[Building] = []
        self.initialize_agents(num_agents)
        self.initialize_spaces()

    def initialize_agents(self, num_agents: int):
        """
        Initialize agents within the environment.

        Parameters:
            num_agents (int): The number of agents to initialize.
        """
        infected_agents = random.randint(0, num_agents/2)
        
        
        for i in range(num_agents):
            agent = Agent(unique_id=i)
            x = random.randint(0, self.x_limit)
            y = random.randint(0, self.y_limit)
            self.add_agent(agent, x, y)

    def add_agent(self, agent: Agent, x: float, y: float):
        """
        Add an agent to the environment at a specified location.

        Parameters:
            agent (Agent): The agent to add.
            x (float): The x-coordinate of the agent's location.
            y (float): The y-coordinate of the agent's location.
        """
        agent.location = (x, y)
        self.agents.append(agent)

    def add_building(self, building: Building):
        """
        Add a building to the environment.

        Parameters:
            building (Building): The building to add.
        """
        self.buildings.append(building)

    def initialize_spaces(self):
        """
        Add spaces to the environment.
        """
        self.add_building(Building("Home", (100, 100), "home"))
        self.add_building(Building("Workplace", (200, 200), "workplace"))
        self.add_building(Building("School", (300, 300), "school"))
        self.add_building(Building("Park", (400, 400), "public"))
        self.add_building(Building("Hospital", (500, 500), "hospital"))

    def move_agent(self, agent: Agent, dir_x: float, dir_y: float):
        """
        Move an agent to a new location.

        Parameters:
            agent (Agent): The agent to move.
            new_x (float): The new x-coordinate of the agent's location.
            new_y (float): The new y-coordinate of the agent's location.
        """
        prev_location = agent.location
        agent.location = (dir_x + prev_location[0], dir_y + prev_location[1])

    def get_neighbors(self, agent: Agent, radius: float = 1.0) -> List[Agent]:
        """
        Get neighboring agents within a certain radius of a given agent.

        Parameters:
            agent (Agent): The agent to find neighbors for.
            radius (float): The radius within which to search for neighbors. Default is 1.0.

        Returns:
            List[Agent]: A list of neighboring agents.
        """
        neighbors = []
        for other_agent in self.agents:
            if agent != other_agent:
                distance = self.calculate_distance(agent.location, other_agent.location)
                if distance <= radius:
                    neighbors.append(other_agent)
        return neighbors

    def calculate_distance(self, pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float:
        """
        Calculate the Euclidean distance between two positions.

        Parameters:
            pos1 (Tuple[float, float]): The first position as a (x, y) tuple.
            pos2 (Tuple[float, float]): The second position as a (x, y) tuple.

        Returns:
            float: The Euclidean distance between the two positions.
        """
        x1, y1 = pos1
        x2, y2 = pos2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def step(self):
        """
        Perform a simulation step, where agents take actions.
        """
        for agent in self.agents:
            # Implement agent actions for each step
            action, parameters = agent.act()
            if action ==  "move":
                self.move_agent(agent,*parameters)
            pass


if __name__ == '__main__':
    # Example usage
    env = Environment(x_limit=100.0, y_limit=100.0, num_agents=10)
    building1 = Building("Workplace", (50.0, 50.0))
    building2 = Building("Park", (30.0, 70.0))
    env.add_building(building1)
    env.add_building(building2)
