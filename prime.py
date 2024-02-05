
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_list(num):
    primes = [i for i in range(2, num + 1) if is_prime(i)]
    return primes

def prime_count(num):
    count = 0
    for i in range(2, num + 1):
        if is_prime(i):
            count += 1
    return count

def sum_primes(nof_primes):
    sum = 0
    for i in range(2, nof_primes + 1):
        if is_prime(i):
            sum += i
    #return sum(prime_list(nof_primes))
    return sum

while True:
    try:

        input_num = input("Please enter a number:\n")
        input_num = int(input_num)
        break

    except ValueError: #if the user entered eg. string

        print("Please enter a valid number")

#print(is_prime(input_num))
#print(prime_list(input_num))
#print(prime_count(input_num))
print(sum_primes(input_num))

input("Press any key to exit...")
