import pyrosim.pyrosim as pyrosim


def create_world(length, width, height, x, y, z):

    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()


def create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, .5, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[.5, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[.5, .5, .5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="BackLeg_FrontLeg", parent="BackLeg", child="FrontLeg", type="revolute", position=[1, 0, 0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, .5, -.5], size=[1, 1, 1])
    pyrosim.End()


create_world(1, 1, 1, -2, 2, .5)

create_robot()
