from random import randint

def sort_tuple(n):
    rand_list = [randint(0, n ** 2) for i in range(n)]
    return tuple(sorted(rand_list))

while True:
    try:

        num = input("Please enter a number:\n")
        num = int(num)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

print(sort_tuple(num))

input("Press any key to exit...")