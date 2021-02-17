import sys
from random import randint

#print(randint(1, 5))
 
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# guess = sys.argv[1]
print(answer)


while True:
    try:
        guess = int(input(f"Guess the numbers between {int(sys.argv[1])} and {int(sys.argv[2])}: "))
        if int(sys.argv[1]) <= guess <= int(sys.argv[2]):
            if guess == answer:
                print("idola nimo oy!")
                break 
            else:
                print("Hapit naka!")
        else:
            print("Baga! Layo ra kaayo ka!")
            continue
    except ValueError:
        print("Bugo! Input a number!")
    









# print(f'hi {guess}')
# while True:
#     guess = int(sys.argv[1])
#     # guess = int(input('What is the number? '))
#     if guess == random:
#         print("You win!")
#         break
#     else:
#         print('Try again!')
    
# solution
# remember error handling