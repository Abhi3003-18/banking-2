class BankAccount:
    Title = "Bank Of Mughals"  # Class attribute

    def __init__(self, name, account_number, routing_number, current_balance, minimum_balance):
        self.name = name
        self._account_number = int(account_number)  # Protected member
        self.__routing_number = int(routing_number)  # Private member
        self.current_balance = float(current_balance)
        self.minimum_balance = float(minimum_balance)

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposit made: ${amount}, Current balance: ${self.current_balance:.2f}")
        return self.current_balance

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(f"Withdrawal of ${amount} denied. Balance cannot go below ${self.minimum_balance:.2f}.")
        else:
            self.current_balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.current_balance:.2f}")
            return self.current_balance

    def print_customer_information(self):
        print(f"{self.Title}")
        print(f"Name: {self.name}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.__routing_number}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
