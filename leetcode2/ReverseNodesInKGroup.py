# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup2(self, head: [ListNode], k: int) -> [ListNode]:
        array = []
        while head != None:
            array.append(head.val)
            head = head.next
        reverseArray = []
        while len(array) // k > 0:
            for i in range(k-1, -1, -1):
                reverseArray.append(array.pop(i))
        reverseArray.extend(array)

        cur = None
        p1 = None
        for val in reverseArray:
            if p1 == None:
                p1 = ListNode(val)
                cur = p1
            else:
                p1.next = ListNode(val)
                p1 = p1.next
        return cur

    def reverse2(self, head):
        pre = None
        cur = head
        nxt = head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    # [a, b), and a node is the head node
    def reverse(self, a, b):
        pre = b
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseBetween(self, head, left, right):
        pass

    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        if head == None:
            return None
        a = b = head
        for i in range(k):
            if b == None:
                return head
            b = b.next
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead

    def traverse(self, head):
        if not head:
            return None
        # preorder
        self.traverse(head.next)
        # postorder
        print(head.val)

if __name__ == '__main__':
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
    s = Solution()
    # s.reverse2(l1)
    # s.reverse(l2, l5)
    # s.reverseKGroup(l1, 2)
    s.traverse(l1)



