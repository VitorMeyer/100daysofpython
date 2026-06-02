# 10%3 == 1 
#CheckOdd or even

numberToCheck = int(input("What number do you want to test? \n") )

if numberToCheck % 2 != 0:
    print(f"{numberToCheck} is Odd")
else:
    print(f"{numberToCheck} is Even")