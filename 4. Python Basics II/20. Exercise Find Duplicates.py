some_list = ['a','b','c','b','d','m','n','n']

duplicates = []

for i in range(len(some_list)):
    counter = 0
    for j in range(len(some_list)):
        if some_list[j] == some_list[i]:
            counter += 1
    
    if counter > 1:
        if some_list[i] not in duplicates:
            duplicates.append(some_list[i])

print(duplicates)

# use .count
# solution
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
