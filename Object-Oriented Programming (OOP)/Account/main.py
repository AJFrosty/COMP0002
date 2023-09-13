from Account import Account

myAccount = Account(1112, 20000, 4.5)

myAccount.withdraw(2500)
myAccount.deposit(3000)

print(f"ID: {myAccount.getId()} \nBalance: {myAccount.getBalance()} \nMonthly Interest Rate: {myAccount.getMonthlyInterestRate() * 100}% \nMonthly Interest: {myAccount.getMonthlyInterest()}")