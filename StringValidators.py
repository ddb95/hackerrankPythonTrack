def checkIsalnum(a):
    state = False;
    for i in range(0,len(a)):
        if(arr[i].isalnum()):
            state = True

    print(state)


def checkIsalphabetical(a):
    state = False;
    for i in range(0,len(a)):
        if(arr[i].isalpha()):
            state = True

    print(state)

def checkHasDigits(a):
    state = False;
    for i in range(0,len(a)):
        if(arr[i].isdigit()):
            state = True

    print(state)
def checklowerCase(a):
    state = False;
    for i in range(0,len(a)):
        if(arr[i].islower()):
            state = True

    print(state)

def checkUpperCase(a):
    state = False;
    for i in range(0,len(a)):
        if(arr[i].isupper()):
            state = True

    print(state)


if __name__ == '__main__':
    s = input()
    arr = list(s)
    print(len(arr))
    checkIsalnum(arr);
    checkIsalphabetical(arr);
    checkHasDigits(arr);
    checklowerCase(arr);
    checkUpperCase(arr);
