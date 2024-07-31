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
        Coffee_Level-=coffee_amount
        print(f"Water level: {Water_Level}")


        if Water_Level < 0 or Milk_Level < 0  or Coffee_Level < 0:
            print("Sorry there is not enough water.")
            return False
        print(f"Your selection: {Coffee}")
        return True
    else:
        print("Unavailable")
        return False
    
    


User_input = input("")


def Off():
    if User_input == "off":
        return False
    return True


def report():
    if User_input == "report":
        return MENU.get("espresso")
    
def process_coins():
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    pennie = 0.01
    coins = 0

    User_input = input("Insert coins(quarter/dime/ nickle/pennie): ")
    while User_input not in ["quarter","dime","nickle","pennie"]:
        print("1st")
        User_input = input("Insert coins(quarter/dime/ nickle/pennie): ")
        coins+=quarter
        print(coins)
    
    cost_coffee = MENU["latte"]["cost"]
    print(cost_coffee)
    while cost_coffee > coins:
        print("2nd")
        
        User_input = input("Insert coins(quarter/dime/ nickle/pennie): ")
        coins+=quarter
        print(coins)
    return "added"

    



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
        Coffee_Selection(User_input)
        
        process_coins()






