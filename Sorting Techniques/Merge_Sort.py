
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):

    i, j = 0,0
    merged = []

    while i <len(left) and j<len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i +=1
        else:
            merged.append(right[j])
            j +=1
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


arr = [9,5,2,4,6,8,3,1,10,7]

result = merge_sort(arr)
print(result)
