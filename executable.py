from ped_simulator import *

flux = 1

# Create simulation
sim = Simulation()

# Adding coordinated for corridors
sim.create_halls([((0, 12.5), (25, 12.5)), ((12.5, 25), (12.5, 0)) ])

# For creating pedestrians on the roads
sim.create_gen({ 'ped_rate': flux*120, 'peds': [[{"path": [0]}], [{"path": [1]}]]})

# Start simulation
vis = Visual(sim)
vis.offset = (-12, -12)
vis.run(steps_per_update=1)
