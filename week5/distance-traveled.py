speed = float(input("What is the speed of the vehicle in mph? "))
time = int(input("How many hours has it traveled? "))

print("Hour\tDistance (Miles)")
print("-" * 25)

for hour in range(1, time + 1):
    distance = speed * hour
    print(f"{hour}\t{distance:.2f}")
