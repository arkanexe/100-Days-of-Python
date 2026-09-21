# import turtle
# timmy = turtle.Turtle()

# print(timmy)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# timmy.shape("square")
# turtle.forward(100)

# my_screen.exitonclick()

# pypi.org  --- python packages docs
# import prettytable


# from prettytable import PrettyTable


# table = PrettyTable()
# table.title = "Table Extraction"
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# table.align["Pokemon Name"] = "l"
# print(table)
# print(table.align)


# with open("welcome.txt", "w") as file:
#     file.write("Hello Welcome to Goose")


# class MenuItem:
#     def __init__(self, name, water, milk, coffee, cost):
#         self.name = name
#         self.cost = cost
#         self.ingredients = {
#             "water": water,
#             "coffee": coffee,
#             "milk": milk
#         }


# class Menu:
#     def __init__(self):
#         self.menu = [
#             MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
#             MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
#             MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
#         ]

#     def get_items(self):
#         option = ""
#         for item in self.menu:
#             option += f" {item.name}/"
#         return option
#     def find_drink (self, order_name):
#         for item in self.menu:
#             if item.name.lower() == order_name.lower():
#                 return item
#         print("Sorry that item is not available.")

# menu = Menu()


# class coffeeMaker:
#     def __init__(self):
#         self.resources = {
#             "water": 300,
#             "milk": 200,
#             "coffee": 100
#         }
#     def report(self):
#         print(f"Water: {self.resources['water']}ml")
#         print(f"Milk: {self.resources["milk"]}ml")
#         print(f"Coffee: {self.resources["coffee"]}g")

#     def is_resources_sufficient(self, drink):
#         can_make = True
#         for item in drink.ingredients:
#             if drink.ingredients[item] >= self.resources[item]:
#                 print(f"Sorry there was no insuffiecient {item}")
#                 can_make = False
#         return can_make

#     def make_coffee(self, drink):
#         for item in drink.ingredients:
#             self.resources[item] -= drink.ingredients[item]
#         print(f"Here is your {drink.name} enjoy!!")

# class MoneyMachine:

#     CURRENCY = "$"
#     COIN_VALUES = {
#         "quarters": 0.25,
#         "dimes": 0.10,
#         "nickles": 0.05,
#         "pennies": 0.01
#     }

#     def __init__(self):
#         self.profit = 0
#         self.money_recieved = 0

#     def report(self):
#         print(f"Money: {self.CURRENCY}{self.profit}")
#     def process_coins(self):
#         for values in self.COIN_VALUES:
#             self.money_recieved += int(input(f"How many {values}? ")) * self.COIN_VALUES[values]

#         return self.money_recieved
#     def make_payment(self, cost):
#         self.process_coins()
#         if self.money_recieved >= cost:
#             self.profit += cost
#             change = self.money_recieved - self.profit

#             if change > 0:
#                 print(f"Here is your {change}")

#             self.money_recieved = 0
#             return True
#         else:
#             print("You Have been refunded!!")
#             self.money_recieved = 0

#             return False


# menu = Menu()
# coffee_maker = coffeeMaker()
# money_machine = MoneyMachine()

# is_on = True

# while is_on:
#     choice = input(f"What drink do you want {menu.get_items()}")

#     if choice == "off":
#         break
#     elif choice == "report":
#         print(coffee_maker.report())
#     else:
#         drink = menu.find_drink(choice)

#         if coffee_maker.is_resources_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
#         else:
#             print(f"Not")


# Library System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
        else:
            print(f"{self.title} has been borrowed. ")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.title} has been returned. ")
        else:
            print(f"{self.title} has been avialable. ")


class Library:
    def __init__(self):
        self.books = [
            Book(title = "Islam is My Religion", author = "Ayanbisi Abdulrahman"),
            Book(title = "We are the Legacy", author="Roheemah"),
            Book(author="Harry Porter", title ="Legacy")
        ]
    def show_books(self):
        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author} - Available")
            else:
                print(f"{book.title} by {book.author} - Borrowed")
    def find_book(self, title):
        for book in self.books:
            if title == book.title:
                return book


library = Library()
is_open = True
while is_open:
    operation = input("What action ?").lower()

    if operation == "off":
        is_open = False
    elif operation == "show":
        library.show_books()
    elif operation == "borrow":
        book_borrow = input("Which book do you want to borrow? ")

        book = library.find_book(book_borrow)

        if book is None:
            print(f"{book_borrow} not available")
        else:
            book.borrow()
    elif operation == "return":
        book_borrow = input("Which book do you want to return? ")

        book = library.find_book(book_borrow)
        if book is None:
            print(f"{book_borrow} not available")
        else:
            book.return_book()
