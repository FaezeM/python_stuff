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

if two > one:

    min = one

else:

    min = two

print(f"The minimum of the numbers are {min}.")

input("Press any key to exit...")