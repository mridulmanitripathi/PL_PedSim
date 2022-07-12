import numpy as np
import random


class Ped:
    def __init__(self, config={}):
        self.set_default_config()
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):    
        self.r = 0.25       # Radius of the pedestrian
        self.l = 2*self.r   # Length of the pedestrain (diameter)
        self.s0 = self.l    # Minimum distance between two pedestrians
        self.v_max = 1.3    # Maximum velocity of the pedestrian
        self.a_max = 2      # Maximum acceleration of the pedestrian

        self.path = []      # list for path of the pedestrian
        self.current_hall_index = 0

        self.x = 0          # Position of the pedestrian
        self.v = self.v_max #round(random.uniform(1.1,self.v_max),1)      # Velocity of the pedestrian
        self.a = 0          # Acceleration of the pedestrian

    def update(self, lead, dt):
        # Updating position and velocity of the pedestrian
        self.v += self.a*dt
        self.x += self.v*dt + self.a*dt*dt/2
        
        # Updating acceleration of the pedestrian
        self.a = self.a_max #round(random.uniform(0,self.a_max),1)
