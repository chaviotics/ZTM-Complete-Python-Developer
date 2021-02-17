def special_forloop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_forloop([1,2,3])
# we can see here that it's just one same  memory

class MyGenerator(): # our own special range
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self 
    
    def __next__(self):
        if MyGenerator.current < self.last:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration # the for loop catches this automatically

    
gen = MyGenerator(0, 100)

for i in gen:
    print(gen)
    print(i)
