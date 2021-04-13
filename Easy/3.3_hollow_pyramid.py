n = int(input("Enter the number of n: "))

for i in range(n):
    for j in range(n*2-1):
        if(i+j == n-1 or j-i == n-1):
            print("*", end="")
        else:
            print(" ",end="")
    print()

