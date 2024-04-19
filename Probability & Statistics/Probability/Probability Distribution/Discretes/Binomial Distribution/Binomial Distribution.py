import numpy as np
from scipy.stats import binom
import seaborn as sns
import matplotlib.pyplot as plt

# Example
# Trials is 5
# p(success) = 0.9
# p(x=0) -> prob. i have not any success -> It's almost equal to zero.
# p(x=1) -> prob. i have 1 any success -> It's almost equal to zero but is greater than p(x=0).
# p(x=5) -> prob. i have 5 any success -> It's very big.


# But the random sample size is very small the above prob. does not apply to it
d_1 = np.random.binomial(n=5, p=0.9, size=10)
sns.countplot(x=d_1)
plt.show()


# the sample random size is big the above prob. can apply to it
d_2 = np.random.binomial(n=5, p=0.9, size=1000)
sns.countplot(x=d_2)
plt.show()


# scipy show the perfect or theoretical
n = 5
p = 0.9
x = np.arange(1, 6)
pmf = binom.pmf(x, n, p)
sns.barplot(x=x, y=pmf)
plt.show()
