name = input("Enter a name to convert into initials: ")
name_list = name.split()
initials = ""

for i in name_list:
    initials += f"{i[0].upper()}."
print(initials)
