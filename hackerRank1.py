N = int(input())
if(N%2!=0):
    print("Weird")
elif(N % 2 == 0):
    if(N>=2 & N<5):
        print("Not Weird")
    elif(N>=6 & N<=20):
        print("Weird")
    elif(N >=20):
        print("Not Weird")
