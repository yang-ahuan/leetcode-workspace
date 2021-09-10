# Idea : Leverage the property of set
# Time/space complexity : O(1) / O(1)
class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        return len(nums) != len(set(nums))