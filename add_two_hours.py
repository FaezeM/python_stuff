while True:
    try:

        hour = input("Please enter the hour:\n")
        hour = int(hour)
        if hour >= 24:
            raise ValueError("Invalid time after addition")
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

while True:
    try:

        minute = input("Please enter the minute:\n")
        minute = int(minute)
        if minute >= 60:
            raise ValueError("Invalid time after addition")
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

hour += 2

if hour > 24:
    hour %= 24

print(f"2 hours later would be {hour}:{minute}")

input("Press any key to exit...")
    