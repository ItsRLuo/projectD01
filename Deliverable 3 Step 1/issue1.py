import numpy as np
import matplotlib.pyplot as plt
plt.figure()
for i in range(16):
    ax= plt.subplot(4,4 ,i+1)
    im=ax.imshow(np.random.normal(size=100).reshape([10,10]))
    plt.tight_layout()
    plt.title(i)
plt.savefig("imshow_4x4.png")