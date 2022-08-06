class Solution:
    def removeElements(self, head, val):
        if head == None:
            return None

        while head.val == val:
            head = head.next
            if head == None:
                return None

        pre = None
        cur = head
        while cur != None:
            if cur.val == val:
                if pre == None:
                    cur = cur.next
                else:
                    pre.next = cur.next
                    cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head

