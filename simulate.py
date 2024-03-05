from simulation import SIMULATION

simulation = SIMULATION()
SIMULATION.Run(simulation)


# # numpy.save('data/front_targetAngles.npy', front_targetAngles)
# # numpy.save('data/back_targetAngles.npy', back_targetAngles)
# # exit()
#

#

# print(backLegSensorValues)
# print('--------------------------- \n')
# print(frontLegSensorValues)
# subdirectory = 'data'
#
# if not os.path.exists(subdirectory):
#     os.makedirs(subdirectory)
# backLegFile = os.path.join(subdirectory, 'backLegSensorValues.npy')
# frontLegFile = os.path.join(subdirectory, 'frontLegSensorValues.npy')
#
# numpy.save(backLegFile, backLegSensorValues)
# numpy.save(frontLegFile, frontLegSensorValues)
