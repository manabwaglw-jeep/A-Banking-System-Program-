def show_balance(balance):
    print (f"You have ${balance} on your account!")

def deposit( balance):
    amount = float(input("Enter the amount to deposit: $"))
    if amount >0:
     balance += amount
     print(f" ${balance} has been deposited")
    else:
        print("Invalid amount ! Please enter a positive number")
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw : $"))
    if amount > balance:
        print(f"{balance} Insufficient Funds ")
    elif amount <= 0:
        print("Invalid number ! Please enter  a posivite number:")
    else:
        balance -= amount    
        print(f" ${amount} has been withdrawn")
    return balance   
    