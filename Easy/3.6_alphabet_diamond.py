n = int(input("Enter the number of n: "))

for i in range(1, n+1):
    for j in range(1,n-i+1):
        print("A", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("+", end="")
        else:
            print("E", end="")
    for k in range(n+1,(2*n)-(i-1)):
        print("B",end="")
    print()
for i in range(n-1,0, -1):
    for j in range(1,n-i+1):
        print("C", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("+", end="")
        else:
            print("E", end="")
    for k in range(n+1,(2*n)-(i-1)):
        print("D",end="")
    print()
    
