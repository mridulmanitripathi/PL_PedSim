from .ped import Ped
from numpy.random import randint
import random

class PedGenerator:
    def __init__(self, sim, config={}):
        self.sim = sim
        self.set_default_config()
        for attr, val in config.items():
            setattr(self, attr, val)

        # For generating new pedestrians
        self.init_properties()
        
    
    def set_default_config(self):
        self.ped_rate = 12        # Flux of the pedestrians in each corridor (Units= per minute)
        self.peds = [({})]        # Configuration of the pedestrians: corridor number
        self.last_added_time = 0  # For recording time of last generated pedestrian

    def init_properties(self):
        self.upcoming_ped = self.generate_ped()  # For generating new pedestrians
        
    def generate_ped(self):
        # For generating new pedestrians alternatively for each corridor
        num = self.sim.counter%2
        return Ped(self.peds[num][0])

    # Function for adding pedestrians
    def update(self):
        # Add pedestrians if time elapsed is more than the desired for a given flux
        if self.sim.t - self.last_added_time >= 60 / self.ped_rate:
            hall = self.sim.halls[self.upcoming_ped.path[0]]  
            # Adding new pedestrians if there is a space in the corridor
            if len(hall.peds) == 0 or hall.peds[-1].x > self.upcoming_ped.s0 + self.upcoming_ped.l:
                self.upcoming_ped.time_added = self.sim.t
                hall.peds.append(self.upcoming_ped)
                # Reset time for latest added pedestrian and counting the number of pedestrians generated
                self.last_added_time = self.sim.t
                self.sim.counter+=1
                print(self.sim.t,',', self.sim.counter)
            # Adding the new pedestrian
            self.upcoming_ped = self.generate_ped()
            
