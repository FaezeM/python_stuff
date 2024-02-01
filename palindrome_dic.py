def is_palindrome (input):
    if str(input) == str(input)[::-1]:
        return True
    else:
        return False

def scan_palindrome (min , max):
    palindrome_dic = {num : is_palindrome(num) for num in range(min , max)}
    return palindrome_dic

def only_palindrome (dict):
    for num , is_palindrome in dict.items():
        if is_palindrome:
            print(f"{num} : {is_palindrome}")

def palindrome_list(dict):
    palindrome_list = [num for num, is_palindrome in dict.items() if is_palindrome]
    return palindrome_list

while True:
    try:

        min = input("Please enter the min number:\n")
        min = int(min)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

while True:
    try:

        max = input("Please enter the max number:\n")
        max = int(max)
        if min >= max:
            raise ValueError("Enter a number bigger than minimum.")
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

#print(scan_palindrome(min , max))
#only_palindrome(scan_palindrome(min , max))
print(palindrome_list(scan_palindrome(min , max)))

input("Press any key to exit...")