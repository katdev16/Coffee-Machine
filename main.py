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


def Coffee_Selection(Coffee):
    Machine={
    "water": 500,
    "milk": 500,
    "coffee": 500
}
    if Coffee in MENU:
        
        water_amount = MENU[Coffee]["ingredients"]["water"]
        milk_amount = MENU[Coffee]["ingredients"]["milk"]
        coffee_amount = MENU[Coffee]["ingredients"]["coffee"]

        Water_Level = Machine.get("water")
        Milk_Level = Machine.get("milk")
        Coffee_Level = Machine.get("coffee")

        Water_Level-=water_amount
        print(Water_Level)
        milk_amount = Milk_Level-milk_amount
        coffee_amount = Coffee_Level-coffee_amount

        if Water_Level < 0 or Milk_Level < 0  or Coffee_Level < 0:
            print("Sorry there is not enough water.") 
            
        
        return f"Your selection: {Coffee}"
    else:
        return "Unavailable"
    

User_input = input("")


def Off():
    if User_input == "off":
        return False
    return True


def report():
    if User_input == "report":
        return MENU.get("espresso")

Machine={
    "water": 500,
    "milk": 500,
    "coffee": 500
}


if __name__ == "__main__":
   
    print("Cofee Machine")
    print(Machine.get("water"))
    print(MENU["latte"]["ingredients"]["water"])

    while Off():
        User_input = input("What would you like? (espresso/latte/cappuccino):")
        while User_input == "report":
            print(report())
            User_input = input("What would you like? (espresso/latte/cappuccino):")

        
        print(Coffee_Selection(User_input))
        print(Machine.get("water"))


