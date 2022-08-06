def getMinNum(nums):
    """
    :param nums: a list(array) contains numbers
    :return: the minimum number of the list
    """
    minNum = nums[0]
    minIndex = 0
    for i in range(len(nums)):
        if minNum > nums[i]:
            minNum = nums[i]
            minIndex = i
    return minIndex

def selectionSort(nums):
    """
    selection sort
    :param nums: a list contains numbers
    :return: a new ascending sorted list
    """
    sortedNums = []
    while len(nums) > 0:
        minIndex = getMinNum(nums)
        sortedNums.append(nums[minIndex])
        nums.remove(nums[minIndex])
    return sortedNums

def selectionSort2(nums):
    """
    selection sort : find the maximum number, and put it on the tail of the list
    :param nums: the unsorted list
    :return: no return value
    """
    for j in range(len(nums)-1, 0, -1):
        maxIndex = 0
        for i in range(j):
            if nums[i] < nums[j]:
                maxIndex = i+1
        nums[maxIndex], nums[j] = nums[j], nums[maxIndex]

if __name__ == '__main__':
    nums = [5, 3, 2, 6, 9, 1, 7, 14]
    print(selectionSort(nums))
    nums = [5, 3, 2, 6, 9, 1, 7, 14]
    selectionSort2(nums)
    print(nums)


