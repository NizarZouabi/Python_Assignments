class Bank_Account:
    instances = []
    #neroaccounts = ['Bank_Account1','Bank_Account2']
    #karenaccounts = ['Bank_Account3','Bank_Account4']
    account_balance = 0
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.account_balance = balance
        Bank_Account.instances.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        return(self)

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.account_balance -= 5
        return(self)

    def display_account_info(self):
        print(f'Balance: ${self.account_balance}')
        return(self)

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.int_rate
            percentage = self.int_rate
            print('With interest rate of: {:.0%}'.format(percentage))
        return(self)
    
    def __str__(self):
        return f"Interest rate: {self.int_rate}, Balance: {self.account_balance}"
    
    @classmethod
    def show_instances(cls):
        for id, instance in enumerate(cls.instances, start=1):
            print(f"Class Instance {id}: {instance}")
            

Bank_Account1 = Bank_Account(0.01, 1200)
Bank_Account2 = Bank_Account(0.02, 800)

Bank_Account3 = Bank_Account(0.03, 400)
Bank_Account4 = Bank_Account(0.03, 1050)

class User:
    
    def __init__(self, name, Bank_Account, Bank_Account2):
        self.user_name = name
        self.account = Bank_Account
        self.account2 = Bank_Account2

    def make_withdrawal(self, account, amount):
        if amount <= account.account_balance:
            account.account_balance -= amount
            print(f'User: {self.user_name} withdrawed {amount}')
        else:
            print("The given Numbers exceeds your Balance")
            account.account_balance -= 5
        return self
    
    def make_deposit(self, account, amount):
        account.account_balance += amount
        print(f'User: {self.user_name} deposited {amount}')
        return self

    def display_user_balance(self, account):
        print(f"User: {self.user_name}, {account}")
        return self

    def transfer_money(self, other_user, account, amount):
        if amount <= account.account_balance:
            account.account_balance -= amount
            other_user.account.account_balance += amount
            print(f'{self.user_name} Transferred {amount} to {other_user.user_name}')
        else:
            print("Insufficient balance")
        return self
 


user_01 = User("Nero", Bank_Account1, Bank_Account2)
user_02 = User("Karen", Bank_Account3, Bank_Account4)


user_01.display_user_balance(user_01.account2).make_deposit(user_01.account2, 200).display_user_balance(user_01.account2)
print()
user_01.display_user_balance(user_01.account)
user_02.display_user_balance(user_02.account).transfer_money(user_01, user_02.account, 120).display_user_balance(user_02.account)
user_01.display_user_balance(user_01.account).make_withdrawal(user_01.account, 200).display_user_balance(user_01.account)
