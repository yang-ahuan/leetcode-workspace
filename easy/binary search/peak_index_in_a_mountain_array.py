# Pattern : Binary search
#
# Init -- New two pointers at head and tail of list.
# Step1 -- Check middle whether is the peak of mountain arry. There are 3 cases.
# Term -- Stop once finding the answer.(Beacuse input array is guaranteed to be a mountain array.)

class Solution:
    def peakIndexInMountainArray(self, arr: int) -> int:
        head, tail = 0, len(arr)-1
        while head < tail:
            middle = (head+tail) // 2
            if arr[middle] < arr[middle+1]:
                head = middle
            if arr[middle] < arr[middle-1]:
                tail = middle
            if arr[middle-1] < arr[middle] > arr[middle+1]:
                return middle

# Time : O(log(n))
#######################################################################################

# Naive approach : Check each element whether is peak of a mountain array.

class Solution:
    def peakIndexInMountainArray(self, arr: int) -> int:
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                return i

# Time : O(n)
