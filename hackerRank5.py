# You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
#
# Input Format
#
# The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
#
# Constraints
#
# Output Format
#
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#
# Sample Input 0
#
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0
#
# 56.00
# Explanation 0
#
# Marks for Malika are  whose average is
#
# Sample Input 1
#
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# Sample Output 1
#
# 26.50
if __name__ == '__main__':
    N = int(input())
    student_marks = {}
    avgMarks= 0
    meanVal=0
    for _ in range(N):
        commandS, *line = input().split()
        scores = list(map(float, line))
        student_marks[commandS] = scores
    query_command = input()
    # print(student_marks[query_command][0])
    # print(len(student_marks[query_command]))
    for i in range(len(student_marks[query_command])):
        avgMarks+=student_marks[query_command][i]
    meanVal = avgMarks / 3.0
    print(meanVal)
    print("%.2f" % meanVal)


    # print(student_marks[query_name][0])
    # print(len(student_marks[query_name]))
    # for i in range(len(student_marks[query_name])):
    #     avgMarks+=student_marks[query_name][i]
    # meanVal = avgMarks / 3.0
    # print(meanVal)
    # print("%.2f" % meanVal)
