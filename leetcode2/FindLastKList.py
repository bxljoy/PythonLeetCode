class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findLastKelement(self, head, k):
        p1 = head
        p2 = head
        count = 0
        while p1 != None:
            if count >= k:
                p2 = p2.next
            p1 = p1.next
            count += 1
        return p2

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6

    element = s.findLastKelement(l1, 3)
    print(element.val)

