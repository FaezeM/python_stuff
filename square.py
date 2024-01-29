num = input("Please enter a number:\n")
try:

    safe_num = float(num)
    square = safe_num ** 2
    print(f"The square of {num} is {square}")

except ValueError: #if the user entered eg. string

    print("Please enter a valid number")

input("Press any key to exit...")