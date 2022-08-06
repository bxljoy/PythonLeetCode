class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        res = []
        while len(l) - (k*2) > 0:
            left = l[:k]
            self.reverse(left)
            total = left + l[k:k*2]
            res += total
            l = l[k*2:]
        if len(l) < k:
            self.reverse(l)
            res += l
        elif k <= len(l) <= k*2:
            left = l[:k]
            self.reverse(left)
            total = left + l[k:]
            res += total
        return ''.join(res)

    def reverse(self, s: [str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    s = Solution()
    output = s.reverseStr('krmyfshbspcgtesxnnljhfursyissjnsocgdhgfxubewllxzqhpasguvlrxtkgatzfybprfmmfithphckksnvjkcvnsqgsgosfxc', 20)
    print(output)
