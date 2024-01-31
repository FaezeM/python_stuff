while True:
    try:

        one = input("Please enter the first number:\n")
        one = int(one)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

while True:
    try:

        two = input("Please enter the second number:\n")
        two = int(two)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

while True:
    try:

        three = input("Please enter the third number:\n")
        three = int(three)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

if one >= two and one >= three:
    max = one
elif two >= one and two >=three:
    max = two
else:
    max = three

print(f"The largest number is {max}.")

input("Press any key to exit...")