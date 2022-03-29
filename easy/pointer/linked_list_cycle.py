# Pattern : Fast & slow pointers
#
# Init -- New slow and fast pointers
# Step 1 -- Slow pointer goes forward 1 node per step and fast pointer goes forward 2 nodes per step.
# Term -- When fast pointer arrives None node or two pointers are on the same node, stop running.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: return True
        return False

# Time : O(n)
# Space : O(1)