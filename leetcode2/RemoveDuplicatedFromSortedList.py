# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates1(self, head: [ListNode]) -> [ListNode]:
        slow = head
        fast = head
        while fast:
            if fast.val == slow.val:
                fast = fast.next
                slow.next = fast
            else:
                slow = slow.next
        return head

    def deleteDuplicates2(self, head: [ListNode]) -> [ListNode]:
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        while cur:
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return head

    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return head
        slow = head
        fast = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head


