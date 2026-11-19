products = {
    "laptop": {
        "price": 800,
        "stock": 3
    },
    "phone": {
        "price": 500,
        "stock": 5
    },
    "headphones": {
        "price": 100,
        "stock": 10
    }
}

profit = 0

def make_report(resources):
    for product in resources:
        print(f"{product}: {resources[product]['stock']}")
    print(f"Money: {profit}")

while True:
    choice = input("What would you like? laptop/phone/headphones: \n").lower()

    if choice in products:
        quantity = int(input("How many? \n"))
        product = products[choice]

        if quantity <= product["stock"]:
            price = product["price"] * quantity
            print(f"Total: {price}")

            money = int(input("How much did you pay? "))

            if money >= price:
                profit += price
                product["stock"] -= quantity

                change = money - price

                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
                print("Purchase sucessful! ")
            else:
                print("Money Refunded Not up to price")
        else:
             print(f"Inadequate {choice} stock in store")

    elif choice == "report":
            make_report(products)
    else:
            break
