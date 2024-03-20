from simulation import SIMULATION
import sys

# Command Line Arguments

directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()
