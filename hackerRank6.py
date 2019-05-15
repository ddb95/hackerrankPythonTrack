# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
#
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]





if __name__ == '__main__':
    N = int(input())
    student_marks = []
    mainArray = []
    k=0
    # storing the values
    for _ in range(N):
        name, *line = input().split()
        scores = list(map(int, line))
        student_marks.append([name, scores])
    for i in range(len(student_marks)):
        if(str(student_marks[i][0])=='insert'):
            mainArray.insert(student_marks[i][1][0],student_marks[i][1][1])
        elif(str(student_marks[i][0])== 'print'):
            print(mainArray)
        elif(str(student_marks[i][0])=='remove'):
            mainArray.remove(student_marks[i][1][0])
        elif(str(student_marks[i][0])=='append'):
            mainArray.append(student_marks[i][1][0])
        elif(str(student_marks[i][0])=='sort'):
            mainArray.sort()
        elif(str(student_marks[i][0])=='pop'):
            mainArray.pop()
        elif(str(student_marks[i][0])=='reverse'):
            mainArray.reverse()
