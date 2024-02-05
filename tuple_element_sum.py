a=((1,2,3),(4,5,6),(7,8,9))

def sum_element(tup):
    sum_tup = tuple(sum(row) for row in tup)
    return sum_tup

print(sum_element(a))

input("Press any key to exit...")