import string

str = input("Please enter the string:\n")
new_str = ""

for char in str:
    if char not in string.punctuation:
        new_str += char

print(new_str)

input("Press any key to exit...")