from Admin import Admin,bank
from User import admin,User

login = False
while True:
    print("------- Hello sir ------")
    control_a=input('if you are admin then write admin\nor user pass Enter\nWrite now:')
    while True:
            if control_a == 'admin':
                print("----------------hello admin sir ---------")
                print("1.create account\n2 delete account \n3.all user accounts list \n4.total available balance \n5. total loan amount \n6. can on or off the loan feature of the bank\n7.Exits and go to the main pag")
                ac=int(input("write now : "))
                if ac == 1:
                    name=input("Please Enter your name :")
                    email=input("Enter your Email address :")
                    address=input("Enter your address :")
                    account_type=input("Enter your account type :")
                    user=User(name,email,address,account_type)
                    admin.Create_account(user)
                    print(f'your account Number : {user.account_Number}')
                elif ac==2:
                    name = input("pleas Enter your name : ")
                    admin.delete_account(name)
                elif ac==3:
                    admin.show_all_user()
                elif ac==4:
                    admin.available_balance()
                elif ac==5:
                    admin.total_loan()
                elif ac==6:
                    contr=input("Enter  True or False ")
                    if contr == "True":
                        controler=True
                    else:
                        controler=False
                    admin.loan_future(controler)
                elif ac==7:
                    break
                

            else:
                print('------------Hello user-------- ')
                control_l=int(input('1.for create a account\n2.for login\n3.Exits and go to the main pag\n write now :'))

                if control_l ==1:
                    name=input("Please Enter your name :")
                    email=input("Enter your Email address :")
                    address=input("Enter your address :")
                    account_type=input("Enter your account type :")
                    user=User(name,email,address,account_type)
                    admin.Create_account(user)
                    print(f'your account Number : {user.account_Number}')

                elif control_l ==2:
                    name=input("Please Enter your name :")
                    account_number=int(input("Enter you account number"))
                    if account_number in bank.acount_Number_list:
                        login=True
                        while login:
                            print('-----------our service--------- \n1.deposit\n2.withdraw\n3.transfer\n4.loan\n5.check balance \n6.history \n7.Exit and go to user pag')
                            lc=int(input())
                            if lc==1:
                                money =int(input("Enter your deposit amount :"))
                                user.deposit(money)
                            elif lc==2:
                                money =int(input("Enter your withdraw amount :"))
                                user.withdraw(money)
                            elif lc==3:
                                money =int(input("Enter your transfer amount :"))
                                trasfer_acount=int(input("Enter your transfer account"))
                                user.transfer_amount(money,trasfer_acnu)
                            elif lc==4:
                                money =int(input("Enter your loan amount :"))
                                user.loan(money)
                            elif lc==5:
                                user.check_balance()
                            elif lc==6:
                                user.all_history()
                            elif lc==7:
                                login =False
                                break

                            

                    else:
                        print("Your Account is'nt found pleas contact bank  autoriti")
                elif control_l == 3:
                    break
        


 