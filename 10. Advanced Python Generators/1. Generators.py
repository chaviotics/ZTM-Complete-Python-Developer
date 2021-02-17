
# generator 
# yield i
# - pauses and resumes functions


range(100) # creates the numbers 1 by 1
list(range(100)) # creates a list

def make_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result

my_list = make_list(50)
print(my_list)
