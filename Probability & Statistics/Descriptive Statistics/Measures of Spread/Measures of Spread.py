from statistics import variance, stdev
import numpy as np

# Example:
# Find the variance and standard deviation of the numbers 3, 8, 6, 10, 12, 9, 11, 10, 12, 7.

data_1 = [3, 8, 6, 10, 12, 9, 11, 10, 12, 7]

# 8.18 2.86
print(round(variance(data_1), 2), round(stdev(data_1), 2))

# Example: Exam Scores
# Consider a set of exam scores: {50, 65, 72, 80, 88, 95, 100}

data_2 = [50, 65, 72, 80, 88, 95, 100]

print(f"Range : {max(data_2) - min(data_2)}")
print(f"Variance : {round(variance(data_2),2)}")
print(f"Standard Deviation : {round(stdev(data_2),2)}")
print(f"IQR : {np.percentile(data_2,75) - np.percentile(data_2,25)}")
