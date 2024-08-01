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
        process_coins(Coffee)



        Water_Level -= water_amount
        Milk_Level -= milk_amount
        Coffee_Level -= coffee_amount

        if Water_Level < 0 or Milk_Level < 0 or Coffee_Level < 0:
            print("Sorry, there is not enough resources.")
            # Rollback resource levels if any of them go negative
            Water_Level += water_amount
            Milk_Level += milk_amount
            Coffee_Level += coffee_amount
            return False

        print(f"Your selection: {Coffee}")
        print(report_Machine())
      
        return True
    else:
        print("Unavailable")
        return False


User_input = input("")


def Off():
    if User_input == "off":
        return False
    return True


def report_Machine():
    print(f"Water level: {Water_Level}")
    print(f"Milk level: {Milk_Level}")
    print(f"Coffee level: {Coffee_Level}")


def process_coins(coffee):
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    dollar = 1.00
    coins = 0

    coin_values = {
        "quarter": quarter,
        "dime": dime,
        "nickel": nickel,
        "penny": penny,
        "dollar": dollar
    }
    cost_coffee = MENU[coffee]["cost"]
    print(f"Cost of {coffee}: {cost_coffee:.2f}")

    while True:
        insert = input("Insert coins (quarter/dime/nickel/penny/dollar) or type 'done' to finish: ").lower()
        if insert == "done":
            break
        elif insert in coin_values:
            coins += coin_values[insert]
            print(f"Added {coin_values[insert]:.2f}, total: {coins:.2f}")
        else:
            print("Invalid input, please try again.")
    
    
    
    while coins < cost_coffee:
        print(f"Insufficient funds. Insert additional coins to reach {cost_coffee:.2f}.")
        insert = input("Insert coins (quarter/dime/nickel/penny/dollar) or type 'done' to finish: ").lower()
        if insert == "done":
            break
        elif insert in coin_values:
            coins += coin_values[insert]
            print(f"Added {coin_values[insert]:.2f}, total: {coins:.2f}")
        else:
            print("Invalid input, please try again.")
    
    if coins >= cost_coffee:
        print(f"Enough funds provided: {coins:.2f}. Enjoy your coffee!")
   
    else:
        print(f"Transaction canceled. Total coins inserted: {coins:.2f}.")
    
    return coins

    



if __name__ == "__main__":
    Water_Level = Machine.get("water")
    water_amount = MENU["latte"]["ingredients"]["water"]
    print(water_amount)
   
    print("Cofee Machine")
    # print(Machine.get("water"))


    while Off():
        User_input = input("What would you like? (espresso/latte/cappuccino):")
        while User_input == "report":
            print(report_Machine())
            User_input = input("What would you like? (espresso/latte/cappuccino):")
        Coffee_Selection(User_input)
     
      
       









