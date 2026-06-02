def search_transaction(ids, target_id):
    left = 0
    right = len(ids) - 1

    while left <= right:
        mid = (left + right) // 2
        if ids[mid] == target_id:
            return mid
        elif ids[mid] < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Тест
print(search_transaction([1001, 1005, 1010, 1025], 1010))  # 2