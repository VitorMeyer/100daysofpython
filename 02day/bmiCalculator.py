# The body mass index (BMI) is a measure used in medicine 
# to see if someone is underweight or overweight. 
# This is the formula used to calculate it:



# bmi is equal to the person's weight divided by the person's height squared.

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height**2
print(bmi)

print(round(bmi,2))

score = 0

# User scores a point

score += 1

print(score)

# f-strings

scoreUser = 0
width = 1.75
iswinning = True
print(f"User score is {scoreUser}, width is {width} and user is winning? {iswinning} ")

a = int("5")/ int(2.7)
print(f"result is:{a} and type is {type(a)}")