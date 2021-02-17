from functools import reduce

# lambda param: (action) func(param)

# lambda functions are one time anonymous functions
# we don't need to run them more than once

my_list = [1,2,3]

# def multiply_by2(item): # We don't need this
#     return item * 2

# def only_odd(item):
#     return item % 2 != 0

# def accumulator(accumulate, item):
#     return accumulate + item

print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list))