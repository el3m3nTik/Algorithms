import random


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

n = 10
mas = [random.randint(1, 100) for i in range(n)]
insertion_sort(mas)
print(mas)
# O(n**2)
