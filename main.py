from savings_account import SavingsAccount
from checkings_account import CheckingAccount

def main():
    # Scenario 1: A user opens a savings account and applies interest
    print("Scenario 1: Savings Account")
    savings_account1 = SavingsAccount("Muhammed Akbar", 123456789, 987654321, 5000.00, 0.00, 2.5)
    savings_account1.print_customer_information()
    savings_account1.deposit(500)
    savings_account1.apply_interest()

    # Scenario 2: A user opens a checking account and attempts a transfer
    print("\nScenario 2: Checking Account")
    checking_account1 = CheckingAccount("Raja Birbal", 987654321, 123456789, 1500.00, 50.00, 1000.00)
    checking_account1.print_customer_information()
    checking_account1.deposit(200)
    checking_account1.transfer(1200)
    checking_account1.transfer(500)  # Should be successful

    # Creating two more instances to test
    print("\nScenario 3: Additional Savings Account")
    savings_account2 = SavingsAccount("Jalaluddin", 111111111, 222222222, 1000.00, 100.00, 3.0)
    savings_account2.deposit(100)
    savings_account2.apply_interest()

    print("\nScenario 4: Additional Checking Account")
    checking_account2 = CheckingAccount("Anarkali", 999999999, 888888888, 3000.00, 200.00, 500.00)
    checking_account2.print_customer_information()
    checking_account2.transfer(200)
    checking_account2.transfer(600)  # Should fail due to transfer limit

if __name__ == "__main__":
    main()
