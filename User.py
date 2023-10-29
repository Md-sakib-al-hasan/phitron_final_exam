from Admin import Admin,bank
admin = Admin()
from random import randint
class User:
    
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self._email = email
        self._address = address
        self.account_type = account_type
        self.bankrupt = False
        self.balance = 0
        self.account_Number = len(name)+len(email)+len(address)+randint(0,100)
        self.loan_NO = 0
        self.history =[]
        

    
     
    def deposit(self,money):
        if money > 0:
            self.balance +=money
            self.history.append(f'deposit money : {money}')
            bank.available_balance+=money
        else:
            print("please Enter your balance more then o")
    
    def withdraw(self,money):
        if self.bankrupt is False:
            if self.balance>=money:
                self.balance -=money
                self.history.append(f'withdraw money:{money}')
                bank.available_balance -=money
            else:
                print("Withdrawal amount exceeded")
        else:
            print("your bank is bankrupt")
    
    def check_balance(self):
        print(self.balance)
    
    def transfer_amount(self,money,trasfer_acnu):
        if self.bankrupt is False:
            if self.balance>=money:
                print(bank.acount_Number_list)
                if trasfer_acnu in bank.acount_Number_list:
                    bank.acount_Number_list[trasfer_acnu].balance +=money
                    self.history.append(f' transfer money : {money}')
                    self.balance -=money
                else:
                    print("Account does not exist")
            else:
                print("Withdrawal amount exceeded")
        else:
            print("your bank is bankrupt")

    def loan(self,amount):
        if bank.loan_future is True:

            if self.loan_NO <2:
                self.loan_NO+=1
                self.history.append(f' loan money : {amount}')
                self.balance +=amount
                bank.available_balance+=amount
                bank.total_loan+=amount
            else:
                print("sorry you all ready received  tow time loan")
        else:
            print("the loan feature of bank is turn off now")

    def all_history(self):
        for it in self.history:
            print(it)

# sakib = User('sakib','@gmail.com','jumgora','saving')
# kamal = User('kamal','@gmail.com','jumgora','saving')
# admin.Create_account(sakib)
# admin.Create_account(kamal)
# sakib1 = User('sakiafafb1','@gmaiafafaf.com','jumfgora','saving')
# kamal1 = User('kamafafal1','@gafafmail.com','jumafagora','saving')
# admin.Create_account(sakib1)
# admin.Create_account(kamal1)
# sakib.deposit(100)
# kamal.deposit(800)
# admin.show_all_user()
# admin.delete_account('sakib')
# admin.show_all_user()
# admin.available_balance()
# admin.total_loan()
# admin.loan_future(False)
# sakib.loan(1000)
# admin.total_loan()