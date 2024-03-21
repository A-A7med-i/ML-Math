import numpy as np

I = np.identity(3)
print(I)

S_M = np.identity(3) * 4
print(S_M)

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[10, 20], [30, 40]])

print(m1 + m2)

print(np.add(m1, m2))

print()

print(m2 - m1)

print(np.subtract(m2, m1))

print()

print(m1 @ m2)

print(np.dot(m1, m2))
