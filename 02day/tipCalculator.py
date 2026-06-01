print("Welcome to the tip calculator!")

totalBill= float(input("What was the total bill?"))
whatmuchTip = int(input("How much tip would you like to give? 10, 12, or 19?"))
howmanyPeople = int(input("How many people to split the bill?"))

calculateTip = round(((totalBill * (whatmuchTip / 100) ) / howmanyPeople), 2 )

print(f"Each person should pay: ${calculateTip}")