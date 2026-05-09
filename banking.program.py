# python banking program


from banking_head import * 
balance=0
is_running=True
while is_running:
    print ("____BANKNG PROGRAM___")
    print("Enter 1 for show balance:")
    print ("Enter 2 for withdraw:")
    print("Enter 3 for deposit:")
    print("Enter 4 exit:")
    
    choice = input("enter your choice(1-4:)")
    if choice == '1':
     balance=show_balance(balance)
    elif choice == '2':
     balance=withdraw(balance)
     
    elif choice == '3':
     balance=deposit(balance)
     
    elif choice == '4':
     break
    else:
        print("Invalid Input")
        
print("Thank you! have a nice day!")
