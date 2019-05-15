# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format
#
# A single line containing a string .
#
# Constraints
#
#
# Output Format
#
# Print the modified string .
#
# Sample Input 0
# HackerRank.com presents "Pythonist 2".

# Sample Output 0
# hACKERrANK.COM PRESENTS "pYTHONIST 2".




import sys
if __name__ == '__main__':

    # HackerRank.com presents "Pythonist 2".
    # hACKERrANK.COM PRESENTS "pYTHONIST 2".

    def swap_case(s):
        for i in range(len(s)):
            if(ord(s[i])>64 and ord(s[i])<91):
                stringss=s[i].lower()
                sys.stdout.write(stringss)
            elif(ord(s[i])>96 and ord(s[i])<123):
                stringss=s[i].upper()
                sys.stdout.write(stringss)
            elif(ord(s[i])>124 and ord(s[i])<125):
                stringss=s[i]
                sys.stdout.write(stringss)
            elif(ord(s[i])>90 and ord(s[i])<97):
                stringss=s[i]
                sys.stdout.write(stringss)
            elif(ord(s[i])>32 and ord(s[i])<65):
                stringss=s[i]
                sys.stdout.write(stringss)
            elif(ord(s[i])==32):
                stringss=s[i]
                sys.stdout.write(stringss)



    s = str(input())
    stringArrays = []
    swap_case(s)
#hACKERrANK.COM PRESENTS "pYTHONIST 2".
#hACKERrANK.COM PRESENTS "pYTHONIST 2".