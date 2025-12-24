class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self._balance = balance #protected

    def get_balance(self):#getter
        return self._balance
    
    def set_balance(self, amount):#setter
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")

acc1 = BankAccount("123456789", 1000)
print(acc1.account_number)
print(acc1.get_balance())
