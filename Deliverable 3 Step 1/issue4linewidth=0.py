import numpy as np
import matplotlib.pyplot as plt
from numpy.random import ranf
ax = plt.subplot(111, polar=True)
for i in range(20):
    ax.bar(left=2*np.pi*i/20.0, height=ranf(), width=2*np.pi/20, color='blue', linewidth=0)
plt.show()

# normal version

# ax = plt.subplot(111)
# for i in range(20):
#     ax.bar(left=2*np.pi*i/20.0, height=ranf(), width=2*np.pi/20, color='blue', linewidth=0)
# plt.show()

'''

fix with eps (not a formal fix)

ax = plt.subplot(111, polar=True)
eps = 0.01
for i in range(20):
    ax.bar(left=2*np.pi*i/20.0, height=ranf(), width=2*np.pi/20+eps, color='blue', linewidth=0)
plt.show()

'''