def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

a = [5, 2, 9, 1, 5, 6]
bubble_sort(a)
print(a)  # [1, 2, 5, 5, 6, 9]