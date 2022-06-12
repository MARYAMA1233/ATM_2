# This is a working step while withdrawing money

Name = input('enter your name please : ')
print("you are welcome", Name, "please kindly input your pin to proceed ")

while True:

    pin = input('Please enter your 4 digit pin!')
    if len(pin) < 4:
        print("your pin must be four digits ")
    elif len(pin) > 4:
        print('Your pin is four digit', Name)
    else:
        transaction = input('Withdrawal, Check balance, Pay Bill or Transfer')
        if transaction == 'Withdrawal':
            input("savings or current?: ")
            amount = input('enter your desired amount ')
            print("take your cash ....")

        elif transaction == 'Check balance':
            print(f'Your balance on the account number: XXXXXXXXXXX is .....')

        elif transaction == 'Pay Bill':
            input('Select bill to pay: water bill, electricity bill and food bill ')
            print('Bill paid successfully!')

        else:
            Account_number = input('enter the beneficiary account number ')
            amount = input("enter your desired amount: ")
            bank_type = input('''
            select your bank ...
            1. Taj Bank
            First Bank
            Gt Bank
            Polaris
            Access Bank
            Union
            Unity
            Diamond  
            ''')
            confirmation = input('Do you really wish to send  this amount to the account number? Yes/ No:')
            if confirmation.lower() == 'yes':
                print('transfer successful!')

            else:
                print('Transaction failed!')
        print('take your card')
