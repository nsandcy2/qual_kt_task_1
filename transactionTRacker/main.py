from user_account import UserAccount

a1 = UserAccount("sandy")
a2 = UserAccount("mohan")

a1.credit("1000")
a1.debit(200)

a2.credit(500)


print(a1.name, a1.get_summary())
print()
print(a2.name, a2.get_summary())
print()
print("Total transactions:", UserAccount.total_transactions)