# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: [ListNode]) -> [ListNode]:
        if not head or not head.next:
            return head
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        arr.sort()

        dummy = ListNode(-1000000)
        for i in range(len(arr)):
            if i == 0:
                cur = ListNode(arr[i])
                dummy.next = cur
            else:
                cur.next = ListNode(arr[i])
                cur = cur.next
        return dummy.next


