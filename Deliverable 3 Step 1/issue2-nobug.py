import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_ylabel('a'*7)
plt.tight_layout()
plt.savefig("issue2-nobug.png")
