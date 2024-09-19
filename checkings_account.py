from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, name, account_number, routing_number, current_balance, minimum_balance, transfer_limit):
        super().__init__(name, account_number, routing_number, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount > self.transfer_limit:
            print(f"Transfer of ${amount} denied. Transfer limit is ${self.transfer_limit:.2f}.")
        else:
            self.current_balance -= amount
            print(f"Transfer of ${amount} successful. New balance: ${self.current_balance:.2f}")
