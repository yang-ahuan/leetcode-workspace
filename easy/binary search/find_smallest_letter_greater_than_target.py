# Pattern : Binary search
#
# Init -- Same to binary search
# Step 1 -- Check whether the case is the worst.
# Step 2 -- Operate binary search.
# Term -- When list is scanned completely, stop running.
# Difference(compared to binary search) -- It cannot stop early.

class Solution:
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        head, tail = 0, len(letters)-1
        while head <= tail:
            middle = (head+tail) // 2
            if target < letters[middle]:
                tail = middle-1
            else:
                head = middle+1
        return letters[head]

# Time : O(log(n))