import matplotlib.pyplot as plt
import seaborn.apionly as sns
"""
This test checks to see if the original bug is fixed.
It creates a histogram with plt.hist(), passing paramaters normed=True and
histtype="stepfilled". The result should produce a image with its y-axis max value = 3.
"""

iris = sns.load_dataset('iris')

plt.figure()
for species, species_df in iris.groupby("species"):
    plt.hist(species_df["petal_length"].values, normed=True, histtype="stepfilled")
plt.legend(sorted(iris.species.unique()))

plt.savefig("stepfilled_normed.png")
