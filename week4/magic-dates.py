print("==================== Magic Date Checker! ====================")

month = int(input("Enter a month in numeric form: "))
day = int(input("Enter a day: "))
year = int(input("Enter a two-digit year: "))

if month * day == year:
    print("This day is a magic date!")
else: 
    print("This day is not a magic date...")
