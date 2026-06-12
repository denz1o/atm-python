pin = int(input('Enter pin'))

while pin != 1234:
    print('Wrong pin!')
    pin = int(input('Enter the pin'))

print('Access given')
print()
total_balance = 10000

while True:
 print('\nCurrent balance', total_balance,'$')
 
 choice = input("What would you like to do today?\n" 
               '"H" to view transaction histroy\n'
               '"D" to deposit money\n'
               '"C" to credit moeny\n' \
               '"Q" to quit\n'
               'Enter:\n').upper()

 if choice == 'H':
 
    print('1/3/2026 - +$1000\n'
          '2/3/2026 - +$300\n'
          '6/3/2026 - +$500\n'
          '7/3/2026 - -$100\n'
    )

 elif choice == 'D':
    deposit = int(input('Enter Amount:'))
    total_balance += deposit
    print('Deposited:', deposit, '$','\n''current balance:', total_balance, '$')

 elif choice == 'C':
    credit = int(input('Enter Withdrawel amount:'))
    
    if credit > total_balance:
        print('Insufficient ammount')
    else:
     total_balance -= credit
     print('Credited:', credit,'$', '\n''remaining', total_balance,'$')


 if choice == 'Q':
   print('See you again!')
   break
   