# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#
# Input Format
#
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
#
# Constraints
#
# There will always be one or more students having the second lowest grade.
# Output Format
#
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
#
# Berry
# Harry
# Explanation 0
#
# There are  students in this class whose names and grades are assembled to build the following list:
#
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.



####################### Working Solution for Finding second highest rank #############################################################################################
n = int(input("Enter the length"))
def findSecondLargest(arr, num):  ## to get the array of second ranks
    first = second = -2193
    fn = sn = "Not My Nigga"
    for i in range(n):
        if (arr[i][0] > first):
            second = first
            sn = fn
            first = arr[i][0]
            fn = arr[i][1]
            if (sn != "Not My Nigga" and second != -2193):
                secondNamesArray.append(sn)
                secondNumArray.append(second)
            else:
                continue
        elif (arr[i][0] > second and arr[i][0] != first):
            second = arr[i][0];
            sn = arr[i][1]
            if (sn != "Not My Nigga" and second != -2193):
                secondNamesArray.append(sn)
                secondNumArray.append(second)
            else:
                continue
    findingNamesOfRepeatingElements(secondNumArray)


def findingNamesOfRepeatingElements(secondNumbersArray):
    lastELement = secondNumbersArray[
        -1]  # finding last element of the array of SecondRank and matching each element to find repeating numbers in the original list
    for i in range(len(num_array)):
        if (lastELement == num_array[i][0]):
            print(num_array[i][1])


num_array = []
secondNamesArray = []
secondNumArray = []
theNamesArray = []

for i in range(int(n)):
    z = float(input("Enter the marks"))
    y = input("Enter the Names")
    num_array.append([z, y])

findSecondLargest(num_array, len(num_array))
#####################################################################Working SOlution##############################################################
#####################################################################HackerRank Solution for finding the second Lowest Rank##############################################################
if __name__ == '__main__':
    secondNamesArray = []
    secondNumArray = []
    theNamesArray = []


    def findSecondLargest(arr, num):  ## to get the array of second ranks
        first = second = 99999
        fn = sn = "Not My Nigga"
        if(len(arr)< 2 or len(arr)==2):
            exit()
        for i in range(len(arr)):
            if (arr[i][0] < first):
                second = first
                sn = fn
                first = arr[i][0]
                fn = arr[i][1]
                if (sn != "Not My Nigga" and second != 99999):
                    secondNamesArray.append(sn)
                    secondNumArray.append(second)
                else:
                    continue
            elif (arr[i][0] < second and arr[i][0] != first):
                second = arr[i][0];
                sn = arr[i][1]
                if (sn != "Not My Nigga" and second != 99999):
                    secondNamesArray.append(sn)
                    secondNumArray.append(second)
                else:
                    continue
        findingNamesOfRepeatingElements(secondNumArray)


    def findingNamesOfRepeatingElements(secondNumbersArray):
        lastELement = secondNumbersArray[
            0]  # finding last element of the array of SecondRank and matching each element to find repeating numbers in the original list
        for i in range(len(num_array)):
            if (lastELement == num_array[i][0]):
                storeNamesArray.append(num_array[i][1])
        storeNamesArray.sort()
        for i in range(len(storeNamesArray)):
            print(storeNamesArray[i])


    num_array = []
    storeNamesArray = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        num_array.append([score, name])
    findSecondLargest(num_array, len(num_array))
