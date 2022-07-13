# PL_PedSim
Phantasma Labs simChallenge: modelling of a pedestrian simulator

The task is explained the pdf file 'Phantasma Simulation Challenge.pdf'
The detailed description of the approach taken in explained the pdf file 'Report_Tripathi.pdf'
To run the simulation:
  1. clone the repository and do not change the structure.
  2. There are two files that can be used for running the simulation: 'RUN.ipynb' for jupyter notebook and 'executable.py' for python IDEs
  3. Open the notebook 'RUN.ipynb'
  4. Run the first cell in 'RUN.ipynb' if you want to store the output in a .txt file OR run the 4th cell if you want to change the parameters of the simulation
  5. If change in parameters is desired, change only the 'flux' value in cell 4, line 6.
  6. Run the notebook 'flux_plots.ipynb' if plots for number of pedestrians at each second are needed to be generated.

The simulation generates 3 output files: (a) image file for last time step (Last_time_step.png)
                                         (b) text file for number of pedestrians at each time step (num_peds.txt)
                                         (c) text file for corrdinates of each pedestrian at each time step (peds_loc.txt)
                           
Image file output can be enabled/disabled by commenting out the line 55 in file 'visual.py'

Text file for number of pedestrians at each time step can be enabled/disables by commenting out the line 41 in file 'ped_generator.py'

Text file for corrdinates of each pedestrian at each time step can be enabled/disabled by commenting out the line 91 in file 'visual.py'


The simulation is based on the tutorial provided by Bilal Himite: Simulating Traffic Flow in Python, URL: https://towardsdatascience.com/simulating-traffic-flow-in-python-ee1eab4dd20f
