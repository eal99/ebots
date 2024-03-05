import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random
import constants as c


class SENSOR:
    def __init__(self, linkName):

        self.linkName = linkName
        self.values = numpy.zeros(1000)

    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        print(self.values[-1])
