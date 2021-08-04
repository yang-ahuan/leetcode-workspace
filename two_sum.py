# Idea : Scan all of possibilities
# Time/space complexity : O(n^2) / O(1)
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for front_idx in range(len(nums)-1):
            for behind_idx in range(front_idx+1, len(nums)):
                if nums[front_idx]+nums[behind_idx] == target:
                    return [front_idx, behind_idx]

# Idea : Check whether difference of target and each number is in nums. To look at difference in nums faster, I convert the data type to set.
# Time/space complexity : O(n) / O(n)
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        nums_set = set(nums)
        for front_idx in range(len(nums)-1):
            if target-nums[front_idx] in nums_set:
                for behind_idx in range(front_idx+1, len(nums)):
                    if target-nums[front_idx] == nums[behind_idx]:
                        return [front_idx, behind_idx]