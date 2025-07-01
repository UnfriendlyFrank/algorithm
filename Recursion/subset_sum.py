def subset_sum(arr, target, index=0):
    if target == 0:
        return True
    if index >= len(arr) or target < 0:
        return False

    include = subset_sum(arr, target- arr[index], index+1)

    exclude = subset_sum(arr, target, index + 1)

    return include or exclude


arr = [3, 34, 4, 12 , 13, 16]
target = 9

print(subset_sum(arr, target))