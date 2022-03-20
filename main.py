import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_str = ""
password_list = []
for char in range(1, nr_letters + 1): #for letters
    l = random.choice(letters)
    password_str += l
    password_list.append(l)
for sym in range(1, nr_symbols + 1): #for symbols
    s = random.choice(symbols)
    password_str += s
    password_list.append(s)

for num in range(1, nr_numbers + 1):
    n = random.choice(numbers)
    password_str += n
    password_list.append(n)
print("your password has generated below ")
print(f"easy password is {password_str}")
#print(password_list) #before shuffle
random.shuffle(password_list)
#print(password_list) #after shuffle

# for convert list to string
pwd = ""
for i in password_list:
    pwd += i
print(f"hard password is {pwd}")


