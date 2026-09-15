import os

print("Welcome to the Python Bank")

balance = 10000
pin = 1234
attempt = 0

while attempt != 3:
    try:
        password = int(input("Enter your PIN: "))
        attempt += 1

        if password == pin:
            break
        else:
            print("Incorrect PIN. Enter again.")

    except ValueError:
        print("PIN must contain numbers only.")

else:
    print("Too many incorrect attempts.")
    print("Your account is locked.")
    exit()


def init():
    print("""
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Exit
""")




def check_balance():
    print(f"Your balance is {balance}")
    return balance


def deposit():
    try:
        deposit_amount = int(input("Enter amount to deposit: "))

        if deposit_amount > 0:
            return balance + deposit_amount
        else:
            print("Amount must be greater than 0.")
            return balance

    except ValueError:
        print("Enter a valid number.")
        return balance


def withdraw():
    try:
        withdraw_amount = int(input("Enter money to withdraw: "))

        if withdraw_amount <= 0:
            print("Amount must be greater than 0.")
            return balance

        if withdraw_amount > balance:
            print("Insufficient Funds.")
            print(f"Your Balance is {balance}")
            return balance

        return balance - withdraw_amount

    except ValueError:
        print("Enter a valid number.")
        return balance


def transfer():
    try:
        transfer_account = int(input("Enter account number: "))
        amount = int(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return balance

        if amount > balance:
            print("Insufficient Funds.")
            print(f"Your Balance is {balance}")
            return balance

        print(f"Successfully transferred {amount} to account {transfer_account}.")
        return balance - amount

    except ValueError:
        print("Enter valid numbers.")
        return balance


setting = {
    1: check_balance,
    2: deposit,
    3: withdraw,
    4: transfer
}


while password == pin:
    init()

    try:
        option = int(input("Choose an option: "))

        if option == 5:
            print("Thank you for using Python Bank.")
            break

        if option in setting:
            balance = setting[option]()
        else:
            print("Enter a valid option.")
        input("Press Enter to continue...")
        os.system("cls")

    except ValueError:
        print("Enter a number.")
