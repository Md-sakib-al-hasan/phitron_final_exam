from bank import Bank
bank =Bank()
class Admin:
    def __init__(self) -> None:
        pass
    
    def Create_account(self,user):
        bank.acount_Number_list.update({user.account_Number:user})
    def show_all_user(self):
        for key,value in bank.acount_Number_list.items():
            print(value.account_Number)
    def delete_account(self,name):
        ud=''
        for key,value in bank.acount_Number_list.items():
            if value.name == name:
                ud=key
        if ud == '':
            print("this account never exist")
        else:
            bank.acount_Number_list.pop(ud)
            print("account remove is completed")
    
    def available_balance(self):
        print(bank.available_balance)
    def total_loan(self):
        print(bank.total_loan)
    def loan_future(self,controler):
        bank.loan_future = controler


    