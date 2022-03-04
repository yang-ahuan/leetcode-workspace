# Pattern : Fast & slow pointers
#
# Init -- New 3 pointers. One for reversing. Two for looking for middle point.
# Step1 -- Reverse first half linked list and find middle point in linked list.
# Step2 -- Check whether is palindrome.
# Term -- Scan completely, or not palindrome

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        front = back = head
        while back and back.next:
            back = back.next.next
            rev, rev.next, front = front, rev, front.next
        # Whether the length of linked list is odd.
        if back: front = front.next
        while front and front.val == rev.val:
            front = front.next
            rev = rev.next
        return not front

# Time : O(n)