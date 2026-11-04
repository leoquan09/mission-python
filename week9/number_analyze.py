nums = []

for i in range(20):
    nums.append(int(input('Enter a number to add to the number set: ')))

print(f"Minimum: {min(nums)}")
print(f"Maximum: {max(nums)}")
print(f"Sum: {sum(nums)}")
print(f"Average: {sum(nums)/20}")
