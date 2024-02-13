import pyrosim.pyrosim as pyrosim


def create_world(length, width, height, x, y, z):

    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()


def create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="BackLeg", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="BackLeg", child="Torso", type="revolute", position=[0, .5, 1])
    pyrosim.Send_Cube(name="Torso", pos=[0, .5, .5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 1, 0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, -.5], size=[1, 1, 1])
    pyrosim.End()


create_world(1, 1, 1, -2, 2, .5)

create_robot()
