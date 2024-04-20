import numpy as np
from scipy.stats import uniform
import seaborn as sns
import matplotlib.pyplot as plt

a = 10
b = 50

# mean , var
sigma, mu = uniform.stats(loc=a, scale=b - a, moments="mv")

# 30.0 133.33333333333331
print(sigma, mu)

# find the prob. for x < 20
p_1 = uniform.cdf(20, loc=a, scale=b - a)

# 0.25
print(p_1)

# find the prob. for 20 < x < 40
p_1 = uniform.cdf(20, loc=a, scale=b - a)
p_2 = uniform.cdf(40, loc=a, scale=b - a)

# 0.5
print(p_2 - p_1)

x = np.arange(a, b + 1)
pdf = uniform.pdf(x, loc=a, scale=b - a)
cdf = uniform.cdf(x, loc=a, scale=b - a)

# plot the denstiy function
plt.plot(x, pdf)
plt.show()

# plot the cumulative function
plt.plot(x, cdf)
plt.show()

# small random sample size
d_1 = np.random.uniform(a, b, size=10)
sns.histplot(d_1)
plt.show()

# big random sample size
d_2 = np.random.uniform(a, b, size=10000)
sns.histplot(d_2)
plt.show()
