my_list = {char for char in 'hello'}

print((my_list))

# for set comprehensions, it's just like list, but using curly brackets

# for dictionary comprehensions 


simple_dict = {
    'a':1,
    'b':2
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
my_dict2 = {num:num*2 for num in [1,2,3]}

print(my_dict)
print(my_dict2)