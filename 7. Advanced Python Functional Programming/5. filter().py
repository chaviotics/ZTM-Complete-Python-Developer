my_list = [1,2,3]
words = ['Mama', 'Abra', 'Ace', 'amos', 'Baboy']

def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

def only_A(item):
    return item[0] == 'A' or item[0] == 'a'

print(list(filter(only_odd, my_list)))
print(list(map(only_odd, my_list)))
# filter checks for a boolean expression in the iterable   
print(list(filter(only_A, words))) 