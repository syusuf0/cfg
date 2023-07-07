class Shop:
    def __init__(self):
        self.items = {"laptop": 190, "charger": 50, "laptop case": 20}
        self.balance = 100
        self.attempts = 0

    def get_item_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            raise ValueError("Error. Item not found.")

    def purchase_item(self, item_name):
        self.attempts += 1
        if self.attempts > 3:
            raise Exception("Maximum tries have been made.")
        price = self.get_item_price(item_name)
        if price > self.balance:
            return False
        self.balance -= price
        return True

    def add_balance(self, amount):
        self.balance += amount

    def exit_shop(self):
        print("Thank you for your purchase!")
class Shop:
    def __init__(self):
        self.items = {"laptop": 190, "charger": 50, "laptop case": 20}
        self.balance = 100
        self.attempts = 0

    def get_item_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            raise ValueError("Invalid input. Item not found.")

    def purchase_item(self, item_name):
        self.attempts += 1
        if self.attempts > 3:
            raise Exception("Maximum attempts reached.")
        price = self.get_item_price(item_name)
        if price > self.balance:
            return False
        self.balance -= price
        return True

    def add_balance(self, amount):
        self.balance += amount

    def exit_shop(self):
        print("Thank you for shopping with us!")


import unittest

class TestShop(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()

    def test_get_item_price_valid_item(self):
        self.assertEqual(self.shop.get_item_price("charger"), 50)

    def test_get_item_price_invalid_item(self):
        with self.assertRaises(ValueError):
            self.shop.get_item_price("invalid_item")

    def test_purchase_item_can_afford(self):
        self.assertTrue(self.shop.purchase_item("laptop case"))  #  can afford the laptop case

    def test_purchase_item_cannot_afford(self):
        self.assertFalse(self.shop.purchase_item("laptop"))  # cannot afford the laptop

    def test_purchase_item_max_attempts(self):
        self.shop.attempts = 3
        with self.assertRaises(Exception):
            self.shop.purchase_item("charger")

    def test_add_balance(self):
        self.shop.add_balance(50)
        self.assertEqual(self.shop.balance, 150)

if __name__ == "__main__":
    unittest.main()
