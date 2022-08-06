# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        dic = {}
        cur = head
        while cur:
            c = cur.val
            cv = dic.setdefault(c, 0)
            dic[c] = cv + 1
            cur = cur.next
        dummy = ListNode(-1)
        array = []
        for key, value in dic.items():
            if value == 1:
                array.append(key)
        cur = None
        for i in range(len(array)):
            if i == 0:
                cur = ListNode(array[i])
                dummy.next = cur
            else:
                cur.next = ListNode(array[i])
                cur = cur.next
        return dummy.next

    def deleteDuplicates1(self, head: [ListNode]) -> [ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        slow = head
        fast = head.next
        flag = False
        while fast:
            if slow.val != fast.val:
                if flag:
                    pre.next = fast
                    slow = fast
                    flag = False
                else:
                    pre = slow
                    slow = slow.next
            else:
                flag = True
            fast = fast.next
        if slow == head:
            return None
        else:
            if flag:
                pre.next = None
        return dummy.next




