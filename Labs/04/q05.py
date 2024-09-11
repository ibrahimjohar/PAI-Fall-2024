#name: ibrahim johar farooqi
#date: 11 september 2024
#lab: 04
#task: 5

class Restaurant:
    menu_items = {}
    book_table = []
    customer_orders = []

    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []
    
    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_num):
        self.book_table.append(table_num)
    
    def customer_order(self, order):
        self.customer_orders.append(order)
    
    def print_menu(self):
        print("menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")
    
    def print_table_reservations(self):
        print("table reservations:")
        for table in self.book_table:
            print(f"table {table}")

    def print_customer_orders(self):
        print("customer orders:")
        for order in self.customer_orders:
            print(order)
    
restaurant1 = Restaurant()

restaurant1.add_item_to_menu("pizza", 5.99)
restaurant1.add_item_to_menu("pasta", 2.33)
restaurant1.add_item_to_menu("burger", 4.99)
restaurant1.add_item_to_menu("steak", 10.99)

restaurant1.book_tables(1)
restaurant1.book_tables(2)

restaurant1.customer_order("order 1: pizza and pasta")
restaurant1.customer_order("order 2: burger and steak")

restaurant1.print_menu()
print("\n")
restaurant1.print_table_reservations()
print("\n")
restaurant1.print_customer_orders()