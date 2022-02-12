# Pattern : Two pointers
#
# Init -- New a empty linked list and two pointers for retruning and tracking
# Step 1 -- Compare value of two sorted lists. There are two cases(>, <=) against list1.
# Step 2 -- Add smaller value of node to new list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        ans = trace = ListNode(None, None)
        while list1 and list2:
            if list1.val > list2.val:
                trace.next = list2
                trace = trace.next
                list2 = list2.next
            else:
                trace.next = list1
                trace = trace.next
                list1 = list1.next
        
        if not list1: trace.next = list2
        if not list2: trace.next = list1
        return ans.next

# Time : O(n)