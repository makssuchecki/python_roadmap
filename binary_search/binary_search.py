
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right)
    else:
        return binary_search_recursive(arr, target, left, mid-1)

numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
result = binary_search_recursive(numbers, 8)
print(f"Found at index: {result}")

def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = binary_search_iterative(numbers, 13)
print(f"Found at index: {result}")

import bisect

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

pos = bisect.bisect_left(numbers, 40)

target = 40
pos= bisect.bisect(numbers, target)
if pos<len(numbers) and numbers[pos] == target:
    print(f"Found {target} at index {pos}")
else:
    print(f"{target} not found")

bisect.insort(numbers, 41)