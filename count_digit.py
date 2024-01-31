#counts how many digits 1 or 2 are present in a given integer, e.g., 20201918
while True:
    try:

        num = input("Please enter the number:\n")
        num = int(num)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

count = 0

while num > 0:
    digit = num % 10 #get the last digit
    if digit == 1 or digit == 2:
        count += 1
    num //= 10 #remove the last digit

print(f"The number has {count} '1 and 2' digits")

input("Press any key to exit...")