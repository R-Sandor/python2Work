#This program demonstrates the BankAccount class.

import BankAccount2

def main ():
    # Get the starting balance.
    start_bal = float(input('Enter your starting balance: '))

    # Create a BankAccount object.
    savings = BankAccount2.BankAccount(start_bal)

    # Deposit the user's paycheck.
    pay = float(input('How much were you paid this week?'))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    # Display the balance.
    print('Your account balance is $', \
          format (savings.get_balance(), ',.2f'), sep='')

    # Get the amount to withdrawl.
    cash = float(input('How much would you like to withdraw?'))
    print ('I will withdraw that from your account.')
    savings.withdrawl(cash)

    # Display the balance.
    print('Your account balance is $', \
    format(savings.get_balance(), ',.2f'), sep= '')
    # Call the main function
main()
                      

