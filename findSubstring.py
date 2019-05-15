def checkNumberofSubstrings(string, substring):
    count =0
    for i in range(0, len(string)-len(substring)+1):
        if(string[i]==substring[0]):
            flag = 1
            for j in range(0, len(substring)):
                if(string[i+j] != substring[j]):
                    flag = 0
                    break
            if(flag == 1):
                    count = count +1

    return count;

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = checkNumberofSubstrings(string, sub_string)
    print(count)
