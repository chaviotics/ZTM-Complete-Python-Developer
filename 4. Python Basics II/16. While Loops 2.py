# While loops vs For Loops
my_list = [1,2,3]
for item in my_list:
    print(item)

i = 0 
while i < (len(my_list)):
    print(i)
    i += 1

# while loops are flexible
# we must remember to halt or stop the loop

# so, for simple, use for loops

# if you're not sure how many times you're going to loop, use while loops
# ex, sending emails

while True:

    response = input("Say something: ")
    if response == "byee":
        print("Bye!")
        break

