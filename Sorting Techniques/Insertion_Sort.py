def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i-1
        while j>=0 and curr<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr
    return arr

arr = [9,8,7,6,5,4,3,2,1]
result = insertion_sort(arr)
print(result)