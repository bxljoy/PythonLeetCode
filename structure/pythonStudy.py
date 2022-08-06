import math, cmath
def binary_search(nums, item):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = nums[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

class Fraction:
    def __init__(self, top, bottom):
        if isinstance(top, int) and isinstance(bottom, int):
            common = gcd(top, bottom)
            self.num = top // common
            self.den = bottom // common
        else:
            raise RuntimeError("top or bottom is not integer!")

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newNum = self.num * other.den + self.den * other.num
        newDen = self.den * other.den
        # common = gcd(newNum, newDen)
        # return Fraction(newNum // common, newDen // common)
        return Fraction(newNum, newDen)

    def __sub__(self, other):
        newNum = self.num * other.den - self.den * other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)

    def __mul__(self, other):
        newNum = self.num * other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)

    def __truediv__(self, other):
        newNum = self.num * other.den
        newDen = self.den * other.num
        return Fraction(newNum, newDen)

    def __gt__(self, other):
        firstFraction = self.num * other.den
        secondFraction = other.num * self.den
        return firstFraction > secondFraction

    def __ge__(self, other):
        firstFraction = self.num * other.den
        secondFraction = other.num * self.den
        return (firstFraction > secondFraction) or (firstFraction == secondFraction)

    def __lt__(self, other):
        firstFraction = self.num * other.den
        secondFraction = other.num * self.den
        return firstFraction < secondFraction

    def __le__(self, other):
        firstFraction = self.num * other.den
        secondFraction = other.num * self.den
        return (firstFraction < secondFraction) or (firstFraction == secondFraction)

    def __ne__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum != secondNum

    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum == secondNum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # nums = [1,3,5,6,7,8,9,15,34,45,46,67,78,99,123]
    # print(binary_search(nums, 1))
    # print(binary_search(nums, 67))

    # f1 = Fraction(1, 2)
    # f2 = Fraction(1, 4)
    # myf = f1 + f2
    # print(myf)
    # myf = f1 - f2
    # print(myf)
    # myf = f1 * f2
    # print(myf)
    # myf = f1 / f2
    # print(myf)
    # myf = f1 > f2
    # print(myf)
    # myf = f1 >= f2
    # print(myf)
    # myf = f1 < f2
    # print(myf)
    # myf = f1 <= f2
    # print(myf)
    # myf = f1 != f2
    # print(myf)
    # myf = f1 == f2
    # print(myf)

    nums = [1,3,5,6,7,8,9,15,34,45,46,67,78,99,123]
    first, *middle, last = nums
    print(middle)
    print(max(middle))
