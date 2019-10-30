from datetime import datetime
import json

# additional imports if needed

# global variables
SHOWS_FILE = "./shows.json"
TRANSACTIONS_FILE = "./transactions.txt"
TICKET_FILE = "./ticket.txt"
SALES_TAX = 0.07  # 7% Sales Tax


def pick_show():
    with open(SHOWS_FILE, "r") as file:
        ticket = input("What show: ")
        for ticket in collection:
            print(ticket["artist"])
            for show in collection:
                print([show])
        json.load(file)


def sell():
    with open(SHOWS_FILE, "r") as file:
        json.load(file)

    for show in collection:
        for show["tickets"] in show:
            print(show["price"])


def transaction():
    with open(SHOWS_FILE) as file:
        quantity = int(input("How many: "))
        for choice in collection:
            for tickets in choice:
                if tickets != 0:
                    ticket -= 1
                elif choice["tickets"] == "SOLD OUT":
                    print("Sold Out")
                elif quantity > choice["tickets"]:
                    print(choice["tickets"])
                else:
                    print("Sold out!!")
        json.load(file)


def main():
    print("Welcome to The Jefferson venue ticket purchasing tool!")
    # this is where the code you write goes
    pick_show()
    sell()
    transaction()


if __name__ == "__main__":
    main()
