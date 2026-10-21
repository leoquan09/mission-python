num_str = input("Enter a string of numbers to find the sum of: ")
num_str_l = [int(i) for i in num_str]
sum = sum(num_str_l)
print(sum)
