# Dictionary of shop items
shop_items = {"Smartphone": 120, "Headphones": 50, "Charger": 20}

# Customer's available money
customer_balance = 100

# Counter for number of tries
purchase_attempts = 0

class PurchaseError(Exception):
    pass

def show_items():
    print("\nWelcome to our shop! Here are the available items:")
    for item, price in shop_items.items():
        print(f"{item}: £{price}")
    print("Type the name of the item you want to buy or 'exit' to leave the shop.")

while True:
    show_items()
    choice = input("\nWhat would you like to buy? ")

    try:
        if choice.lower() == 'exit':
            print("Thank you for visiting our shop. Have a nice day!")
            break

        elif choice not in shop_items:
            raise ValueError

        elif shop_items[choice] > customer_balance:
            print(f"You can't afford {choice}. It costs £{shop_items[choice]} and you have only £{customer_balance}")
            more_money = input("Do you have more money to add to your balance? (yes/no) ")

            if more_money.lower() == 'yes':
                added_money = float(input("How much do you want to add? "))
                customer_balance += added_money
                print(f"You have now £{customer_balance}.")

        elif shop_items[choice] <= customer_balance:
            customer_balance -= shop_items[choice]
            print(f"Here's your {choice}! You have £{customer_balance} left.")
            break

        purchase_attempts += 1

        if purchase_attempts >= 3:
            raise PurchaseError("Too many unsuccessful purchase attempts. You are asked to leave the shop.")

    except ValueError:
        print("Invalid input. Please type the exact name of the item or 'exit'.")

    except PurchaseError as e:
        print(str(e))
        break

