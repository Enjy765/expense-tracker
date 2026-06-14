Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> expenses = []
... 
... print("Expense Tracker")
... print("Enter expenses one by one.")
... print("Type 0 to finish.\n")
... 
... while True:
...     expense = float(input("Enter expense: "))
... 
...     if expense == 0:
...         break
... 
...     expenses.append(expense)
... 
... total = sum(expenses)
... 
... print("\n----- Summary -----")
... print("Number of Expenses:", len(expenses))
... print("Expenses:", expenses)
