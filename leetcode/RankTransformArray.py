class Solution:
    def arrayRankTransform(self, arr):
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return [1]
        hashmap = {}
        oldArr = arr.copy()
        rankArr = []
        arr.sort(reverse=False)
        rank = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                hashmap.setdefault(arr[i-1], rank)
                hashmap.setdefault(arr[i], rank+1)
                rank += 1
            else:
                hashmap.setdefault(arr[i-1], rank)
                hashmap.setdefault(arr[i], rank)
        for j in range(len(oldArr)):
            rankArr.append(hashmap.get(oldArr[j]))
        return rankArr

if __name__ == '__main__':
    s = Solution()
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    print(s.arrayRankTransform(arr))

