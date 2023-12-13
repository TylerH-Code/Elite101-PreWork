class Products:

  def __init__(self, id, name, price):
    self.id = str(id)
    self.name = name
    self.price = price

  def print_name(self):

    print(self.id + ": " + self.name)

  def print_price(self):
    print(self.id + ": " + str(self.price))


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
    print(self.name)

  def print_address(self):
    print(self.address)

  def print_hours(self):
    print(self.hours)

  def show_ui(self):
    next = False
    while next is False:
      print("1")
      print("2")
      print("3")
      print("4")
      print("5")
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

  def show_product_ui(self):
    next = False
    while next is False:
      print("1")
      print("2")
      print("3")
      choice = input()
      if (choice == "1"):
        for i in range(len(inventory)):
          inventory[i].print_name()
      elif (choice == "2"):
        for i in range(len(inventory)):
          inventory[i].print_price()
      elif (choice == "3"):
        break
