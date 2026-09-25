#Write a Python program to create a simple ATM system.
#The user starts with an initial balance of ₹10,000.
#Display the following menu:
#===== ATM MENU =====
#1. Check Balance
#2. Deposit
#3. Withdraw
#4. Exit
#Ask the user to enter their choice.
#Use if-elif-else to perform the following operations:
#Check Balance
#Display the current account balance.
#Deposit
#Ask the user to enter the deposit amount.
#Add the amount to the balance.
#Display the updated balance.
#Withdraw
#Ask the user to enter the withdrawal amount.
#Check whether the withdrawal amount is less than or equal to the available balance.
#If sufficient balance is available, deduct the amount and display the remaining balance.
#Otherwise, display "Insufficient Balance".
#Exit
#Display "Thank you for using the ATM".
#If the user enters any other choice:
#Display "Invalid Choice".

balance=10000

print("======================ATM MENU===================")
print(f"1.Check Balance \n2.Deposit \n3.Withdraw \n4.Exit")

choice=input("Enter your choice: ")

if choice=="1":
    print(f"Your current account balance is {balance}")

elif choice=="2":
    deposit_amount=int(input("enter the deposit amount: "))
    balance=deposit_amount+balance
    print(f"Your updated balance is {balance}")

elif choice=="3":
    withdrawl_amount=int(input("Enter your withdrawl amount: "))
    if withdrawl_amount<=balance:
        balance=balance-withdrawl_amount
        print(f"Your updated balance is {balance}")
    else:
        print("Sorry, you have insufficient balance")
        
elif choice=="4":
    print("Thank you for using the ATM")
else:
    print("Invalid choice")

