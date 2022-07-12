from scipy.spatial import distance
from collections import deque

class Hall:
    def __init__(self, start, end):
        # Start and End of the corridors
        self.start = start
        self.end = end
        # Pedestrians are added in double ended queue
        self.peds = deque()
        self.init_properties()

    def init_properties(self):
        # Length of the corridor
        self.length = distance.euclidean(self.start, self.end)
        # Orientation of the corridor
        self.angle_sin = (self.end[1]-self.start[1]) / self.length
        self.angle_cos = (self.end[0]-self.start[0]) / self.length

    def update(self, dt):
        n = len(self.peds)
        if n > 0:
            # Updating the first pedestrian
            self.peds[0].update(None, dt)
            # Updating the other pedestrians
            for i in range(1, n):
                lead = self.peds[i-1]
                self.peds[i].update(lead, dt)
