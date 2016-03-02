import matplotlib
import matplotlib.pyplot as plt
"""
This test will use set_xlabel() with tight_layout().
The test makes sure the fix does not break whatever was working before.
If the x axis has a reasonable length label, it should still work and
produce an image.
"""
fig, ax = plt.subplots()
ax.set_xlabel('a'*9)
plt.tight_layout()
plt.savefig("regular_xlabel.png")