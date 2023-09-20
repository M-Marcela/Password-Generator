#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_letters = random.sample(letters, nr_letters)
pass_symbols = random.sample(symbols, nr_symbols)
pass_numbers = random.sample(numbers, nr_numbers)

password = pass_letters + pass_symbols + pass_numbers
password_easy = ''.join(password)
print("Your 1st easy password is: " + password_easy)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_mix = pass_letters + pass_symbols + pass_numbers
random.shuffle(password_mix)
password_hard = ''.join(password_mix)
print("Your 1st hard password is: " + password_hard)

# other way to write this code for easy and hard level
new_pswd = ""
for char in range(1, nr_letters + 1):
    new_pswd += random.choice(letters)
for char in range(1, nr_symbols + 1):
    new_pswd += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    new_pswd += random.choice(numbers)

print("\nYour 2nd easy password is: " + new_pswd)

new_pswd = []
for char in range(1, nr_letters + 1):
    new_pswd.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    new_pswd.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    new_pswd.append(random.choice(numbers))

random.shuffle(new_pswd)
new_pswd_str = ""
for char in new_pswd:
    new_pswd_str += char
print("Your 2nd hard password is: " + new_pswd_str)
