import numpy as np

np.random.seed(1)
array = np.random.randint(0, 100, (4, 4))
print("The mean is:", np.mean(array))
print("The max is:", np.max(array))
print("The min is:", np.min(array))
print("The sum is:", np.sum(array))