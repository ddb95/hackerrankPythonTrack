import heapq

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains . The second line contains an array   of  integers each separated by a space.
#
# Constraints
#
# Output Format
#
# Print the runner-up score.
#
# Sample Input 0
#
# 5
# 2 3 6 6 5
# Sample Output 0
#
# 5
# Explanation 0
#
# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
# [2, 3, 6, 6, 5]
# 12, 35, 1, 10, 34, 1]
n = int(input("Enter the length"))


def findSecondLargest(arr, length):
    first = second = -213
    for i in range(length):
        if (arr[i] > first):
            second = first
            first = arr[i]
        elif (arr[i] > second and arr[i] != first):
            second = arr[i]
    print(second)


num_array = list()

for i in range(int(n)):
    z = input("enter array items:")
    num_array.append(int(z))

print(num_array)
findSecondLargest(num_array, n)
