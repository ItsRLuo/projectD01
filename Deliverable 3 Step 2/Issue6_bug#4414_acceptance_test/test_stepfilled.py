import matplotlib.pyplot as plt
import seaborn.apionly as sns
"""
The test makes sure the fix does not break whatever was working before.
It creates a histogram with plt.hist(), passing paramater histtype="stepfilled".
The result should produce a image with its y-axis max value = 14.
"""

iris = sns.load_dataset('iris')

plt.figure()
for species, species_df in iris.groupby("species"):
    plt.hist(species_df["petal_length"].values, histtype="stepfilled")
plt.legend(sorted(iris.species.unique()))

plt.savefig("stepfilled.png")
