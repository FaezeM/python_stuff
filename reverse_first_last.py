a = (1,2,4,5,6,4,9,7,8,0)

def reverse_element(tup):
    new_tup = (tup[-1],) + (tup[1: -1]) + (tup[0],)
    return new_tup

print(reverse_element(a))

input("Press any key to exit...")