import clear


class Products:

  def __init__(self, id, name, price):
    self.id = str(id)
    self.name = name
    self.price = price

  def print_name(self):
    print(f"{self.id}  | {self.name}")

  def print_price(self):
    #formating found on https://stackoverflow.com/questions/6149006/how-to-display-a-float-with-two-decimal-places
    print(f"{self.id}  | {str('{:.2f}'.format(self.price))}")


inventory = [
    Products(1, "apple", 5.00),
    Products(2, "banana", 3.00),
    Products(3, "orange", 4.00),
    Products(4, "grape", 2.00),
    Products(5, "watermelon", 6.00),
    Products(6, "strawberry", 4.00)
]


class Store:

  def __init__(self):
    self.name = "Retail Store"
    self.address = "123 Main St"
    self.hours = "5:00AM-9:00PM"
    self.inventory = inventory

  def print_name(self):
    clear.run()
    print(f"\n{self.name}\n")

  def print_address(self):
    clear.run()
    print(f"\n{self.address}\n")

  def print_hours(self):
    clear.run()
    print(f"\n{self.hours}\n")

  def show_ui(self):
    clear.run()
    next = False
    while next is False:
      print("1: show name")
      print("2: show address")
      print("3: show hours")
      print("4: Inventory")
      print("5: Exit")
      choice = input("Enter your choice: ")
      if (choice == "1"):
        self.print_name()
      elif (choice == "2"):
        self.print_address()
      elif (choice == "3"):
        self.print_hours()
      elif (choice == "4"):
        self.show_product_ui()
      elif (choice == "5"):
        break
      else:
        print("Invalid choice")

  def show_product_ui(self):
    clear.run()
    next = False
    while next is False:
      print("Menu for Inventory\n")
      print("1: show products")
      print("2: show prices")
      print("3: exit")
      choice = input("Enter your choice: ")
      if (choice == "1"):
        clear.run()
        print("ID | Product\n---|-------------")
        for i in range(len(inventory)):
          inventory[i].print_name()
        print("")
      elif (choice == "2"):
        clear.run()
        print("ID | Cost\n---|-------------")
        for i in range(len(inventory)):
          inventory[i].print_price()
        print("")
      elif (choice == "3"):
        clear.run()
        break
      else:
        print("Invalid choice")
