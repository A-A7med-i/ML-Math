import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, num=10)

# [-5.         -3.88888889 -2.77777778 -1.66666667 -0.55555556  0.55555556
#   1.66666667  2.77777778  3.88888889  5.        ]
print(x)


# probability density function (PDF) for a normal distribution
# f(x) = (1 / (σ * sqrt(2π))) * exp( - ((x - μ)² / (2σ²)) )


print(norm.pdf(x))
# [1.48671951e-06 2.07440309e-04 8.42153448e-03 9.94771388e-02
#  3.41892294e-01 3.41892294e-01 9.94771388e-02 8.42153448e-03
#  2.07440309e-04 1.48671951e-06]

# Cumulative distribution function (CDF)
print(norm.cdf(x))
# [2.86651572e-07 5.03521029e-05 2.73660179e-03 4.77903523e-02
#  2.89257361e-01 7.10742639e-01 9.52209648e-01 9.97263398e-01
#  9.99949648e-01 9.99999713e-01]

plt.plot(x, norm.pdf(x))
plt.show()

plt.plot(x, norm.cdf(x))
plt.show()
