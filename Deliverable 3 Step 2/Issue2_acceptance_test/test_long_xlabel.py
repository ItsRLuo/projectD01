import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlabel('a'*50000)
plt.tight_layout()
plt.savefig("long_xlabel.png")