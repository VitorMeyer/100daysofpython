# todo: work out how much. they need to pay based 
# ontheir size choice.
# todo work out how much to add to their bill 
# based on their pepperoni choice.
# todo: work out their final amount vased on whether 
# if they want extra chesse.

print("Welcome to Python pizza pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: \n").upper()
pepperoni  = input("Do you want pepperoni on your pizza? Y or N\n").upper()
extraCheese = input ("Do you want extra cheese?Y or N \n").upper()
bill = 0


if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 4.5
    else:
        bill += 3.5

if extraCheese =="Y":
    bill +=3.2


print(f"Please pay ${bill:.2f} for pizza!")

if size =="S" and pepperoni =="Y" :
    bill = 19.5
