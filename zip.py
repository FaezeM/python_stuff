a = (1,2,4,5,6,4,9,7,8,0)

def is_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

def zipped(tup):
    new_list = list(zip(tup, (is_odd(element) for element in tup)))
    return new_list

print(zipped(a))

input("Press any key to exit...")