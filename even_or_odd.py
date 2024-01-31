while True:
    try:

        num = input("Please enter the number:\n")
        num = int(num)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

input("Press any key to exit...")