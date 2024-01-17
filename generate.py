import pyrosim.pyrosim as pyrosim


def create_world(length, width, height, x, y, z):

    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()


def create_robot():

    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1])
    pyrosim.Send_Cube(name="Link1", pos=[0, 0, .5], size=[1, 1, 1])
    pyrosim.End()


create_world(1, 1, 1, -2, 2, .5)

create_robot()
