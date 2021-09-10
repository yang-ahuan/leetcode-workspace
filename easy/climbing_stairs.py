# Idea : Through observing, the rule is exactly fibonacci
# Time/space complexity : O(n)/O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        before, current = 0, 1
        for _ in range(1, n+1):
            temp = current
            current = before + current
            before = temp
        return current