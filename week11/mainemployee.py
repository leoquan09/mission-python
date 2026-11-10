from Employee import Employee

Susan_Meyers = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
Mark_Jones = Employee("Mark Jones", "39119", "IT", "Programmer")
Joy_Rogers = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

print(f"Name: {Susan_Meyers.name}, ID Number: {Susan_Meyers.id}, Department: {Susan_Meyers.department}, Job Title: {Susan_Meyers.title}")
print(f"Name: {Mark_Jones.name}, ID Number: {Mark_Jones.id}, Department: {Mark_Jones.department}, Job Title: {Mark_Jones.title}")
print(f"Name: {Joy_Rogers.name}, ID Number: {Joy_Rogers.id}, Department: {Joy_Rogers.department}, Job Title: {Joy_Rogers.title}")
