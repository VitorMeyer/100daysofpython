import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]

# compute_choise = random.randint(0,2)
# user_choise = int(input("What do you chosse? Type 0 for rock, 1 for Paper or 2 for Scissors \n"))
# if user_choise >= 3 or user_choise < 0: 
#     print("You typed an invalid number, you lose!")
# else:
#     print(f"You Choise: \n {choices[user_choise]} \n Compute choise: \n {choices[compute_choise]}")
#     if user_choise ==  compute_choise:
#         print ("Draw")
#     elif user_choise == 0 and compute_choise == 1:
#         print("You lose! =[")
#     elif user_choise == 0 and compute_choise == 2:
#         print("You Win! =]")
#     elif user_choise == 1 and compute_choise == 0:
#         print("You Win! =]")
#     elif user_choise == 1 and compute_choise == 2:
#         print("You lose! =[")
#     elif user_choise == 2 and compute_choise == 0:
#         print("You lose! =[")
#     elif user_choise == 2 and compute_choise == 1:
#         print("You Win! =]")


compute_choise = random.randint(0,2)
user_choise = int(input("What do you chosse? Type 0 for rock, 1 for Paper or 2 for Scissors \n"))
if user_choise >= 3 or user_choise < 0: 
    print("You typed an invalid number, you lose!")
else:
    print(f"You Choise: \n {choices[user_choise]} \n Compute choise: \n {choices[compute_choise]}")
    choise_sum =  user_choise - compute_choise 

    if user_choise ==  compute_choise:
        print ("Draw! ")

    elif  choise_sum in [-1, 2]: 
        print("You lose! :=[")
    elif choise_sum in [-2, 1]:
        print("You Win! ;=]")
