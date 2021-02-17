import os

with open('.\sections CWD.txt', 'r') as file:
    sections = [i.strip('\n').replace(':', '').replace('Section ', '') for i in file.readlines() if i[0] not in '0123456789']

    for section in sections:
        try:
            os.mkdir(f".\{section}")
        except FileExistsError:
            continue



    # for i in sections:
    #     print(i)
    
    # print(sections)

