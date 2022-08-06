class Solution:
    def canPlaceFlowers1(self, flowerbed: [int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if n == 0:
                break
            if i == 0:
                if flowerbed[i] == 0:
                    if length == 1:
                        n -= 1
                        flowerbed[i] = 1
                    else:
                        if flowerbed[i+1] == 0:
                            n -= 1
                            flowerbed[i] = 1
                        else:
                            continue
                else:
                    continue
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0:
                    if i == length - 1:
                        if flowerbed[length - 1] == 0:
                            n -= 1
                            flowerbed[i] = 1
                    elif flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
        if n == 0:
            return True
        else:
            return False

    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        if n == 0:
            return True
        length = len(flowerbed)
        if length == 0:
            return False
        if length == 1:
            if flowerbed[0] == 1:
                return False
            else:
                n -= 1
                flowerbed[0] == 1
        else:
            for i in range(length):
                if n == 0:
                    break
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                elif i == length - 1:
                    if flowerbed[length - 1] == 0 and flowerbed[length - 2] == 0:
                        n -= 1
                        flowerbed[i] = 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
        if n == 0:
            return True
        else:
            return False


