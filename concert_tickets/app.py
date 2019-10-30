from datetime import datetime
import json

# additional imports if needed

# global variables
SHOWS_FILE = "./shows.json"
TRANSACTIONS_FILE = "./transactions.txt"
TICKET_FILE = "./ticket.txt"
SALES_TAX = 0.07  # 7% Sales Tax


def get_menu():
    with open(SHOWS_FILE) as menu:
        return json.load(menu)


def show_menu(collection):
    for element in collection:
        dots = 18 - len(element["artist"])
        print(f'{element["artist"]}{dots * "."}${element["price"]:.2f}')


def make_choice(collection):
    valid_options = []
    for item in collection:
        valid_options.append(item.get("artist"))
    while True:
        choice = input("Choice: ")
        if choice in valid_options:
            return choice


def ticket_update(collection, choice):
    with open(SHOWS_FILE, "r") as files:
        json.load(files)

    with open(SHOWS_FILE, "a") as file:
        # ticket = int(input("How many tickets did you get: "))
        for item in collection:
            if item.get("artist") == choice:
                item["tickets"]
                if item["tickets"] == "SOLD OUT":
                    print("Sold Out")
                    make_choice(collection)
                # else:
                #     del item["tickets"]
                #     item.update("tickets" + (-ticket))


def get_price(collection, choice):
    for item in collection:
        if item.get("artist") == choice:
            return item.get("price")


def get_code(collection, choice):
    for item in collection:
        if item.get("artist") == choice:
            return item.get("code")


def save_file(choice, price, code):
    name = input("First and Last Name: ")
    tickets = int(input("How many tickets did you get: "))
    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(
            f"\n{name}, {choice}, {code}, {tickets}, {'$'}{price * tickets}, {'$'}{(SALES_TAX * tickets)}, {datetime.now()}"
        )


def main():
    print("Welcome to The Jefferson venue ticket purchasing tool!")
    data = get_menu()
    show_menu(data)
    choice = make_choice(data)
    tickets = int(input("How many tickets: "))
    price = get_price(data, choice)
    code = get_code(data, choice)
    ticket_amount = ticket_update(data, choice)
    total = (SALES_TAX + price) * tickets
    print(
        "{} tickets for {} coming up! That will be ${:.2f}".format(
            tickets, choice, total
        )
    )
    save_file(choice, price, code)
    print("Have a good day.")


if __name__ == "__main__":
    main()
