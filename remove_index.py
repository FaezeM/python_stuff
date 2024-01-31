str = input("Please enter the string:\n")
new_str = ""

while True:
    try:

        index = input("Please enter the index number:\n")
        index = int(index)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

new_str = str[:index] + str[index + 1:]

print(new_str)

input("Press any key to exit...")