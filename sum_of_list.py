a = [1,2,4,5,6,4,9,7,8,0]

def list_sum(li):
    return sum(li)
    #sum = 0
    #for element in li:
    #    sum += element
    #return sum

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def odd_even_sum(li , o_or_e):
    res = 0
    if o_or_e == 'even':
        return sum(num for num in li if is_even(num))
    elif o_or_e == 'odd':
        return sum(num for num in li if not is_even(num))
    
def odd_even_list(li , o_or_e):
    if o_or_e == 'even':
        return list(num for num in li if is_even(num))
    elif o_or_e == 'odd':
        return list(num for num in li if not is_even(num))
    
def odd_even_index_sum(li, o_or_e):
    if o_or_e == 'even':
        return sum(li[::2])
    elif o_or_e == 'odd':
        return sum(li[1::2])
    
def min_element(li):
    minimum = li[0]
    for i in range(len(li)):
        if li[i] < minimum:
            minimum = li[i]
    return minimum
    #return min(li)

def min_index(li):
    return li.index(min(li))

def reverse_sort(li):
    return sorted(li)[::-1]

def is_sum_odd(li):
    if is_even(sum(li)):
        return False
    elif not is_even(sum(li)):
        return True
    
def sliced_sum(li):

    while True:
        try:

            first = int(input("Please enter the first index:\n"))
            if first > len(li):
                raise ValueError("Invalid index")
            break

        except ValueError: #if the user entered eg. string

            print("Please enter a valid number")

    while True:
        try:

            second = int(input("Please enter the second index:\n"))
            if second > len(li) or second < first:
                raise ValueError("Invalid index")
            break

        except ValueError: #if the user entered eg. string

            print("Please enter a valid number")
    
    return sum(li[first:second + 1])

#print(list_sum(a))
#print(odd_even_sum(a , 'odd'))
#print(odd_even_index_sum(a , 'odd'))
#print(min_element(a))
#print(min_index(a))
#print(reverse_sort(a))
#print(is_sum_odd(a))
#print(sliced_sum(a))
print(odd_even_list(a , 'even'))

input("Press any key to exit...")