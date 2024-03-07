import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.num_steps)
        self.t = numpy.linspace(0, 2 * numpy.pi, c.num_steps)

        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

        self.f_amplitude = c.front_amplitude
        self.f_frequency = c.front_frequency
        self.f_offset = c.front_phaseOffset

        self.b_amplitude = c.back_amplitude
        # Adjust the back leg frequency to half if it's one motor, otherwise use the standard frequency
        if self.jointName == b'BackLeg_FrontLeg':
            self.b_frequency = c.back_frequency / 2  # Half the frequency for this specific joint
        else:
            self.b_frequency = c.back_frequency
        self.b_offset = c.back_phaseOffset

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if self.jointName == b'Torso_BackLeg':
            self.motorValues = self.f_amplitude * numpy.sin(self.f_frequency * self.t + self.f_offset)
        elif self.jointName == b'BackLeg_FrontLeg':
            self.motorValues = self.b_amplitude * numpy.sin(self.b_frequency * self.t + self.b_offset)
        else:
            print("Error: Unknown joint name", self.jointName)

    def Set_Value(self, robot, desiredAngle):
        print(f"Setting {self.jointName} to {desiredAngle}")
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce
        )


