is_on = True
nums = []

while is_on:
    num = int(input("Enter a positive number to add or negative number to cancel: "))
    if num < 0:
        is_on = False
        print(sum(nums))
    else:
        nums.append(num)
