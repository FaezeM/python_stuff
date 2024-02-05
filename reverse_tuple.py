a = (1,2,4,5,6,4,9,7,8,0)

def reverse(tup):
    if len(tup) % 2 == 0:
        new_tup = tup[::-1]
        return new_tup
    else:
        return 'not even'
    
print(reverse(a))

input("Press any key to exit...")
