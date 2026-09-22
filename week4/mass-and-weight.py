mass = float(input("Enter a mass to convert to weight in newtons: "))
result = mass * 9.8
if result > 500:
    print(f"This object is too heavy! It was {result} newtons")
elif result < 100:
    print(f"This object is too light! It was {result} newtons")
else:
    print(f"The object is {result} newtons")
