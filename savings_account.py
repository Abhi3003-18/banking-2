from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, account_number, routing_number, current_balance, minimum_balance, interest_rate):
        super().__init__(name, account_number, routing_number, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * self.interest_rate / 100
        self.current_balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.current_balance:.2f}")
