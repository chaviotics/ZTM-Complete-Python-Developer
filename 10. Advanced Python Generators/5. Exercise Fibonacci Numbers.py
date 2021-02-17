def fibonacci(index):
    a = 0
    b = 1
    for i in range(index):
        yield a
        temp = a
        a = b
        b = temp + b

# for i in fibonacci(20):
#     print(i) 
# print(next(fib))
# print(next(fib))
# print(fib)

def fib2(index):
    a = 0
    b = 1
    fib = []
    for i in range(index):
        fib.append(a)
        temp = a
        a = b
        b = temp + b

    return fib

for i in fib2(10):
    print(i)








# Here is an example generator which calculates fibonacci numbers:
# generator version
# def fib(number):
#     a =  0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b

# for x in fib(100):
#     print(x)



# def fib2(number):
#     a =  0
#     b = 1
#     result = []
#     for i in range(number):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result

# print(fib2(100))