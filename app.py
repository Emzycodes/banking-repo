from main import BankAccount

account_name = ""
account_type = ""
account_number = ""

def user_app():
# user public account details
    account_name = input('What is your fullname:   ')
    print ('\n')
    account_type = input('savings or current? :   ')
    print ('\n')
    account_number = int(input('fill in your acct number:   \n'))
    print('\n')
    if account_name and account_type and account_number:
        print("Login sucessfully")
    else: 
        account_name and account_type and account_number == ''
        print ("Incorrect login credential..")
        
print ("LOGIN TO START\n ")
user_input = input("press any button to login :  ")
if user_input:
    user_app()

#bank as a instance of BankAccount Class
bank = BankAccount(account_name,account_type,account_number)#user public acct details as parameters


