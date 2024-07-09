import csv
import os
import time
import getpass
# Hello! How are you?

def read_db():
    try:
        with open("account_info.csv", "r") as fileobj:
            account_info = next(csv.DictReader(fileobj))
            for key, value in account_info.items():
                account_info[key] = float(account_info[key])
            return account_info
    except FileNotFoundError as e:
        print(e)
        time.sleep(1)
        quit()


def write_db(user_info: dict):
    with open("account_info.csv", "w", newline="") as fileobj:
        print(user_info)
        writer = csv.DictWriter(fileobj, fieldnames=user_info.keys())
        writer.writeheader()
        writer.writerow(user_info)


def withdraw():
    user = read_db()
    choice = input("[1].Checking\n[2].Savings\n>>>: ")
    try:
        if choice == "1":
            amount = float(input("How much would you like to withdraw?: "))
            if amount <= user["checking"]:
                user["checking"] = user["checking"] - amount
                write_db(user)
            else:
                print("Insufficient Funds")
        if choice == "2":
            amount = float(input("How much would you like to withdraw? "))
            if amount <= user["savings"]:
                user["savings"] = user["savings"] - amount
                write_db(user)
            else:
                print("Insufficient Funds")
    except ValueError as e:
        print(e)
        print(f"Not a number")
        time.sleep(2)
        os.system("cls")


def deposit():
    user = read_db()
    choice = input("[1].Checking\n[2].Savings\n>>>: ")
    try:
        if choice == "1":
            amount = float(input("How much would you like to deposit?: "))
            if amount <= user["checking"]:
                user["checking"] = user["checking"] + amount
                write_db(user)
            else:
                print("Insufficient Funds")
        if choice == "2":
            amount = float(input("How much would you like to deposit? "))
            if amount <= user["savings"]:
                user["savings"] = user["savings"] + amount
                write_db(user)
            else:
                print("Insufficient Funds")
    except ValueError as e:
        print(e)
        print(f"Not a number")
        time.sleep(2)
        os.system("cls")


def show_balance():
    user = read_db()
    print(f"Your checking has ${user["checking"]:,.2f}")
    print(f"Your savings has ${user["savings"]:,.2f}")


def transfer():
    user = read_db()
    choice = input("Transfer to\n [1].Checking\n[2].Savings\n>>>: ")
    try:
        if choice == "1":
            amount = float(input("How much would you like to transfer? "))
            if amount <= user["savings"]:
                user["savings"] = user["savings"] - amount
                user["checking"] = user["checking"] + amount
                write_db(user)
            else:
                print("Insufficient Funds")
        if choice == "2":
            amount = float(input("How much would you like to transfer? "))
            if amount <= user["checking"]:
                user["savings"] = user["savings"] + amount
                user["checking"] = user["checking"] - amount
                write_db(user)
            else:
                print("Insufficient Funds")
    except ValueError as e:
        print(e)
        print(f"Not a number")
        time.sleep(2)


def main(attempts=0):
    if attempts < 4:
        print("Chase ATM")

        user = read_db()
        pin = getpass.getpass("Please enter your pin: ")

        if float(pin) == user["pin"]:
            print("Login Successful\n")
            for _ in range(12):
                os.system("cls")
                selection = input("[1].Withdraw\n[2].Deposit\n[3].Transfer\n[4].Balance\n[5].Quit\n>>>: ")
                if selection == "1":
                    withdraw()
                elif selection == "2":
                    deposit()
                elif selection == "3":
                    transfer()
                elif selection == "4":
                    show_balance()
                elif selection == "5":
                    quit()

        else:
            print("Login Failed")
            time.sleep(1)
            os.system("cls")
            main(attempts+1)
    return quit()


main()



