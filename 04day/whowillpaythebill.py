import random
friends = ["Alice", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe"]

randomFriend = random.randint(0,5)

print(f"pay the bill, {friends[randomFriend]}!")

print(f"pay the bill,{random.choice(friends)}")

print(len(friends))