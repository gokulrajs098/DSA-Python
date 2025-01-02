def sliding_window(arr, n):

    left = 0
    right = 0
    minimum = float('inf')

    subsum = 0

    while right < len(arr):
        subsum = sum(arr[left:right+1 ])

        if subsum >= n:
            minimum = min(minimum, right-left+1)
            left += 1
        else:
            right += 1
    return minimum


arr = [2,3,1,2,4]
n = 7

result = sliding_window(arr, n)
print(result)