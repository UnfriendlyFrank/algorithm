def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1


numbers = [3, 5, 7, 11, 0, 2, 4, 56]
target_number = 12

print(linear_search(numbers, target_number))
