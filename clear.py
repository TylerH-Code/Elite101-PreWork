import os


def run():
  #found using os documentation
  #checks if linux is being used
  if (os.name == "posix"):
    os.system('clear')
  #checks if windows is being used
  if (os.name == "nt"):
    os.system('cls')
