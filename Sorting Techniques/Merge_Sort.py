def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0,0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

arr = [9,8,7,6,5,5,4,3,2,8,2,1]
result = merge_sort(arr)
print(result)