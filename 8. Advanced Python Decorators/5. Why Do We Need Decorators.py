from time import time

def performance(function):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = function(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000):
        i * 5

long_time()

# used in authenticate
# used in log-in
# used in Django