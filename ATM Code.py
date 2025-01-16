import time
print("Please insert your ATM card")
time.sleep(5)
password = 1234
pin = int(input("Please enter your PIN: "))
balance = 5000
if pin == password:
    while True:
        print("""
              1 == Balance inquiry
              2 == Cash Withdrawal
              3 == Cash Deposit
              4 == Exit
              """)
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter valid choice")
        if option == 1:
            print(f"Your current balance is ${balance}")
        if option == 2:
            withdrawal_amount = int(input("Enter your withdrawal amount: "))
            balance = balance - withdrawal_amount
            print(f"${withdrawal_amount} has been debited from your account!")
            print(f"Your updated balance is {balance}")
        if option == 3:
            deposit_amount = int(input("Please enter your deposit amount: "))
            balance = balance + deposit_amount
            print(f"${deposit_amount} has been credited to your account!")
            print(f"Your updated balance is {balance}")
        if option == 4:
            break
else:
    print("Invalid PIN. Please try again")