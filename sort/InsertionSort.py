def insertionSort(aList):
    """
    insertion sort : use the full switch
    :param aList:
    :return:
    """
    for i in range(1, len(aList)):
        for j in range(i-1, 0, -1):
            if aList[j] < aList[j-1]:
                aList[j], aList[j-1] = aList[j-1], aList[j]

def insertionSort2(nums):
    """
    insertion sort: use the incomplete switch, right shift
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):
        currentValue = nums[i]
        position = i
        while position > 0 and nums[position-1] > currentValue:
            nums[position] = nums[position-1]
            position -= 1
        nums[position] = currentValue

if __name__ == '__main__':
    nums = [5, 3, 2, 6, 9, 1, 7, 14]
    insertionSort2(nums)
    print(nums)
