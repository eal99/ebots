import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
SIMULATION.Run(simulation)



#
# num_steps = 1000
# t = numpy.linspace(0, 2 * numpy.pi, num_steps)  # Create a time array

#

#
#
# # numpy.save('data/front_targetAngles.npy', front_targetAngles)
# # numpy.save('data/back_targetAngles.npy', back_targetAngles)
# # exit()
#

#

# print(backLegSensorValues)
# print('--------------------------- \n')
# print(frontLegSensorValues)
# subdirectory = 'data'
#
# if not os.path.exists(subdirectory):
#     os.makedirs(subdirectory)
# backLegFile = os.path.join(subdirectory, 'backLegSensorValues.npy')
# frontLegFile = os.path.join(subdirectory, 'frontLegSensorValues.npy')
#
# numpy.save(backLegFile, backLegSensorValues)
# numpy.save(frontLegFile, frontLegSensorValues)
