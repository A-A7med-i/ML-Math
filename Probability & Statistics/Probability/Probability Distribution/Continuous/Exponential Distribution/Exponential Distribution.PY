import numpy as np
from scipy.stats import expon
import seaborn as sns
import matplotlib.pyplot as plt

lambda_1 = 1 / 5
lambda_2 = 1 / 2

mean_1 = expon.stats(loc=0, scale=1 / lambda_1, moments="m")
mean_2 = expon.stats(loc=0, scale=1 / lambda_2, moments="m")

# 5.0 2.0
print(mean_1, mean_2)

x = np.linspace(1, 20)


# denstiy function
pdf_1 = expon.pdf(x, loc=0, scale=1 / lambda_1)
pdf_2 = expon.pdf(x, loc=0, scale=1 / lambda_2)

plt.plot(pdf_1)
plt.plot(pdf_2)

plt.show()


# Cumulative function
cdf_1 = expon.cdf(x, loc=0, scale=1 / lambda_1)
cdf_2 = expon.cdf(x, loc=0, scale=1 / lambda_2)

plt.plot(cdf_1)
plt.plot(cdf_2)

plt.show()


# small random sample
d_1 = np.random.exponential(scale=1 / lambda_1, size=10)
sns.histplot(d_1, kde=True)
plt.show()


# big random sample
d_2 = np.random.exponential(scale=1 / lambda_1, size=10000)
sns.histplot(d_2, kde=True)
plt.show()
