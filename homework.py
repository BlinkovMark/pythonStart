"""
Blinkov Mark
TA-21V
Task #4, Medium level
"""

i = int(input("Total amount: "))


def salary(amount):
    if amount >= 1000:
        amount -= (amount / 100) * 101
        print(amount)
    else:
        print("Amount is less than 1000")


salary(i)
