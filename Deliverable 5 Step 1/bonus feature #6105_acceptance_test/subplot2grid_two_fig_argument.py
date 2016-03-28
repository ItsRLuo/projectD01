import matplotlib.pyplot as plt

def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        for tl in ax.get_xticklabels() + ax.get_yticklabels():
            tl.set_visible(False)



ax1 = plt.subplot2grid((3,3), (0,0), colspan=3, fig=plt.figure(0))
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2, fig=plt.figure(5))
ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=2, fig=plt.figure(0))
ax4 = plt.subplot2grid((3,3), (2, 0), fig=plt.figure(0))
ax5 = plt.subplot2grid((3,3), (2, 1), fig=plt.figure(5))

plt.suptitle("subplot2grid")
make_ticklabels_invisible(plt.gcf())
plt.show()

