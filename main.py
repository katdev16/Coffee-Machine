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

Water_Level = 500
Milk_Level = 500
Coffee_Level = 500


Machine={
    "water": Water_Level,
    "milk": Milk_Level,
    "coffee": Coffee_Level
}

def Coffee_Selection(Coffee):
    global Water_Level
    global Milk_Level
    global Coffee_Level

    if Coffee in MENU:
        
        
        water_amount = MENU[Coffee]["ingredients"]["water"]
        milk_amount = MENU[Coffee]["ingredients"]["milk"]
        coffee_amount = MENU[Coffee]["ingredients"]["coffee"]

        Water_Level-=water_amount
        print(f"Water level: {Water_Level}")


        if Water_Level < 0 or Milk_Level < 0  or Coffee_Level < 0:
            return "Sorry there is not enough water."
            
        
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


if __name__ == "__main__":
  
    Water_Level = Machine.get("water")
    water_amount = MENU["latte"]["ingredients"]["water"]
    print(water_amount)
   
    print("Cofee Machine")
    # print(Machine.get("water"))


    while Off():
        User_input = input("What would you like? (espresso/latte/cappuccino):")
        while User_input == "report":
            print(report())
            User_input = input("What would you like? (espresso/latte/cappuccino):")

        
        print(Coffee_Selection(User_input))






