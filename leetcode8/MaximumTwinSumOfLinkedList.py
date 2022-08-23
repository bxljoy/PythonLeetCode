# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: [ListNode]) -> int:
        res = 0
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        left = 0
        right = len(nums) - 1
        while left < right:
            res = max(res, nums[left]+nums[right])
            left += 1
            right -= 1
        return res


