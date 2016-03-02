import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_ylabel('a'*9)
plt.tight_layout()
plt.savefig("regular_ylabel.png")