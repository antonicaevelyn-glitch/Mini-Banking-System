accounts = {}
def create_account():
    name = input("Enter Account Holder Name: ")
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists!")
    else:
        accounts[acc_no] = {"name": name, "balance": 0}
        print("Account created successfully!")

def deposit():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Amount deposited successfully!")
    else:
        print("Account not found!")

def withdraw():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Current Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found!")

while True:
    print("\n--- Mini Banking System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thank you for using Banking System!")
        break
    else:
        print("Invalid choice!")


        