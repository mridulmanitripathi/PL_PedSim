import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import gfxdraw
import numpy as np
import time

class Visual:
    
    def __init__(self, sim, config={}):
        self.sim = sim
        self.set_default_config()
        for attr, val in config.items():
            setattr(self, attr, val)
        
    def set_default_config(self):
        # Setting the screen for visualization
        self.width = 700
        self.height = 700
        self.bg_color = (250, 250, 250)
        self.fps = 60
        self.zoom = 20
        self.offset = (0, 0)

        
    def loop(self, loop=None):
        
        # Create a pygame window
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.flip()

        # Time for screen
        clock = pygame.time.Clock()
        # Time for simulation duration
        timer = pygame.time.get_ticks()

        # Draw loop
        running = True
        while running and timer <=60000: # 60000 = 60 seconds as the timer has resolution of 1ms
            timer = pygame.time.get_ticks()
            # Updating the simulation
            if loop: loop(self.sim)
            # Drawing the corridors and pedestrians
            self.draw(timer)
            # Updating the display window
            pygame.display.update()
            clock.tick(self.fps)
            
            # Exit the program if pygame window is closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False            
        
        # Save the positions of pedestrians at the last time step
        #pygame.image.save(self.screen,"Last_time_step.jpg")
        pygame. quit()
        

    # Function for updating the simulation
    def run(self, steps_per_update=1):  
        def loop(sim):
            sim.run(steps_per_update)
        self.loop(loop)
        

    # Function for convertign simulation coordinates to screen coordinates
    def convert(self, x, y=None):    
        if isinstance(x, list):
            return [self.convert(e[0], e[1]) for e in x]
        if isinstance(x, tuple):
            return self.convert(*x)
        return (int(self.width/2 + (x + self.offset[0])*self.zoom), int(self.height/2 + (y + self.offset[1])*self.zoom))


    # Function for colouring the background of the screen
    def background(self, r, g, b):
        self.screen.fill((r, g, b))


    # Function for drawing a circle
    def circle(self, pos, radius, color, timer, cos=None, sin=None, filled=True):
        x, y = pos
        r = radius
        l=2*r
        h=2*r        
        vertex = lambda e1, e2: (x + (e1*l*cos + e2*h*sin)/2, y + (e1*l*sin - e2*h*cos)/2)
        vertices = self.convert([vertex(*e) for e in [(-1,-1), (-1, 1), (1,1), (1,-1)]])
        temp_x = max(vertices[0][0], vertices[2][0]) - np.abs((vertices[0][0] - vertices[2][0]))/2
        temp_y = max(vertices[0][1], vertices[2][1]) - np.abs((vertices[0][1] - vertices[2][1]))/2
        temp_r = np.abs((vertices[0][1] - vertices[2][1]))/2
        #print(timer//1000,',',temp_x,',', temp_y)
        pygame.draw.rect(self.screen, color, (temp_x,temp_y, 2*temp_r, 2*temp_r), border_radius = int(temp_r))
 

    # Function for drawing a rectangle
    def rectangle(self, pos, size, cos=None, sin=None, color=(0, 0, 255), filled=True):
        x, y = pos
        l, h = size        
        vertex = lambda e1, e2: (x + (e1*l*cos + e2*h*sin)/2, y + (e1*l*sin - e2*h*cos)/2)
        vertices = self.convert([vertex(*e) for e in [(0,-1), (0, 1), (2,1), (2,-1)]])
        gfxdraw.filled_polygon(self.screen, vertices, color)
        
    
    # Function for drawing all corridors 
    def draw_halls(self):
        for hall in self.sim.halls:
            self.rectangle(hall.start, (hall.length, 5), cos=hall.angle_cos, sin=hall.angle_sin, color=(218,218, 250))
            

    # Function for drawing a circular pedestrian
    def draw_ped(self, ped, hall, timer):
        r = ped.r
        sin, cos = hall.angle_sin, hall.angle_cos
        x = hall.start[0] + cos * ped.x 
        y = hall.start[1] + sin * ped.x   
        self.circle((x, y), r, cos=cos, sin=sin, color=(255,0,0), timer = timer)


    # Function for drawing multiple circular pedestrians
    def draw_peds(self, timer):
        for hall in self.sim.halls:
            for ped in hall.peds:
                self.draw_ped(ped, hall, timer)
               

    # Function for printing the time and the pedestrian counter on the screen
    def draw_status(self):
        pygame.font.init()
        self.text_font = pygame.font.SysFont('Arial', 22)
        text_time = self.text_font.render(f'Time elapsed = {self.sim.t:.3} seconds', False, (0, 0, 0))
        text_counter = self.text_font.render(f'Number of pedestrians generated ={self.sim.counter}', False, (0, 0, 0))
        self.screen.blit(text_time, (0, 0))
        self.screen.blit(text_counter, (0, 650))


    # Function for drawing on the screen
    def draw(self, timer):
        # Fill background
        self.background(*self.bg_color)
        self.draw_halls()
        self.draw_peds(timer)
        # Draw status info
        self.draw_status()
        
