import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
y = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.plot( np.cos(x), y)

plt.show()