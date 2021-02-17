# clean code

def isEven(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

print(isEven(5))

# cleaning up further

def is_even(num):
    if num % 2 == 0:
        return True
    return False

# even cleaner

def is_even2(num):
    return num % 2 == 0
