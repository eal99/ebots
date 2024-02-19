import numpy as np
import os
import matplotlib.pyplot as plt

back = os.path.join('data', 'backLegSensorValues.npy')
front = os.path.join('data', 'frontLegSensorValues.npy')
front_openLoop = os.path.join('data', 'front_targetAngles.npy')
back_openLoop = os.path.join('data', 'back_targetAngles.npy')
# backLegSensorValues = np.load(back)
# frontLegSensorValues = np.load(front)
front_sin = np.load(front_openLoop)
back_sin = np.load(back_openLoop)
# Plotting with labels
plt.plot(front_sin, label='Back Leg', linewidth=4)
plt.plot(back_sin)
# plt.plot(backLegSensorValues, label='Back Leg', linewidth=2.5)
# plt.plot(frontLegSensorValues, label='Front Leg')
#
# # Adding a legend with the specified labels
# plt.legend()

# Display the plot
plt.show()
