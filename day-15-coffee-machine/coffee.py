from menu import MENU
def money():
    print("please insert coins.")
    try:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        return (0.25 *  quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    except ValueError:
        print("enter a number")
        return 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def make_report(ing):
    return (
        f"Water: {ing['water']}ml\n"
        f"Milk: {ing['milk']}ml\n"
        f"Coffee: {ing['coffee']}g\n"
        f"Money: ${profit:.2f}"
    )

def check_resources(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


while True:
    choice = input("what would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        break
    elif choice == "report":
        print(make_report(resources))
    elif choice in MENU:
        maker = MENU[choice]
        if(check_resources(maker["ingredients"])):
            currency = money()
            if maker["cost"] <= currency:
                change = currency - maker["cost"]
                profit += maker["cost"]
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {choice} Enjoy!!")

                for item in maker["ingredients"]:
                    resources[item] -= maker["ingredients"][item]
            else:
                if currency > 0:
                    print("Sorry, that's not enough money. Money refunded.")
    else:
         print("Enter a valid option!!")
