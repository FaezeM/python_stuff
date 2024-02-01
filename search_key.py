phone_prefixes = {'Naples' : '081','Rome' : '06','Bari' : '080','Venice' : '041'}

def is_key( dic , key ):
    return key in dic

input_key = input("Please enter the key:\n")
print(is_key(phone_prefixes , input_key))

input("Press any key to exit...")