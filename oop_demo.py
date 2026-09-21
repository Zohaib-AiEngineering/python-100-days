"""
Day 5: Object-Oriented Programming (OOP) Fundamentals
Modeling a Real-World Bank Account System
"""

class BankAccount:
    # Class Variable (Shared across all accounts)
    bank_name = "AI Student Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """
        Constructor method to initialize instance variables.
        """
        # HINT 1: Self ke sath instance variables store karein
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Method to deposit money into the account.
        """
        if amount > 0:
            # HINT 2: Balance me amount add karein
            self.balance += amount
            print(f"[DEPOSIT] Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("[ERROR] Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        """
        Method to withdraw money safely with balance check.
        """
        # HINT 3: Check karein agar withdrawal amount balance se chota ya barabar ho
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"[WITHDRAW] Withdrew ${amount}. Remaining Balance: ${self.balance}")
        else:
            print("[ERROR] Insufficient balance or invalid amount.")

    def display_details(self) -> None:
        """
        Prints account details.
        """
        print(f"Bank: {self.bank_name} | Holder: {self.account_holder} | Balance: ${self.balance}")


def main():
    print("--- Day 5: OOP Fundamentals Demo ---")
    
    # HINT 4: Object create karein 'Muhammad Zohaib' naam se aur initial balance 500.0 dein
    user_account = BankAccount("Muhammad Zohaib", 500.0)
    
    # Details check karein
    user_account.display_details()
    
    # Deposit test karein
    user_account.deposit(250.0)
    
    # Withdraw test karein
    user_account.withdraw(100.0)

if __name__ == "__main__":
    main()