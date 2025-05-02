class Solution:
    def __init__(self):

        self.list2 =[]
    def threeSum(self, nums):
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    self.list2.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
                elif total > 0:
                    right -=1
                else:
                    left +=1
        return self.list2


solution = Solution()
print(solution.threeSum([-9,0,9,0,-5,5,1,4,7]))




def threesum(arr, target):
    list1 = []
    for i in range(0, len(arr)-2):
        left = i+1
        right = len(arr)-1

        if i > 0 and arr[i] == arr[i-1]:
            continue
        while left < right:
            sum = arr[i]+arr[left]+arr[right]
            if sum == target:
                list1.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left+1]:
                    left +=1
                while left < right and arr[right] == arr[right-1]:
                    right -=1
                left +=1
                right -=1
            elif sum > target:
                right -=1
            else:
                left +=1
        return list




# def three_sum(arr):
#     arr.sort()
#     max= 0

#     for i in range(len(arr)-2):
#         for j in range(1, len(arr)-1):
#             for k in range(2, len(arr)):
#                 sum = arr[i]+arr[j]+arr[k]
#                 if sum > max:
#                     max = sum
#     return max
                

# arr = [1,2,5,6,7,9,3,2,4,6,9]
# print(three_sum(arr))


# def three_sum(arr, target):
#     arr.sort()
#     print(arr)

#     for i in range(len(arr)-2):
#         for j in range(1, len(arr)-1):
#             for k in range(2, len(arr)):
#                 sum = arr[i]+arr[j]+arr[k]
#                 if sum == target:
#                     return [arr[i], arr[j], arr[k]]
#     return None


# arr = [1,2,5,6,7,9,3,2,4,6,9]
# target = 25
# print(three_sum(arr, target))

