
# coding: utf-8

# In[ ]:



## store initial data 
import shelve
from getpass import getpass
import os
import time


acc1 = { 'name':'ram','bal':20000,'password':'123'}
acc2 = { 'name':'shyam','bal':15000,'password':'@hello'}
acc3 = { 'name':'ghyanshaym','bal':1000,'password':'bye@'}
acc4 = { 'name':'radheshyam','bal':12000,'password':'redhat'}

db = shelve.open("Bank/bank.db")
db['1001'] = acc1
db['1002'] = acc2
db['1003'] = acc3
db['1004'] = acc4 

db.close()


def main_menu():
    try:
        
        s = """1. Login\n2.Signup\n3.admin \n4.Exit"""
        print(s)
        ch = int(input("Enter your Choice : "))
        if ch == 1 :
            acc_no = input("Enter your acc number : ").strip()
            password = getpass("Enter your password : ")
            if login(acc_no,password) :
                os.system("cls")
                menu(acc_no)
            else :
                os.system("cls")
                main_menu()
        elif ch==2:
            os.system("cls")
            sign_up()
        elif ch==3:
            os.system("cls")
            admin()
        elif ch==4:
            os.system("cls")
            Exit()
        else:
            os.system("cls")
            print("Invalide choice")
            time.sleep(4)
            os.system("cls")
            main_menu()
    except BaseException as arg:
        os.system("cls")
        print("Error !",arg)
        main_menu()
        

def login(acc_no,password):
    try:
        db = shelve.open('Bank/bank.db')
        data = db.get(acc_no,False)
        if data : 
            if data.get('password') == password :
                os.system("cls")
                print("Login Sucessfull")
                m = time.ctime()+":"+"login :"+"user :"+acc_no +"\n"
                f = open('log.txt','a')
                f.write(m)
                f.close()
                time.sleep(4)
                return True 
            else : 
                os.system("cls")
                print("Invalid Password")
                print("Try Again")
                m = time.ctime()+":"+"Error :"+"invalid password for user  :"+acc_no+"\n"
                f = open('log.txt','a')
                f.write(m)
                f.close()
                time.sleep(4)
                return False 
        else :
            os.system("cls")
            print("Invalid Account Number")
            print("If you don't have any account please signup")
            m = time.ctime()+":"+"Error :"+" invalid account number :"+ acc_no +"\n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            return False
        db.close()
    except BaseException as arg:
        print("Error !",arg)
        os.system("cls")
        main_menu()
def menu(acc_no):
    try:
        s = """1. Credit\n2.Debit\n3.Check Balance\n4.Update Password\n5.exit"""
        print(s)
        ch = int(input("Enter your choice : "))
        if ch==1:
            os.system("cls")
            credit(acc_no)
        elif ch==2:
            os.system("cls")
            debit(acc_no)
        elif ch==3:
            os.system("cls")
            check_details(acc_no)
        elif ch == 4 :
            os.system("cls")
            update_password(acc_no)
        elif ch==5:
            os.system("cls")
            exit()
        else:
            os.system("cls")
            print("Invalid choice")
            print("you are at menu of logged in function")
            time.sleep(4)
            os.system("cls")
            main_menu()
    except BaseException as arg:
        os.system("cls")
        print("Error !",arg)
        main_menu()
def credit(acc_no):
    try:
        amount=float(input("Enter the amount which you want to credit into your account  :"))
        db = shelve.open('Bank/bank.db',writeback=True)
        old_balance=db[acc_no]["bal"]
        print(old_balance)
        new_balance=old_balance+amount
        print(new_balance)
        db[acc_no]["bal"]=new_balance
        update=db[acc_no]["bal"]
        print("Your balance is updated.",update)
        db.close()
        m = time.ctime()+":"+" credited : "+str(amount)+"  in account  "+acc_no+"\n" 
        f = open('log.txt','a')
        f.write(m)
        f.close()
        time.sleep(4)
        os.system("cls")
        menu(acc_no)
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
def debit(acc_no):
    try:
        amount=float(input("Enter the amount which you want to debit"))
        db = shelve.open('Bank/bank.db',writeback=True)
        old_balance=db[acc_no]["bal"]
        if old_balance<amount:
            print("Sorry ! we can not debit that much money from your account\n due to insufficient balance.")
            time.sleep(4)
            os.system("cls")
            debit(acc_no)
        else:
            new_balance=old_balance-amount
            db[acc_no]["bal"]=new_balance
            print("Successfully debited.")
            update=db[acc_no]["bal"]
            print("Your current updated balance is",update)
            db.close()
            m = time.ctime()+":"+" debited : "+" amount : "+str(amount)+" in "+acc_no+"\n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            os.system("cls")
            menu(acc_no)
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
def check_details(acc_no):
    try:
        db = shelve.open('Bank/bank.db',writeback=True)
        details=db[acc_no]
        print(f"Your account details is \n {details}")
        db.close()
        m = time.ctime()+" : "+" check details  : " + "for account  "+acc_no+"\n"
        f = open('log.txt','a')
        f.write(m)
        f.close()
        time.sleep(4)
        os.system("cls")
        menu(acc_no)
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
    
