import numpy as np
import matplotlib.pyplot as plt
"""
This test will use subplot with imshow() and tight_layout() inside the loop.
The expected output should show all 15 image. 
"""
plt.figure()
for i in range(15):
    ax= plt.subplot(3,5 ,i+1)
    im=ax.imshow(np.random.normal(size=100).reshape([10,10]))
    plt.tight_layout()
    plt.title(i)
plt.savefig('imshow_3x5.png')