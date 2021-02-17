total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())

# Using global is most of the time, not a good idea.

# Use dependency injection
