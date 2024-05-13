import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

password = [""]
for char in range(0, number_of_letters):
    random_char = random.choice(letters)
    password += random_char
for number in range(0, number_of_numbers):
    random_number = random.choice(numbers)
    password += random_number
for sym in range(0, number_of_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol

random.shuffle(password)
passkey = ""
for x in password:
    passkey += x

print(passkey)

