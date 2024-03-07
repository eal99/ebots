import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import time

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            print(jointName)

    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                joint_name = self.nn.Get_Motor_Neurons_Joint(neuronName)
                joint_name_byte = joint_name.encode()
                desired_angle = self.nn.Get_Value_Of(neuronName)
                # if joint_name_byte == b'Torso_BackLeg':
                #     # Rotate clockwise
                #     desired_angle = abs(desired_angle)
                # elif joint_name_byte == b'BackLeg_FrontLeg':
                #     # Rotate counterclockwise
                #     desired_angle = -abs(desired_angle)
                if joint_name_byte in self.motors:
                    self.motors[joint_name_byte].Set_Value(self.robotId, desired_angle)
                print(f"Motor Neuron: {neuronName} \n Joint Name: {joint_name} \n Desired Angle: {desired_angle}")

        # for motor in self.motors.values():
        #     motor.Set_Value(self.robotId, i)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

