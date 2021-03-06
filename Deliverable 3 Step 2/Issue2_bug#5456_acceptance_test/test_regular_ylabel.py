import matplotlib
import matplotlib.pyplot as plt
"""
This test will use set_xlabel() with tight_layout().
The test makes sure the fix does not break whatever was working before.
If the y axis has a reasonable length label, it should still work and
produce an image.
"""
fig, ax = plt.subplots()
ax.set_ylabel('a'*9)
plt.tight_layout()
plt.savefig("regular_ylabel.png")