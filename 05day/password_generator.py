import random
print("Welcome to the PyPassword Generator!")


number_of_letters = int(input("How many letters would you like in Your password?\n"))
number_of_numbers = int(input("How many numbers would you like in Your password?\n"))
number_of_symbols = int(input("How many smbols would you like in Your password?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '-', '_']
options = letters + numbers + symbols 





letters_in_password = random.choices(letters, k=number_of_letters)
numbers_in_password = random.choices(numbers, k=number_of_numbers)
symbols_in_password = random.choices(symbols, k=number_of_symbols)
#print(f"{letters_in_password} and {numbers_in_password} and {symbols_in_password}")
list_itens = letters_in_password + numbers_in_password +symbols_in_password
random.shuffle(list_itens)
password = "".join(list_itens)
print(f"Your password is:\n {password}" )



password_list = []


for _ in range(number_of_letters):
    
    posicao = random.randint(0, len(letters) - 1)
    password_list.append(letters[posicao])

for _ in range(number_of_numbers):
    posicao = random.randint(0, len(numbers) - 1)
    password_list.append(numbers[posicao])


for _ in range(number_of_symbols):
    posicao = random.randint(0, len(symbols) - 1)
    password_list.append(symbols[posicao])

size = len(password_list)
for i in range(size -1, 0, -1):
    j = random.randint(0, i)
    #Fisher-Yates Shuffle.
    password_list[i], password_list[j] = password_list[j], password_list[i]

print(password_list)