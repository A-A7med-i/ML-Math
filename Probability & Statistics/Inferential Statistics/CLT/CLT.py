import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

means_1 = []

# small sample
for i in range(5):
    data = np.random.exponential(1 / 3, size=10)
    mean = data.mean()
    means_1.append(mean)

sns.histplot(means_1, kde=True)
plt.show()

means_2 = []

# big sample sample but small range
for i in range(5):
    data = np.random.exponential(1 / 3, size=1000)
    mean = data.mean()
    means_2.append(mean)

sns.histplot(means_2, kde=True)
plt.show()

means_3 = []

# big sample sample and big range
for i in range(1000):
    data = np.random.exponential(1 / 3, size=1000)
    mean = data.mean()
    means_3.append(mean)

sns.histplot(means_3, kde=True)
plt.show()
# it is become normal dist.
