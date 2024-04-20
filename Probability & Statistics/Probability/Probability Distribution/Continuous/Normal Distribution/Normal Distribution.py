import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt

# get the prob. < 2
# standard normal
p_1 = norm.cdf(2)

# 0.9772498680518208
print(p_1)


# get the prob. < 2
# normal with mean 10 and std = 3
p_2 = norm.cdf(2, loc=10, scale=3)

# 0.0038303805675897365
print(p_2)

x = np.arange(-5, 5)

pdf_1 = norm.pdf(x)
cdf_1 = norm.cdf(x)

# plot pdf
sns.barplot(x=x, y=pdf_1)
plt.show()

# plot cdf
plt.plot(cdf_1)
plt.show()

# small random sample size
d_1 = np.random.normal(size=10)
sns.histplot(d_1, kde=True)
plt.show()


# big random sample size
d_2 = np.random.normal(size=10000)
sns.histplot(d_2, kde=True)
plt.show()
