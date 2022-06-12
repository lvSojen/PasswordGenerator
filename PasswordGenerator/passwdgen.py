import random
import os
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator v0.2!")
def passwordLoop():
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  #Eazy Level - Order not randomised:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
  letter = random.randint(0,len(letters))
  password = []
  # generating letters 
  for data in range(nr_letters):
    letter = random.randint(0,len(letters)-1)
    password.append(letters[letter])
  # generating symbols
  for data in range(nr_symbols):
    symbol = random.randint(0,len(symbols)-1)
    password.append(symbols[symbol])
  # generating numbers
  for data in range(nr_numbers):
    number = random.randint(0,len(numbers)-1)
    password.append(numbers[number])
  print("Random password: "+"".join(password))

  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  advanced_password = []
  for data in range(len(password)):
    index = random.randint(0,len(password)-1)
    advanced_password.append(password[index])
    password.pop(index)
  print("Advanced password: "+"".join(advanced_password))

passwordLoop()
nr_choice = input("Are you satisfied with the passwords? (type 'yes' to quit)\n")
while( nr_choice.lower() != 'yes' and nr_choice.lower() != "'yes'"):
  passwordLoop()
  nr_choice = input("Are you satisfied with the passwords? (type 'yes' to quit)\n")
print("Thank you and see you again")
os.system('pause')
