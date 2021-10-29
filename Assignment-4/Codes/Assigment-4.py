import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point1  = np.array([2.5, 0, 0])
point2  = np.array([0, 5, 0])
point3  = np.array([0, 0, 5])
normal = np.array([0.4, 0.2, 0.2])

d = -point1.dot(normal)

# Create x,y
xx, yy = np.meshgrid(range(10), range(10))

# Calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# Plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z, alpha=0.2)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()