# Idea : It's brute force. Initialize and calculate summation
# Time/space complexity : O(n)/O(n) -- per time
class NumArray:
    def __init__(self, nums: list):
        self.list = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == right: return self.list[left]
        return sum(self.list[left:right+1])

# Idea : It's dynamic programming. Record all summation from index 0 to i (i<=len(nums)),
#        and select two of them to calculate difference. The advantage of this method is
#        that we don't need to access all of numbers in range, and decrease spending time
#        effectively.
# Time/space complexity : O(n)/O(n) -- Initialize, O(1)/O(1) -- per time
class NumArray:
    def __init__(self, nums: list):
        self.list = nums
        self.summations = self.calSum()
    
    def calSum(self):
        summations = [0]
        for num in self.list:
            summations.append(summations[-1] + num)
        return summations

    def sumRange(self, left: int, right: int) -> int:
        if left == right: return self.list[left]
        return self.summations[right+1] - self.summations[left]