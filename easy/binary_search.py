# Pattern : Binary Search(standard method)
#
# Init -- Initialize two pointers at top and tail
# Step 1 -- Compare target with middle. There are 3 cases (>, <, =)
# Term -- If equal, return index of target. if not found, return -1

class Solution:
    def search(self, nums: list, target: int) -> int:
        back_idx, front_idx = 0, len(nums)-1
        while back_idx <= front_idx:
            middle_idx = (back_idx+front_idx)//2
            if target == nums[middle_idx]:
                return middle_idx
            if target > nums[middle_idx]:
                back_idx = middle_idx+1
            if target < nums[middle_idx]:
                front_idx = middle_idx-1
        return -1

# Time : O(log(n))