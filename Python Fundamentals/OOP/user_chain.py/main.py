from user import User

user1 = User("Nizar", 1520)
user2 = User("James", 600)
user3 = User("Amal", 850)

user1.make_deposit(20).display_user_balance().make_deposit(60).display_user_balance().make_deposit(80).display_user_balance().make_withdrawal(50).display_user_balance()

print()

user2.make_deposit(300).display_user_balance().make_deposit(230).display_user_balance().make_withdrawal(400).display_user_balance().make_withdrawal(80).display_user_balance()

print()

user3.make_deposit(700).display_user_balance().make_withdrawal(400).display_user_balance().make_withdrawal(25).display_user_balance().make_withdrawal(50).display_user_balance()

print()

user1.transfer_money(user2, 170).display_user_balance()
user2.display_user_balance()
