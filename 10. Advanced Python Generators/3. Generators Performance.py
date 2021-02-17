# generators are useful when we are dealing with huge sets of data.
# because we don't have to put the data in a memory.
# everytime we use a generator, we just hold the data in one memory, and go to another data, but still in the same memory

def gen_fun(num):
    for i in range(num):
        yield i

for item in gen_fun(100):
    print(gen_fun)
    print(item)

