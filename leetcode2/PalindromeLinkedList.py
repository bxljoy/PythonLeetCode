# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        slow = head
        fast = head
        while fast or fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        left = head
        right = self.reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head):
        pre = None
        cur = head
        nxt = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


