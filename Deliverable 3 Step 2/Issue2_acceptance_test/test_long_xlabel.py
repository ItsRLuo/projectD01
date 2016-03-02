import matplotlib
import matplotlib.pyplot as plt
"""
This test will use set_xlabel() with tight_layout().
The test make sure that if the x label are set to a long length
it should still work.
"""
fig, ax = plt.subplots()
ax.set_xlabel('a'*50000)
plt.tight_layout()
plt.savefig("long_xlabel.png")