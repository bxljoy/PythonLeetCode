class Solution:
    def deleteMiddle(self, head):
        if head.next == None:
            return None
        slow = head
        fast = head
        previous = head

        while fast != None and fast.next != None:
            if slow != head:
                previous = previous.next
            fast = fast.next.next
            slow = slow.next

        previous.next = slow.next
        return head
