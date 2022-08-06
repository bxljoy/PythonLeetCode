class Solution:
    def intersect(self, nums1, nums2):
        """
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [4,9]
        """
        resultDic = dict()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j not in resultDic:
                        resultDic.setdefault(j, nums2[j])
                        break
        return list(resultDic.values())

class Solution2:
    def intersect(self, nums1, nums2):
        """
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [4,9]
        """
        nums1Dic = dict()
        nums2Dic = dict()
        nums3Dic = dict()
        result = []
        for num in nums1:
            if nums1.count(num) > 0:
                nums1Dic.setdefault(num, nums1.count(num))

        for num in nums2:
            if nums2.count(num) > 0:
                nums2Dic.setdefault(num, nums2.count(num))

        for num in nums1Dic.keys():
            if num in nums2Dic:
                nums3Dic.setdefault(num, min(nums1Dic[num], nums2Dic[num]))

        for key,value in nums3Dic.items():
            result += [key]*value

        return result


if __name__ == '__main__':
    s = Solution2()
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(s.intersect(nums1, nums2))



