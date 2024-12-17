def two_sum(arr, target):
    left = 0
    right = len(arr)-1

    while left != right:
        sum = left+right
        if sum == target:
            return [left, right]
        elif sum > target:
            right -=1
        else:
            left += 1
    return None


arr = [1,2,3,4,5,6,7,8,9,10]
target = 5
result = two_sum(arr, target)
print(result)