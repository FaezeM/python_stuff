while True:
    try:

        length = input("Please enter the length of the rectangle:\n")
        safe_length = float(length)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")
while True:
    try:

        width = input("Please enter the width of the rectangle:\n")
        safe_width = float(width)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

area = safe_length * safe_width
print(f"The area of the rectangle is {area}.")

input("Press any key to exit...")
    