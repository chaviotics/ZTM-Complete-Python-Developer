# iterable
# __iter__

# iterate

# generators - are iterable

# but not everything that is iterable is a generator
# example is range

# general way to create a generator
# they are usually functions
def generator_function(num):
    for i in range(num):
        yield i # pauses the function and comes back to it which we do something to it

g = generator_function(100)
# remembers the value before the next
print(next(g)) # 0
next(g) # 1
print(g)
print(next(g)) # 2
print(next(g))  # 3
next(g) # 4
print(next(g)) # 5
print(g)

# generator functions just keep the recent data in memory, rather than putting all those individual values in memory

#so yield and next are in pair when we use generator functions
# a generator is created when we use the yield

# yield pauses the function

# for item in generator_function(100):
#     print(item)

# this is similar below

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i)
#     return result   