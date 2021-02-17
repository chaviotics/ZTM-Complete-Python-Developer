my_list = [1,2,3]
my_list2 = [4,5,6]

# the function should only get 1 item in the iterable
def multiply_by2(item):
    return item * 2

my_list2 = list(map(multiply_by2, my_list2))

print(my_list2)

print(list(map(multiply_by2, my_list)))
print(my_list)

word = 'chavi'
# letters = ['a','b','c','d']
letters = 'a'

def change_first(word):
    return str(word[0].upper() + word[1:])

print(list(map(change_first,letters)))










'''
BEFORE
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list

print(multiply_by2([1,2,3]))
'''



