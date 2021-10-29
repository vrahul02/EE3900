import numpy as np
import math
from matplotlib import pyplot as plt

y = np.linspace(-6,6,100)

def x(y):
    return (y**2)/8

plt.grid()
plt.title('Parabola')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x(y),y,'b',label='$y^2=8x$')

plt.legend()