class User:
    
    def __init__(self, name, balance):
        self.user_name = name
        self.user_balance = balance

    def make_withdrawal(self, amount):
        if amount <= self.user_balance:
            self.user_balance -= amount
            print(f'User: {self.user_name} withdrawed {amount}')
        else:
            print("The given Numbers exceeds your Balance")
        return self
    
    def make_deposit(self, amount):
        self.user_balance += amount
        print(f'User: {self.user_name} deposited {amount}')
        return self

    def display_user_balance(self,):
        print(f"User: {self.user_name}, Balance: {self.user_balance}")
        return self

    def transfer_money(self, other_user, amount):
        if amount <= self.user_balance:
            self.user_balance -= amount
            other_user.user_balance += amount
            print(f'{self.user_name} Transferred {amount} to {other_user.user_name}')
        else:
            print("Insufficient balance")
        return self
