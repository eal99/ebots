import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


class ROBOT:

    def __init__(self, SolutionID):
        self.robotId = p.loadURDF("robot.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
        self.ID = SolutionID
        self.nn = NEURAL_NETWORK("brain" + str(SolutionID) + ".nndf")
        os.system("rm brain" + str(SolutionID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

                # print(neuronName + " " + jointName + " " + str(desiredAngle))

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(self.ID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("mv tmp" + str(self.ID) + ".txt" + " fitness" + str(self.ID) + ".txt")
        # print("~~~~ Look Here!! ~~~~ \n")
        # print(str(xCoordinateOfLinkZero))
        # exit()


