# Matplotlib minimal example: Issue #6000
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)
U = X
V = X**2

# basic streamline plot
plt.figure()
sp1 = plt.streamplot(x, y, U, V)

# Attempt to hide lines and arrows from streamline plot
plt.figure()
sp2 = plt.streamplot(x, y, U, V)
sp2.lines.set_visible(False)
sp2.arrows.set_visible(False)

plt.show()