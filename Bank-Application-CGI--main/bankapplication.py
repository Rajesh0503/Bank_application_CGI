import time
import json


def login():
    accountNo = input('enter the account number:-\n')
    with open(f"accounts/{accountNo}", "r") as fp:
        accno = json.load(fp)
        # accno = ["sachin", "redhat", 60000]
        password =input('enter the pass word:-\n')
        if accno[2]==password:
            msg='please wait loging you'
            for i in range(10):
                msg=msg+'.'
                print(f'{msg}\r',end='')
                time.sleep(.2)
            print('log in')
            return accountNo # ["sachin", "redhat", 60000]
        else:
            print('\n\n....ivalid password try again...\n\n')
            return False
    
        
def get_last_acc_number():
    with open("last_account.json", "r") as fp:
        acc = json.load(fp)
    return acc
def update_last_acc_number(acc):
    with open("last_account.json", "w") as fp:
        json.dump(acc, fp)
        
def create_new_account(record):
    old = get_last_acc_number()
    new = old+1
    update_last_acc_number(new)
    with open(f"accounts/{new}", "w") as fp:
        json.dump(record, fp)
    return new

def sign_up():
    name =input('enter your name:-  ')
    mail=input('enter your email id:-  ')
    password=input('enter your password:- ')
    balance=float(input('enter your balance:- '))
    record = [name,mail,password,balance]
    new_acc =  create_new_account(record)
    msg='creating your account'
    for i in range(10):
        msg=msg+'.'
        print(f'{msg}\r',end='')
        time.sleep(.5)
    print(f'note your account no.{new_acc}')
    input('enter any key to continue')
    
    main_menu()




        
        
        
def debit(accountNo):
    with open(f'accounts/{accountNo}','r') as fp:
        cr =json.load(fp)
        debit=float(input('enter amount you want to debit'))
        old_bal =cr[3]
        if debit<=old_bal:
            cr[3] -= debit
            with open(f"accounts/{accountNo}",'w') as fp:
                json.dump(cr,fp)
            msg='loading your debited amount'
            for i in range(10):
                msg=msg+'.'
                print(f'{msg}\r',end='')
                time.sleep(.2)
            print(f'old balance is{old_bal}')
            print(f'your new balance after debit isnow you have{cr[3]}')
        else:
            print('insufficient amount')
def credit(accountNo):
    with open(f'accounts/{accountNo}','r') as fp:
        cr =json.load(fp)
        credit=float(input('enter the amount you want credit'))
        cr[3] +=credit
        with open(f'accounts/{accountNo}','w') as fp:
            json.dump(cr,fp)
    
    msg='loading your credited amount'
    for i in range(10):
        msg=msg+'.'
        print(f'{msg}\r',end='')
        time.sleep(.5)
    print(f'your new balance is now you have{cr[3]}')
def check(accountNo):
    with open(f"accounts/{accountNo}",'r') as fp:
        ch = json.load(fp)
    msg='please wait loading your balance'
    for i in range(10):
        msg=msg+'.'
        print(f'{msg}\r',end='')
        time.sleep(.2)
    print('\n',ch[3])
def delete_acc(accountNo):
    msg='please wait deleting your account'
    for i in range(10):
        msg=msg+'.'
        print(f'{msg}\r',end='')
        time.sleep(.5)
    data1.pop(accountNo)
def password(accountNo):
    with open(f"accounts/{accountNo}",'r') as fp:
        pss =json.load(fp)
        new = input('enter the new password')
        new1 = input('confrim your new password')
        if new ==new1:
            msg='please wait changing your password'
            for i in range(10):
                msg=msg+'.'
                print(f'{msg}\r',end='')
                time.sleep(.2)
                pss[2]=new1
            with open(f"accounts/{accountNo}",'w') as fp:
                json.dump(pss,fp)
                print(f'your new password is succesfully changed ')
        
        
        
def sub_menu(accountNo):
    menu =f"""
    welcome user 
    1. Credit
    2. Debit
    3. Check balance
    4. Delete account
    5. Password change
    6.logout
    """
    while True:
        
        print(menu)
        num =int(input('enter option 1 to 4:\n\n'))
        if num ==1:
            credit(accountNo)
        elif num ==2:
            debit(accountNo)
        elif num ==3:
            check(accountNo)
        elif num==4:
            delete_acc(accountNo)
        elif num ==5:
            password(accountNo)
        elif num==6:
            print('thank you')
            break
        
        
        
last_account =1003
def main_menu():
    menu ="""
    1. LOGIN
    2. SIGN UP
    3. EXIT
   """
    print(menu)
    num =int(input('choose option between 1 to 3'))
    if num ==1:
        accountNo =login()
        if accountNo:
            print('login successfull')
            sub_menu(accountNo)
        else:
            print('log in unsuccesfull')
        main_menu()
    elif num==2:
        sign_up()
    
    elif num ==3:
        print('byee byee')
        exit(0)
    else:
        print('invalid choice')
        main_menu()
    
        
        
main_menu()
