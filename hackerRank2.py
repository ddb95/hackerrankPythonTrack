import numpy as np
import itertools

# List Comprehensions
# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of is not equal to . Here,
#
# Input Format
#
# Four integers  and  each on four separate lines, respectively.
#
# Constraints
#
# Print the list in lexicographic increasing order.
#
# Sample Input 0
#
# 1
# 1
# 1
# 2
# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Sample Input 1
# 2
# 2
# 2
# 2
# Sample Output 1
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

x = int(input("Enter the first Input"))
y = int(input("Enter the second Input"))
z = int(input("Enter the third Input"))
n = int(input("Enter the integer Input"))
print(tuple([a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n))
print(list([a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n))
# for i in range(0,x+1):
#     l = i
#     subList=[l,m,n]
#     arrayObj.append(subList)
#     arrayObj.append(subList)
#     if(l!=k):
#         subList = [l, m, n]
#         arrayObj.append(subList)
#     for l in range(0, y+1):
#         m=l
#         if(l+m!=k):
#             subList = [l, m, n]
#             arrayObj.append(subList)
#     for m in range(0,z+1):
#         n=m
#         if(l+m+n!=k):
#             subList = [l, m, n]
#             arrayObj.append(subList)
#
#
# arrayObj.sort()
# print(arrayObj)
