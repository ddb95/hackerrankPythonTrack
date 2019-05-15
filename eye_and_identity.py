import numpy as np

# print(np.identity(3))
print(np.eye(7, 7, 0, dtype=int))
print('\n')
print(np.eye(7, 7, 1, dtype=int))
print('\n')
print(np.eye(7, 7, -1, dtype=int))

nums = list(map(int, input().split()))
print(np.eye(nums[0], nums[1], k=0))


