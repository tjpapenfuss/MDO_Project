import numpy as np
import math
import matplotlib.pyplot as plt

# t = linspace(0, 2*math.pi, 400)
# a = sin(t)
# b = cos(t)
# c = a + b
plt.rcParams["figure.autolayout"] = True

x1 = np.linspace(-5,5,101)
x2 = np.linspace(-5,5,101)

t = x1**2 + x2**2 
t2 = x2**2 - ((x1-1)**3)

#plt.plot(t, 'r') # plotting t, a separately 
# plt.plot(t2, 'g')
#plt.plot(t, b, 'b') # plotting t, b separately 
#plt.plot(t, c, 'g') # plotting t, c separately 

plt.plot(x2, -(x1**2)**.5, 'r')
plt.plot(x2, ((x1-1)**3)**.5, 'r')
plt.show()

