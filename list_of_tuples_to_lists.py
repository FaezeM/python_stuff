a = [(2,3),(4,5)]

def convert(li):
    new = [list(i) for i in li]
    return new

print(convert(a))

input("Press any key to exit...")