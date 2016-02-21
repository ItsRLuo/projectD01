import matplotlib
matplotlib.use("PDF")
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_ylabel('a'*50000)
plt.tight_layout()