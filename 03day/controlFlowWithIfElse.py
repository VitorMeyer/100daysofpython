# # operator
# > greater than
# < less than
# >= greater than or equal TimeoutError
# <= less than or equal to
# == equal to
# != not equal to




# print("Welcome to the rollercoaster!")
# height = int(input("Whats is your height in cm? \n"))

# if height <= 120:
#     print("You can't ride the rollercoaster! ")
# else:
#     print("you can ride the rollercoaster!")    





# print("Welcome to the rollercoaster!")
# height = int(input("Whats is your height in cm? \n"))

# if height <= 120:
#     age = int(input("how old are you? /n "))
#     if age <= 18:
#         print("Please pay $7,00")
#     else:
#         print("Please pay $12,00")


# else:
#     print("you can ride the rollercoaster!")    



print("Welcome to the rollercoaster!")
height = int(input("Whats is your height in cm? \n"))

if height >= 120:
    age = int(input("how old are you? /n "))
    if age <= 12:
        print("Please pay $5,00")
    elif age <=18:
        print("Please pay $7,00")
    else:
        print("Please pay $12,00")
else:
    print("you can ride the rollercoaster!")    
