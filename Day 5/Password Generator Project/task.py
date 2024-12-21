import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# passwords = ""
# for number in range (0, nr_letters):
#     passwords += random.choice(letters)
#
# for number in range (0, nr_symbols):
#     passwords += random.choice(symbols)
#
# for number in range (0, nr_letters):
#     passwords += random.choice(numbers)
# print(passwords)

passwords_list = []
for number in range (0, nr_letters):
    passwords_list.append(random.choice(letters))

for number in range (0, nr_symbols):
    passwords_list.append(random.choice(symbols))

for number in range (0, nr_letters):
    passwords_list.append(random.choice(numbers))

random.shuffle(passwords_list)
password = ""
for char in passwords_list:
    password += char
print(password)





