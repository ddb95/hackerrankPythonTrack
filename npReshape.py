import numpy as np


def arrays(arr):
    myArr = np.reshape(arr, (3, 3))
    return myArr.astype(int)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
