#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Tom = Cat("Tom", 12)
Kigs = Cat("Kigs", 13)
Amao = Cat("Amao", 50)

cats = [Tom, Kigs, Amao]
# 2 Create a function that finds the oldest cat
def oldest_cat(cats:list):
    oldest = None
    age = 0
    for cat in cats:
        if cat.age > 0:
            age = cat.age
            oldest = cat
    return str(f"The oldest cat, {cat.name}, is {age} years old.")



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(oldest_cat(cats))


'''
SOLUTION

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")
'''