# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        array = []
        cur = head
        while cur:
            array.append(cur.val)
            cur = cur.next
        arrayMid = array[left - 1:right]
        arrayMid.reverse()
        array = array[:left - 1] + arrayMid + array[right:]

        head2 = None
        cur2 = None
        for i in range(len(array)):
            if head2 is None:
                head2 = ListNode(array[i])
                cur2 = head2
            else:
                cur2.next = ListNode(array[i])
                cur2 = cur2.next

        return head2

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        pass