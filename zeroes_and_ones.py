import numpy as np

# numbers = map(int, input().split())
# no = list(numbers)
# zeroes = no[0]
# ones = no[1]
# looops = no[2]
#
# for i in range(0,looops):
#     print(np.zeros((zeroes, zeroes)))
# for i in range(0,looops):
#     print(np.ones((ones, ones)))

nums = list(map(int, input().split()))
print(np.zeros(nums, dtype=np.int))
print(np.ones(nums, dtype=np.int))
