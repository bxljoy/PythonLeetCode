class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == headB:
            return headA
        n = 1
        p1 = headA
        p2 = headB
        while n > 0:
            na = self.findLastKelement(p1, n)
            nb = self.findLastKelement(p2, n)
            if na != nb:
                break
            n += 1
        if n == 1:
            return None
        else:
            return self.findLastKelement(p1, n-1)

    def getIntersectionNode4(self, headA, headB):
        if headA == headB:
            return headA
        n = 1
        while True:
            p1 = self.findLastKelement(headA, n)
            p2 = self.findLastKelement(headB, n)
            if p1 != p2:
                break
            n += 1
        if n == 1:
            return None
        else:
            return self.findLastKelement(headA, n-1)

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

    def getIntersectionNode2(self, headA, headB):
        p1 = headA
        p2 = headB
        lenA = 0
        lenB = 0
        while p1:
            p1 = p1.next
            lenA += 1
        while p2:
            p2 = p2.next
            lenB += 1

        p1 = headA
        p2 = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                p1 = p1.next
        else:
            for i in range(lenB - lenA):
                p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def getIntersectionNode3(self, headA, headB):
        p1 = headA
        p2 = headB

        while p1 != p2:
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next

        return p1




