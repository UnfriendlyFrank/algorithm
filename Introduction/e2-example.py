import time
import random


# الگوریتم مرتب سازی حبابی
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# الگوریتم مرتب سازی سریع
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# تولید یک لیست تصادفی بزرگ
arr = [random.randint(0, 20000) for _ in range(20000)]

# مقایسه زمان اجرا برای مرتب‌سازی سریع
start_time = time.time()
quick_sort(arr.copy())
quick_sort_time = time.time() - start_time
print("زمان اجرا برای مرتب‌سازی سریع: {:.5f} ثانیه".format(quick_sort_time))

# مقایسه زمان اجرا برای مرتب‌سازی حبابی
start_time = time.time()
bubble_sort(arr.copy())
bubble_sort_time = time.time() - start_time
print("زمان اجرا برای مرتب‌سازی حبابی: {:.5f} ثانیه".format(bubble_sort_time))



