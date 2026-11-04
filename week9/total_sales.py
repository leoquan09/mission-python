sales = []
days = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',]
total = 0

for day in days:
    sales.append(input(f'Enter the total sales for {day}: '))

for sale in sales:
    total += int(sale)

print(f'Your total sales for this week is {total}')
