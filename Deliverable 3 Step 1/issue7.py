import matplotlib.pyplot as plt
import seaborn.apionly as sns
iris = sns.load_dataset('iris')

plt.figure()
for species, species_df in iris.groupby("species"):
    plt.hist(species_df["petal_length"].values, normed=True, histtype="stepfilled")
plt.legend(sorted(iris.species.unique()))

plt.show()