import numpy as np
from scipy.stats import poisson
import seaborn as sns
import matplotlib.pyplot as plt

# small lamda
lambda_1 = 2

# big lamda
lambda_2 = 10

x = np.arange(1, 11)

pmf_1 = poisson.pmf(lambda_1, x)
pmf_2 = poisson.pmf(lambda_2, x)

sns.barplot(x=x, y=pmf_1)
plt.show()


sns.barplot(x=x, y=pmf_2)
plt.show()


# Small random sample size and small lamda
d_1 = np.random.poisson(lambda_1, size=10)
sns.histplot(d_1)
plt.show()

# Big random sample size and small lamda
d_2 = np.random.poisson(lambda_1, size=10000)
sns.histplot(d_2)
plt.show()


# Small random sample size and big lamda
d_3 = np.random.poisson(lambda_2, size=10)
sns.histplot(d_3)
plt.show()

# Big random sample size and big lamda
# It is approaching to normal dist.
d_4 = np.random.poisson(lambda_2, size=10000)
sns.histplot(d_4)
plt.show()
