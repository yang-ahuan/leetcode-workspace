# Idea : Scan and record number in a list.
# Time/space complexity : O(n)/O(n)
class Solution:
    def singleNumber(self, nums: list) -> int:
        one = set()
        two = set()
        for num in nums:
            if num in two:
                continue
            elif num in one:
                one.remove(num)
                two.add(num)
            else:
                one.add(num)
        ans = [*one]
        return ans[0]

# Idea : By bit manipulation(XOR), get the single number after scan the list.
# Time/space complexity : O(n)/O(1)
class Solution:
    def singleNumber(self, nums: list) -> int:
        temp = nums[0]
        for num in nums[1:]:
            temp = temp ^ num
        return temp

# P.S. Using reduce function from functools is that consume more memory
from functools import reduce
class Solution:
    def singleNumber(self, nums: list) -> int:
        return reduce(lambda x,y:x^y, nums)