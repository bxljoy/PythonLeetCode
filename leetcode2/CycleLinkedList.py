class CycleLinkedList:
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def detectCycle(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow