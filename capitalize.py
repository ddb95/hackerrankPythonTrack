# Complete the solve function below.
import os


def solve(s):
    buzz = ''
    s_list = s.split(' ')
    for i in range(0, len(s_list)):
        s_list[i] = s_list[i].capitalize()

    for i in range(0, len(s_list)):
        buzz += s_list[i]
        buzz += ' '
    return buzz

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()
