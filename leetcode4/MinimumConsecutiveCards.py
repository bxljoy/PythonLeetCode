class Solution:
    def minimumCardPickup(self, cards: [int]) -> int:
        window = {}
        left = 0
        right = 0
        res = -1
        while right < len(cards):
            c = cards[right]
            right += 1
            cv = window.setdefault(c, 0)
            window[c] = cv + 1
            while window[c] > 1:
                if res > -1:
                    res = min(res, right - left)
                else:
                    res = right - left
                d = cards[left]
                left += 1
                dv = window.setdefault(d, 0)
                window[d] = dv - 1
        return res
