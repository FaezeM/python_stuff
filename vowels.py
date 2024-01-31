vowels = 'aeiouAEIOU'
sample = 'aurora'
count = 0
for char in sample:
    if char in vowels:
        count += 1

print(count)

input("Press any key to exit...")