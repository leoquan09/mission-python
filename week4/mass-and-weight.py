# 5. Mass and Weight
# 
# Scientists measure an object's mass in kilograms and its weight in
# newtons. If you know the amount of mass of an object in kilograms, you
# can calculate its weight in newtons with the following formula:
# 
# weight = mass * 9.8
# 
# Write a program that asks the user to enter an object's mass, then
# calculates its weight. If the object weighs more than 500 newtons, display
# a message indicating that it is too heavy. If the object weighs less than 100
# newtons, display a message indicating that it is too light.

mass = float(input("Enter a mass to convert to weight in newtons: "))
result = mass * 9.8
if result > 500:
    print(f"This object is too heavy! It was {result} newtons")
elif result < 100:
    print(f"This object is too light! It was {result} newtons")
else:
    print(f"The object is {result} newtons")
