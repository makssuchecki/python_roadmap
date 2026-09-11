# try / except

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


try: 
    value = int(input("Write a number: "))
except ValueError as e:
    print(f"Invalid value: {e}")
except (TypeError, KeyError) as e:
    print(f"Other error: {e}")
else:
    print("Works when there is no exception")
finally:
    print("Always works")

# Throwing your own exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be smaller than zero")
    return age

# Exception classes

class InsufficentFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount   
        super().__init__(f"No funds: {balance} < {amount}")

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficentFundsError(self.balance, amount)
        self.balance -= amount