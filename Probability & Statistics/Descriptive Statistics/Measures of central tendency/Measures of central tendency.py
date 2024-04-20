from statistics import mean, mode, median
import numpy as np

data = np.random.randint(-100, 100, size=20)

print(mean(data), median(data), mode(data))
