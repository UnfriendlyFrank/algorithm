def subset_sum(arr, target, index=0):
    """
    بررسی اینکه آیا زیرمجموعه‌ای از لیست 'arr' وجود دارد که مجموع آن برابر 'target' باشد.
    """
    # پایه بازگشت: اگر مقدار هدف صفر شود، به جواب رسیده‌ایم
    if target == 0:
        return True
    # شرط خاتمه: اگر لیست تمام شود یا مقدار هدف منفی شود
    if index >= len(arr) or target < 0:
        return False

    # حالت اول: عنصر فعلی انتخاب شود
    include = subset_sum(arr, target - arr[index], index + 1)

    # حالت دوم: عنصر فعلی انتخاب نشود
    exclude = subset_sum(arr, target, index + 1)

    # اگر یک از دو حالت جواب درست بدهد، مجموع ممکن است
    return include or exclude


# مثال تست
arr = [3, 34, 4, 12, 5, 2]
target = 9
print("آیا زیرمجموعه‌ای وجود دارد که مجموع مساوی هدف باشد؟", subset_sum(arr, target))
