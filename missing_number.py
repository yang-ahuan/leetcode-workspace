# Idea : Check each number whether is a missing number. I use the property of set to find number in nums quickly.
# Time/space complexity : O(n) / O(n)
class Solution:
    def missingNumber(self, nums: list) -> int:
        nums_set = set(nums)
        for num in range(len(nums)):
            if num not in nums_set:
                return num
        return len(nums)

# Idea : The summation in range is stable, and only one number is missing. So, the difference of these lists is answer
# Time/space complexity : O(n) / O(1)
class Solution:
    def missingNumber(self, nums: list) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)