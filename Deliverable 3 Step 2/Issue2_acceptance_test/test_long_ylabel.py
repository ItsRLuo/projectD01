import matplotlib
import matplotlib.pyplot as plt
"""
This test will use set_xlabel() with tight_layout().
The test make sure that the original bug is fixed.
"""
fig, ax = plt.subplots()
ax.set_ylabel('a'*50000)
plt.tight_layout()
plt.savefig("long_ylabel.png")