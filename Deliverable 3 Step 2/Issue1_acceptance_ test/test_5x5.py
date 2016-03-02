import numpy as np
import matplotlib.pyplot as plt

"""
This test will use imshow() with tight_layout() inside the loop.
This test should create a png figure without any image missing.
"""

plt.figure()
for i in range(25):
    ax= plt.subplot(5,5 ,i+1)
    im=ax.imshow(np.random.normal(size=100).reshape([10,10]))
    plt.tight_layout()
    plt.title(i)
plt.savefig('imshow_5x5.png')