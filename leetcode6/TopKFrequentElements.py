class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        kFrequent = {}
        kSorted = {}
        res = []
        for num in nums:
            v = kFrequent.setdefault(num, 0)
            kFrequent[num] = v + 1
        for key, value in kFrequent.items():
             if value not in kSorted:
                kSorted[value] = key
             else:
                vk = kSorted[value]
                if isinstance(vk, list):
                    vk.append(key)
                    kSorted[value] = vk
                else:
                    arr = [vk, key]
                    kSorted[value] = arr
        keys = kSorted.keys()
        keysArr = list(keys)
        keysArr.sort(reverse=True)
        for i in range(len(keysArr)):
            if len(res) == k:
                break
            elif len(res) < k:
                if isinstance(kSorted[keysArr[i]], list):
                    res.extend(kSorted[keysArr[i]])
                else:
                    res.append(kSorted[keysArr[i]])
            elif len(res) > k:
                count = len(res) - k
                for _ in range(count):
                    res.pop()
        return res