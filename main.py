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
    "cappuccion": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 1000,
    "milk": 800,
    "coffee": 650,
}


def is_ingredients_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry,there is not enough {item}")
            return False
    return True


def coins_taken():
    print("insert your coins")
    total = int(input("how many peeny: ")) * 0.01
    total += int(input("how many dime: ")) * 0.10
    total += int(input("how many nickel: ")) * 0.05
    total += int(input("how many quarter: ")) * 0.25
    return total


def transcation_successful(pay_ment, drink_cost):
    if pay_ment >= drink_cost:
        change = round(pay_ment - drink_cost, 2)
        print(f"here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money,money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"and here is your  {drink_name} ☕ , have a nice day🖤🖤\nVISIT AGAIN, MAIEKL'S COFFEE SHOP✯✯✯")


print("WELCOME TO MAIKEL'S COFFEE SHOP✯✯✯")
print('''

                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' 
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'


''')
is_on = True
while is_on:
    choice = input("what do you like to drink? espresso/latte/cappuccion: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"profit:${profit}")
    else:
        drink = MENU[choice]
        drink2 = drink["cost"]
        print(f"{choice} cost is ${drink2} ")
        if is_ingredients_sufficient(drink["ingredients"]):
            payment = coins_taken()
            if transcation_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])