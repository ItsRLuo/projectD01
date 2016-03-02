import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlabel('a'*9)
plt.tight_layout()
plt.savefig("regular_xlabel.png")