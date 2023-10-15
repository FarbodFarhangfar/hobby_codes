import time
import random
import math
import numpy as np

def binary_search(arr, target):
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

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)

    else:
        return binary_search_recursive(arr, target, mid + 1, high)





def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev
    return -1


n = 10**5


random_list = np.random.randint(low=1, high=n-2, size=n)
random_list.sort()

target = 32125

print(target)
ind1 = binary_search(random_list, target)
print(ind1, random_list[ind1])

ind3 = binary_search_recursive(random_list, target, 0, len(random_list))
print(ind3)

ind2 = jump_search(random_list, target)

print(ind2, random_list[ind2])

print(np.where(random_list==target))








