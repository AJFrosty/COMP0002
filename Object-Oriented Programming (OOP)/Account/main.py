from Account import Account

myAccount = Account(1112, 20000, 4.5)

myAccount.Withdraw(2500)
myAccount.Deposit(3000)

print(f"ID: {myAccount.getId()} \nBalance: {myAccount.getBalance()} \nMonthly Interest Rate: {myAccount.getMonthlyInterestRate()} \nMonthly Interest: {myAccount.getMonthlyInterest()}")