dirtyDozen = [
    "Strawberries", "Spinach", "Kale", "Nectarines", "Apples", 
    "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", 
    "Celery", "Potatoes"
]

cleanFifteen = [
    "Avocados", "Sweet corn", "Pineapples", "Cabbages", "Onions", 
    "Sweet peas (frozen)", "Papayas", "Asparagus", "Mangoes", 
    "Eggplants", "Honeydew melons", "Kiwis", "Cantaloupes", 
    "Cauliflower", "Broccoli"
]



fruits_and_vegetables = [dirtyDozen, cleanFifteen]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
#print(fruits)


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[1][1])
#print(dirty_dozen[1][2])
print(F"1 -3 {dirty_dozen[1][3]}")