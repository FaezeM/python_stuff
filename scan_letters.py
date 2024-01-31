str = input("Please enter the string:\n")
letter = 0
digit = 0
symbol = 0

for char in str:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
        letter += 1
    else:
        symbol += 1

print(f"Digits = {digit}\tLetters = {letter}\t Symbols = {symbol}")

input("Press any key to exit...")