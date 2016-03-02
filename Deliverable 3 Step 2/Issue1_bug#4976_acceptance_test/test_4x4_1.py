import numpy as np
import matplotlib.pyplot as plt

"""
This test will use imshow() with tight_layout() outside the loop.
The test make sure the fix does not break anything that was working
before.
"""

plt.figure()
for i in range(16):
    ax= plt.subplot(4,4 ,i+1)
    im=ax.imshow(np.random.normal(size=100).reshape([10,10]))
    plt.title(i)
plt.tight_layout()
plt.savefig('imshow_4x4_1.png')