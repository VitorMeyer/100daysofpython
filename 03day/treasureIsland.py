print("Welcome to Treasure Island.")
print("Your mission is to find the hidden treasure.")
print("You arrive at a dark, misty crossroad. The air is thick with mystery.")


print("There is a path to the 'left' into the spooky forest, and a path to the 'right' towards the rocky cliffs.")

action = input("Left ou Right? \n Type L or R\n")

if action == "L":

    print("You step onto the rocky path, but the ground gives way! You fall into a deep, hidden hole.")
    print("Game Over.")
else:
    print("You step onto the rocky path, but the ground gives way! You fall into a deep, hidden hole.")
    
    action = input("Swim or wait? \n Type S or W \n")
    if action == "S":
        print("You dive into the water, but it's a trap! You are attacked by a school of giant, angry trout.")
        print("Game Over.")    
    else:
        print("You wait patiently. Suddenly, a magical wooden boat appears and ferries you to the island.")
        print("You stand before a massive ancient temple with three majestic doors.")

        action = input("There is a 'Red' door, a 'Yellow' door, and a 'Blue' door. Which one do you open?\n Type R, B or Y\n")

        if action == "R":
            print("You open the red door. A massive fireball erupts from the room! You are burned by fire.")
            print("Game Over.")

        elif action == "B":
                print("You open the blue door. A pack of shadow beasts lunges out of the darkness! You are eaten by beasts.")
                print("Game Over.")
        elif action == "Y":
             print("You slowly open the yellow door. The room is filled with glittering gold and ancient jewels!")
             print("You Win!")
        else:
             print("You hesitate and try to find another way, but you step on a trap and the temple collapses on you.")
             print("Game Over.")