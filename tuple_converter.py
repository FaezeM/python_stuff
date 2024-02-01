a = (1,2,4,5,6,4,9,7,8,0);

def tuple_converter(tup):
    string = ''
    for element in tup:
        string += str(element)
    return string

print(tuple_converter(a))

input("Press any key to exit...")