import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.motors = {}
        self.sensors = {}
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Prepare_To_Act(self):

        i = 0
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            print(jointName)
            i += 1

    def Act(self, i):
        for motor in self.motors.values():
            motor.Set_Value(self.robotId, i)
