my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = [100,200,300]

print(list(zip(my_list, your_list, their_list)))

# doesn't matter if tuple because it's an iterable
# its use is usually with zipping details of accounts such as usernname and password, number and stuff