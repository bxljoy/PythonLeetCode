class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

successor = None
class Solution:
    def reverseList(self, head):
        p1 = head
        array = []
        if p1 == None or p1.next == None:
            return head
        while p1 != None:
            array.append(p1.val)
            p1 = p1.next
        cur = None
        while len(array) > 0:
            if p1 == None:
                p1 = ListNode(array.pop())
                cur = p1
            else:
                p1.next = ListNode(array.pop())
                p1 = p1.next
        return cur

    def reverseList2(self, head):
        if head == None or head.next == None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseN(self, head, n):
        global successor
        if n == 1:
            successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = successor
        return last
