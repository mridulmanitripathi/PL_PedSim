from .hall import Hall
from copy import deepcopy
from .ped_generator import PedGenerator

class Simulation:
    def __init__(self, config={}):
        self.set_default_config()
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0            # For recording the time elapsed during the simulation
        self.dt = 1/60          # Time step for simulation
        self.halls = []         # List for storing the corridors
        self.generators = []    # For adding pedestrians
        self.counter = 0        # For counting the number of pedestrians generated

    # Function for adding corridors into the list
    def create_hall(self, start, end):
        hall = Hall(start, end)
        self.halls.append(hall)
        return hall

    # Function for creating corridors based on the input data
    def create_halls(self, hall_list):
        for hall in hall_list:
            self.create_hall(*hall)

    # Function for creating pedestrians
    def create_gen(self, config={}):
        gen = PedGenerator(self, config)
        self.generators.append(gen)
        return gen


    # Function for updating all parameters
    def update(self):
        # Updating every corridors
        for hall in self.halls:
            hall.update(self.dt)

        # Updating and adding pedestrians
        for gen in self.generators:
            gen.update()

        # Checking pedestrians that crossed the corridor's limits
        for hall in self.halls:
            if len(hall.peds) == 0: continue
            ped = hall.peds[0]
            # Removing pedestrians that crossed the corridor's limits
            if ped.x >= hall.length:
                hall.peds.popleft() 
        # Time increment
        self.t += self.dt


    # Function for updating parameters for all time steps
    def run(self, steps):
        for _ in range(steps):
            self.update()
