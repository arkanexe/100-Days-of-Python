# import turtle
# timmy = turtle.Turtle()

# print(timmy)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# timmy.shape("square")
# turtle.forward(100)

# my_screen.exitonclick()

# pypi.org  --- python packages docs
import prettytable


from prettytable import PrettyTable


table = PrettyTable()
table.title = "Table Extraction"
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align["Pokemon Name"] = "l"
print(table)
print(table.align)


# with open("welcome.txt", "w") as file:
#     file.write("Hello Welcome to Goose")


class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "coffee": coffee,
            "milk": milk
        }

latte = MenuItem()


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        option = ""
        for item in self.menu:
            option += f"{item.name}"
        return option
    def find_drink (self, order_name):
        for item in self.menu:
            if item.name == order_name.lower():
                return item
        print("Sorry that item is not available.")

menu = Menu()
print(menu.find_drink("latte"))


class coffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources["milk"]}g")
