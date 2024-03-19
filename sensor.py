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
        # print("testing \n")
        # print("1-2-3..... \n")
        # print(pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName))
