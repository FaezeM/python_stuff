#convert m/s to km/h
while True:
    try:

        num = input("Please enter a number:\n")
        safe_num = float(num)
        kmph = safe_num * 3600 / 1000
        print(f"The equivalent of {num}m/s is {kmph}km/h")
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

input("Press any key to exit...")
