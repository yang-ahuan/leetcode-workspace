# Idea : It's brute force. Compare all of possible subarray and return maximum summation of subarray 
# Time/space complexity : O(n^2)/O(n)
# Status : Time limit exceeded (201/203)
class Solution:
    def maxSubArray(self, nums: list) -> int:
        record = -float("inf")
        for length in range(len(nums),1,-1):
            record_list = []
            for idx in range(0,len(nums)-length+1):
                record_list.append(sum(nums[idx:idx+length]))
            maximum = max(record_list)
            if maximum > record:
                record = maximum
        maximum = max(nums)
        if maximum > record:
            record = maximum
        return record

# Idea : It's Kadane’s algorithm. The algorithm is that find local maximum at index i is the maximum of A[i] and "the sum of A[i] and previous maximum at index i-1"(main idea).
# (from https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d)
# Time/space complexity : O(n)/O(1)
class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 1: return nums[0]
        record = nums[0]
        maximum = nums[0]
        for idx in range(1, len(nums)):
            record = max(nums[idx], record + nums[idx])
            if record > maximum: 
                maximum = record
        return maximum

# Idea : It's divide and conquer. Divide array into two subarraies and find maximum summation of a subarray individually, l_max and r_max. Then, we calculate the maximum summation of subarray crossing left and right subarray, c_max.
#        Finally, compare among l_max, r_max and c_max and get maximum summation.(林立宇演算法筆記)
# Time/space complexity : O(nlogn)/O()
class Solution:
    def maxSubArray(self, nums: list) -> int:
        length = len(nums)
        if length == 1: return nums[0]
        l_max = self.maxSubArray(nums[:length//2])
        r_max = self.maxSubArray(nums[length//2:])
        c_max = max([sum(nums[length//2:idx]) for idx in range(length//2+1, length+1)]) +                       max([sum(nums[idx:length//2]) for idx in range(length//2-1, -1, -1)])
        return max(l_max, r_max, c_max)