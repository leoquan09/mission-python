date = input("Enter a date in the form mm/dd/yyyy: ")
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
date_l = date.split("/")

date_final = ""

date_final = f"{months[int(date_l[0]) - 1]} {date_l[1]}, {date_l[2]}"
print(date_final)
