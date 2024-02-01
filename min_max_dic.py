def create_dic():
    while True:
        try:

            min = input("Please enter the minimum number:\n")
            min = int(min)
            break

        except ValueError: #if the user entered eg. string

            print("Please enter a valid number")

    while True:
        try:

            max = input("Please enter the maximum number:\n")
            max = int(max)
            if min >= max:
                raise ValueError("Enter a number bigger than minimum.")
            break

        except ValueError: #if the user entered eg. string

            print("Please enter a valid number")

    square_dic = {num : num ** 2 for num in range(min , max)}

    return square_dic

print(create_dic())

input("Press any key to exit...")