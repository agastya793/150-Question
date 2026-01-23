# Count Even and Odd Numbers in List

def count_even_odd(lst):
    even = odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(count_even_odd([1,2,3,4,5,6]))
