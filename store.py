import clear


class Products:

  def __init__(self, id, name, price):
    self.id = str(id)
    self.name =str( name)
    self.price =float( price)

  def print_name(self):
    def spaces(num):
      return " " * num
    #formating float of price found on https://stackoverflow.com/questions/6149006/how-to-display-a-float-with-two-decimal-places
    if(len(self.name)<=8):
      self.name+=spaces(8-len(self.name))
    print(f"{self.id}  | {self.name} | {str('{:.2f}'.format(self.price))}")

order=[
  Products(1, "chicken",5.00),
  Products(2, "beef", 6.00)
]

class Store:

  def __init__(self,name,address,order):
    self.name = name
    self.address =address
    self.order = order

  def print_name(self):
    clear.run()
    print(f"\n{self.name}\n")

  def print_address(self):
    clear.run()
    print(f"\n{self.address}\n")


  def show_ui(self, username):
    clear.run()
    next = False
    print(f"Welcome {username} to {self.name}")
    while next is False:
      ui_strings = ["show name", "show address", "Order", "Tracking", "Exit"]
      for menu_option in ui_strings:
        print(f"{ui_strings.index(menu_option)+1} | {menu_option}")
      choice = input("Enter your choice: ")
      if (choice == "1"):
        self.print_name()
      elif (choice == "2"):
        self.print_address()
      elif (choice == "3"):
        self.show_product_menu()
      elif (choice == "4"):
        self.show_tracking_ui()
      elif (choice == "5"):
        break
      else:
        print("Invalid choice")

  def show_product_menu(self):
    clear.run()
    print("ID | Product  | Cost\n---|----------|-------")
    for i in range(len(order)):
      order[i].print_name()
    print("")
     

  def show_tracking_ui(self):
    clear.run()
    def get_driver_location():
      print("driver on route")
      #display location on map
    while True:
      print("1: Track Driver")
      print("2: Exit")
      choice = input("Enter your choice: ")
      if (choice == "1"):
        clear.run()
        get_driver_location()
      elif(choice=="2"):
        clear.run()
        break
      else:
        print("Invalid choice")
