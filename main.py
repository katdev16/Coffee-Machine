MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def Coffee_Selection(Coffee):
    if Coffee in MENU:
        return f"Your selection: {Coffee}"
    else:
        return "Unavailable"

def Off():
    if User_input == "off":
        return False
    return True

while Off():
    User_input = input("What would you like? (espresso/latte/cappuccino):")
    print(Coffee_Selection(User_input))

