import pyrosim.pyrosim as pyrosim


def create_world(length, width, height, x, y, z):

    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()


create_world(1, 1, 1, 0, 0, .5)
