#beginner Fibonacci sequence using loop
n = 0
m = 1
print(f"{n}\n")
      
for count in range(100):
    temp = m
    m = n + m
    n = temp
    print(f"{n}\n")
    #print(f"m = {m}\n")

input("Press any key to exit...")