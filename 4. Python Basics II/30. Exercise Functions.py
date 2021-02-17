li = [10, 2, 3, 4, 8, 11, 12]


def highest_even(li):
    highest_even = 0
    for num in li:
        if num > highest_even and num % 2 == 0:
            highest_even = num
    return highest_even


print(highest_even(li))


def highest_even_solution(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
        return max(evens)
