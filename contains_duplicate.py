# Intuition : Leverage the property of set
class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        return len(nums) != len(set(nums))