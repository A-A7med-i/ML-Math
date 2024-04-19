import numpy as np
from scipy.stats import bernoulli
import seaborn as sns
import matplotlib.pyplot as plt

# Example
# coin p(H) = p(T) = 0.5

# sample size is small
d_1 = np.random.binomial(n=1, p=0.5, size=5)
sns.countplot(x=d_1)

# sample size is big
d_2 = np.random.binomial(n=1, p=0.5, size=1000)
sns.countplot(x=d_2)


# scipy
# plot is perfect the prob. is equal in each other
x = [0, 1]
p = bernoulli.pmf(x, p=0.5)
sns.barplot(x=x, y=p)
plt.show()
