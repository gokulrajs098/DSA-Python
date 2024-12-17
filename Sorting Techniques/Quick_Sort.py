import random

def quick_sort(arr):
    
    if len(arr) < 2:
        return arr
    
    pivot = random.choice(arr)
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]

    return quick_sort(left)+middle+quick_sort(right)

arr = [9,8,7,6,5,5,4,3,2,1]
result = quick_sort(arr)

print(result)