def update_password(acc_no):
    try:
        p1 = getpass("Enter password : ")
        p2 = getpass("Verify password :")
        if p1 == p2 : 
            db = shelve.open('Bank/bank.db',writeback=True)
            db[acc_no]['password'] = p1
            print("password sucessfully updated")
            print("Please Login Again to verify ")
            db.close()
            m = time.ctime()+":"+" update password : "+"of account "+acc_no+" new password is :"+p1+":\n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            os.system("cls")
            main_menu()
        else : 
            print("Password does not match ")
            print("Try Again")
            time.sleep(4)
            os.system("cls")
            update_password(acc_no)
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
def exit():
    print("Thanks for using our services.")
    time.sleep(4)
    os.system("cls")
    main_menu()
def sign_up():
    try:

        db = shelve.open('Bank/bank.db',writeback=True)
        acc_no=int(input("Enter your account number "))
        data=list(map(int,db.keys()))
        print(data)
        if acc_no in data:
            print("Sorry ! This account number is already exit.")
            print("Try Again .")
            time.sleep(4)
            os.system("cls")
            sign_up()
        else:
            print("Please enter your details")
            new_user={
                    'name':input("Enter your name.").strip().lower(),
                    'bal':int(input("Enter your opening balance.")) ,
                    'password': getpass("Enter your password.")
                }
            db[str(acc_no)]=new_user
            db.close()
            print("your accound is succesfully added.")
            m = time.ctime()+":"+" Sign up : "+str(acc_no)+" \n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            os.system("cls")
            main_menu()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
    
def Exit():
    print("Thanks for using our services.")
def admin():
    try:
        exits_password="mai hun don"
        password=getpass("Enter yous password admin : ")
        if exits_password==password:
            print("1.Reset password\n2.Delete Account \n3. Account details\n4main_menu")
            ch=int(input("Enter your choice : "))
            if ch==1:
                os.system("cls")
                reset_password()
            elif ch==2:
                os.system("cls")
                delete_account()
            elif ch==3:
                os.system("cls")
                account_details()
            elif ch==4:
                os.system("cls")
                main_menu()
            else:
                print("Invalid choice.")
                time.sleep(4)
                os.system("cls")
                admin()
        else:
            print("Incorrect Password")
            print("Try again .")
            m = time.ctime()+":"+" admin "+" try to login "+"\n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            os.system("cls")
            main_menu()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
        
def reset_password():
    try:
        acc_no=input("Enter account number ").strip()
        password=input("Enter the new password ")
        password_2=input("Enter the new password again .")
        if password==password_2:
            db = shelve.open('Bank/bank.db',writeback=True)
            db[acc_no]["password"]=password
            db.close()
            print("User's password succesfully change.")
            time.sleep(4)
            m=time.ctime()+":"+" Admin reset the password of account "+acc_no+" password is "+password+"\n"
            f=open("log.txt","a")
            f.write(m)
            f.close()
            os.system("cls")
            main_menu()
        else:
            print("Password does not match\n Please try again !")
            time.sleep(4)
            os.system("cls")
            admin()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
def delete_account():
    try:
        acc_no=input("Enter account number which you want to delete.").strip()
        db = shelve.open('Bank/bank.db',writeback=True)
        del db[acc_no]
        print("Account is deleted")
        db.close()
        m=time.ctime()+":"+" Admin deleted an account "+" number is "+acc_no+"\n"
        time.sleep(4)
        os.system("cls")
        main_menu()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
def account_details():
    try:
        db = shelve.open('Bank/bank.db',writeback=True)
        account=int(input("Enter the account Number "))
        data=list(map(int,db.keys()))
        print(data)
        if account in data:
            details=db[str(account)]
            print(details)
            db.close()
            time.sleep(4)
            os.system("cls")
            admin()
        else:
            print("Account is not present")
            time.sleep(4)
            os.system("cls")
            account_details()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
    
def info():
    details="Welcome to Bank Management System".center(510,"*")
    print(details)
    print("Created by - Afzal Ali")
    time.sleep(4)
    os.system("cls")
info()
main_menu()


# #### 
