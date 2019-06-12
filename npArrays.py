import numpy as np


def arrays(arr):
    a = sorted(np.array(arr))
    return np.array(a).astype(float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
