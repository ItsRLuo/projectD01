import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.ion() # My interactive backend is Qt4Agg, with default @ 80 DPI

""" Prepare and plot 2 FancyArrowPatch instances, the 2nd one with a 
    mutation_scale parameter 3 times bigger than the 1st one. 
"""
common_opts = dict(arrowstyle=u'->', lw=3)
arrow_patch_0 = FancyArrowPatch(posA=(0.2, 0.8), posB=(0.8, 0.65),
                                mutation_scale=50, **common_opts)
arrow_patch_1 = FancyArrowPatch(posA=(0.2, 0.2), posB=(0.8, 0.45),
                                mutation_scale=150, **common_opts)

fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
ax.text(0.2, 0.85, "mutation_scale = 50", ha='left', va='bottom')
ax.text(0.2, 0.15, "mutation_scale = 150", ha='left', va='top')
for arrow_patch in [arrow_patch_0, arrow_patch_1]:
    ax.add_patch(arrow_patch)

""" Export to different formats, with different DPI values if rasterized.
"""
common_prefix = 'FancyArrowPatch_testfile'
fig.savefig(common_prefix + '.eps')
fig.savefig(common_prefix + '.pdf')
fig.savefig(common_prefix + '_300dpi.png', dpi=300)
fig.savefig(common_prefix + '_100dpi.png', dpi=100)
fig.savefig(common_prefix + '_300dpi.jpg', dpi=300)
fig.savefig(common_prefix + '_100dpi.jpg', dpi=100)