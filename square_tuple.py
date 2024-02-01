a = [2,3,4]

def make_square_tuple(li):
    new_list = ((i , i**2) for i in li)
    return tuple(new_list)

print(make_square_tuple(a))

input("Press any key to exit...")