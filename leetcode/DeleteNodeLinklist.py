# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        cur = node
        while cur.next != None:
            cur.val = cur.next.val
            if cur.next.next == None:
                cur.next = None
                break
            cur = cur.next
