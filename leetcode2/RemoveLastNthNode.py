
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        p1 = head
        # p2 is the removed node
        p2 = head
        p3 = None
        res = head
        count = 0
        while p1 != None:
            if p1.next == None:
                p3 = p2
            if count >= n:
                p2 = p2.next
            p1 = p1.next
            count += 1
        # if we need remove the head node
        if p2 == head:
            res = p2.next
        else:
            p3.next = p2.next
        p2.next = None
        return res

    def removeNthFromEnd2(self, head, n):
        dummy = ListNode()
        dummy.next = head

        x = self.findFromEnd(dummy, n + 1)
        x.next = x.next.next
        return dummy.next

    def findFromEnd(self, head, n):
        p1 = head
        p2 = head
        for i in range(n):
            p1 = p1.next

        while p1 != None:
            p2 = p2.next
            p1 = p1.next
        return p2


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)

    s = Solution()
    res = s.removeNthFromEnd2(head, 2)
    print(123)

