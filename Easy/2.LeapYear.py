year = int(input("Enter the Year: "))

if (year % 400 == 0):
    print("%d is leap year " %year)
elif (year % 4 == 0):
    print("%d is leap year " %year)
elif (year % 100 == 0):
    print("%d is not leap year " %year)
else:
    print("%d is not leap year " %year)