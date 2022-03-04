# Pattern : Fast & Slow Pointers
#
# Init : Two pointers for check whether the value of nodes are the same
# Step 1 : If the value of adjacent nodes are the same, remove one. Otherwise, continue.
# Term : Reach the tail of linked list, None.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # -100 <= Node.val <= 100
        before, check, check_val = ListNode(None, head), head, -101
        while check:
            if check.val != check_val:
                check_val = check.val
                before, check = before.next, check.next
            else:
                before.next, check = check.next, check.next
        return head

# Time : O(n)