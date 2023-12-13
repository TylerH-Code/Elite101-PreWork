import store

Store=store.Store()
print("Welcome to CHATBOT user")
#Ask user for name
while(True):
    print("Enter your name:\n")
    name=input()
    if (name.isalpha()):
      break
    else:
      print("Please enter only string characters")
#ask user for age
while(True):
  try:
    print("Enter your age:\n")
    age=float(input())
    break
  except Exception:
    print("Please enter only integer characters")

#Show Store UI
Store.show_ui()