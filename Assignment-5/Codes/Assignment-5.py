import numpy as np
import math
from matplotlib import pyplot as plt

y = np.arange(-6,6,0.1)

def x(y):
    return (y**2)/8

plt.grid()
plt.title('Parabola')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x(y),y,'blue',label='$y^2=8x$')

# Focus
f=[2,0]
plt.scatter(f[0],f[1],color='red',label='Focus')

# Latus rectum
y1 = np.arange(-4,4,0.1)
x1=2+0*y1
plt.plot(x1,y1,color='green',label='latus rectum')

# Directrix
y2 = np.arange(-6,6,0.1)
x2=-2+0*y2
plt.plot(x2,y2,color='yellow',label='directrix')

# Axis
x3 = np.arange(-2,5,0.1)
y3=0+0*x3
plt.plot(x3,y3,color='brown',label='axis')

plt.legend()