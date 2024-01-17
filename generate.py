import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = height/2

for b in range(5):

    for j in range(5):

        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        for i in range(10):
            z += 1
            length = length * .90
            width = width * .90
            height = height * .90
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        height, width, length = 1, 1, 1
        z = height/2
        x += 1
    length = 1
    width = 1
    height = 1
    x = 0
    y += 1
    z = height / 2


pyrosim.End()
