a = (1,2,4,5,6,4,9,7,8,0)
b = (11,12,13)

def append_three(tup):
    new_tuple = tuple(list(tup) + [3])
    return new_tuple

def add_b(tup , new):
    new_tuple = tuple(list(tup[:1]) + list(new) + list(tup[1:]))
    return new_tuple

#new_tup = append_three(a)
new_tup = add_b(a , b)
print(new_tup)

input("Press any key to exit...")