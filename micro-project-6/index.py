class bankAcc:
    def __init__(self,owner,balance=0):
        print("initalizing bank account for user")

        self.owner=owner
        self.balance=balance


    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("invalid amount to deposit.please crosscheck")

    def withdraw(self,amount):
        
        if amount>self.balance:
            print("insufficient funds.")
        elif amount==0:
            print("amount cannot be null")
        else:
            self.balance-=amount
            print(f"with drawl of {amount} successful from {self.balance}")


    def get_balance(self):
        balance=self.balance
        print(f"{balance}")

if __name__=="__main__":
    account=bankAcc("Prab",100)

    print(f"👤 Account owner: {account.owner}")
    print(f"💰 Initial balance: ${account.get_balance()}")

    account.deposit(50)     # +50
    account.withdraw(30)    # -30
    account.withdraw(200)   # too much
    account.deposit(-10)