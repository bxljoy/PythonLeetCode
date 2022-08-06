import TwoStackForQueue as ts
# use queue to implement the radixSort
def sortNumbers(nums):
    mainBucket = ts.Queue()
    buckets = [ts.Queue() for _ in range(10)]
    for num in nums:
        mainBucket.enqueue(num)
    length = len(str(max(nums)))
    for n in range(length+1):
        for _ in range(mainBucket.size()):
            num = mainBucket.dequeque()
            posNum = getNumberPos(num, n)
            for j in range(10):
                if posNum == j:
                    buckets[j].enqueue(num)
        for k in range(10):
            while not buckets[k].isEmpty():
                mainBucket.enqueue(buckets[k].dequeque())
    return mainBucket
# use List to implement the radixSort
def radixSort(nums):
    mainBucket = []
    buckets = [[] for _ in range(10)]
    maxNum = max(nums)
    length = len(str(maxNum))
    for num in nums:
        mainBucket.append(num)
    for i in range(length+1):
        for _ in range(len(mainBucket)):
            num = mainBucket.pop()
            numPos = getNumberPos(num, i)
            for j in range(10):
                if numPos == j:
                    buckets[j].append(num)
        for k in range(10):
            while len(buckets[k]) != 0:
                mainBucket.append(buckets[k].pop())
    return mainBucket

def getNumberPos(num, pos):
    return (num // 10 ** (pos - 1)) % 10

if __name__ == '__main__':
    nums = [123, 456, 342, 789, 433, 12, 6, 12345, 4321, 30, 0]
    # mBucket = sortNumbers(nums)
    # for i in range(mBucket.size()):
    #     print(mBucket.dequeque())

    mBucket = radixSort(nums)
    for _ in range(len(mBucket)):
        print(mBucket.pop(0))





