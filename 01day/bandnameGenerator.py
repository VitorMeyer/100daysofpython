"""
Band Name Generator Project
    create a freeting for nyour program
    Ask the user for the cityy that they grew up in
    and store. it in a variable.
    ask the user the name of a pet and store it in a variable.
    Combine the name of their city and pet and show them their band name.


"""

print("Welcome to the Band Name Generator.")
nameCity = input("What's the name of the city you grew up in?\n")
namePet = input("What's your pet's name?\n")

print('Your band name is: ' + namePet + " " + nameCity)