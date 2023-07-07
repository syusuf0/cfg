# Shop items
shop_items = {"laptop": 190, "charger": 50, "laptop case": 20}

# Customer's money
customer_balance = 100

# no of tries
purchase_attempts = 0

class PurchaseError(Exception):
    pass

def show_items():
    print("\nWelcome to Tech shop! This is a catalogue of available items:")
    for item, price in shop_items.items():
        print(f"{item}: £{price}")
    print("Enter the name of the product you wish to purchase or 'quit' to leave the shop.")

while True:
    show_items()
    choice = input("\nWhat would you like to purchase? ")

    try:
        if choice.lower() == 'exit':
            print("Thank you for browsing. Enjoy your day!")
            break

        elif choice not in shop_items:
            raise ValueError

        elif shop_items[choice] > customer_balance:
            print(f"You do not have sufficient balance for {choice}. The amount is £{shop_items[choice]} and your balance £{customer_balance}")
            more_money = input("Can you add money to your balance? (yes/no) ")

            if more_money.lower() == 'yes':
                added_money = float(input("How much do you want to add? "))
                customer_balance += added_money
                print(f"You now have £{customer_balance}.")

        elif shop_items[choice] <= customer_balance:
            customer_balance -= shop_items[choice]
            print(f"Here's your {choice}! You have £{customer_balance} left.")
            break

        purchase_attempts += 1

        if purchase_attempts >= 3:
            raise PurchaseError("Error! Too many unsuccessful attempts. Please leave the shop.")

    except ValueError:
        print("Invalid input. Please enter the name of the item or 'quit'.")

    except PurchaseError as e:
        print(str(e))
        break