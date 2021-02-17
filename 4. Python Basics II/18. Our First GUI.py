picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

for i in picture:
    for j in i:
        if j == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print()


fill = "#"
empty = " " 

for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end="")
        else:
            print(empty, end="")
    print()
