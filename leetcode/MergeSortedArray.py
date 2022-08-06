class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        """
        total = m+n
        while len(nums1) > total:
            nums1.pop()

        for j in range(n):
            nums1[m+j] = nums2[j]
            for k in range(m+j, 0, -1):
                if nums1[k-1] > nums1[k]:
                    nums1[k-1], nums1[k] = nums1[k], nums1[k-1]
                else:
                    break

class Solution2:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        """
        l = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                l.append(nums1[i])
                i += 1
            else:
                l.append(nums2[j])
                j += 1

        while i < m:
            l.append(nums1[i])
            i += 1
        while j < n:
            l.append(nums2[j])
            j += 1
        nums1.clear()
        nums1.extend(l)

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 1, 0, 1, 4, 6]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    # s = Solution()
    # s.merge(nums1, m, nums2, n)
    # print(nums1)

    s2 = Solution2()
    s2.merge(nums1, m, nums2, n)
