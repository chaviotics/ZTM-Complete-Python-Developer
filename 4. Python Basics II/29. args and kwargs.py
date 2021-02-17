# *args **kwargs

# * this accepts any number of arguments
# ** creates a dictionary with an equal

def super_func(*args, **kwargs):
    total = 0
    print(*args)
    print(args)
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

# Rules of ordering
# Params, *args, default paramaters, **kwargs