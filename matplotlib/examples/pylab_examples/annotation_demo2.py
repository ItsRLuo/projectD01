
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np



if 1:
    fig = plt.figure(2)
    fig.clf()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1, 5), ylim=(-5, 3))

    el = Ellipse((2, -1), 0.5, 0.5)
    ax.add_patch(el)

    ax.annotate('simple', xy=(2., -1), xycoords='data',
                xytext=(100, 60), textcoords='offset points',
                size=20,
                # bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="simple",
                                fc="0.6", ec="none",
                                patchB=el),
                )


plt.show()
