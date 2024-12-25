class Solution:
    def threeSumClosest(self, nums,  target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            
            while left < right:
                current_sum = nums[i]+nums[left]+nums[right]

                if abs(current_sum - target) < abs(closest_sum-target):
                    closest_sum = current_sum
                if current_sum < target:
                    left+=1
                elif current_sum > target:
                    right -=1
                elif current_sum == target:
                    return current_sum
        return closest_sum
