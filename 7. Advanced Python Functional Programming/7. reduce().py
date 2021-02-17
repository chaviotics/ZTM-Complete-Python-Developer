from functools import reduce

my_list = [1,2,3]

def accumulator(accumulate, item):
    return accumulate + item

print(reduce(accumulator, my_list, 10)) # 10 is initial number

# used to 
# reduce is loved by programmers