str = input("Please enter the string:\n")

vowel_count = {vowel: 0 for vowel in "aeiouAEIOU"}

for char in str:
    if char in vowel_count:
        vowel_count[char] += 1

print(vowel_count)

input("Press any key to exit...")