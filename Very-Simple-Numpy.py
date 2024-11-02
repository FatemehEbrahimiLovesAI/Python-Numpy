import numpy as np

array = np.random.randint(0,100,(4,4))
np.random.seed(1)
print("the mean is :", np.mean(array))
print("the max is :", np.max(array))
print("the min is :", np.min(array))
print("the sum is :", np.sum(array))
