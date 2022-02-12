# Pattern : In-place reversal of a linked list
#
# Init : New three potiners to record front, back and tracking node.
# Step 1 : Reverse the first two pointers.
# Step 2 : Move three pointers to next node at the same time.
# Term : Stop running when front is None.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        before, middle, front = None, head, head.next
        while True:
            middle.next = before
            if not front: return middle
            before, middle, front = middle, front, front.next

# Time : O(n)