# Pattern : Fast & slow pointers
#
# Init -- New fast and slow pointers.
# Step1 -- Step size of slow pointer and fast pointer are individually one and two.
# Term -- While fast pointer reaches the end of the linked list, the position of slow pointer is exactly middle point.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        front = back = head
        while back and back.next:
            front = front.next
            back = back.next.next
        return front

# Time : O(n)