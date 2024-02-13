import clear
import store

Store = store.Store("McDon", "123 Main St", "555-555-5555")
print("Welcome to CHATBOT user")
#Ask user for name
while (True):
  print("Enter your name:\n")
  name = input()
  if (name.isalpha()):
    clear.run()
    break
  else:
    print("Please enter only string characters")
#ask user for age
while (True):
  try:
    print("Enter your age:\n")
    age = float(input())
    clear.run()
    break
  except Exception:
    print("Please enter only integer characters")

#Show Store UI
Store.show_ui(name)
