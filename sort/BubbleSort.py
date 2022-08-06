def bubbleSort(nums):
    """
    :param nums: a list(array) contians numbers
    :return: no return value, but this function can change the argument
    cost:  O(n) time complexity
    """
    for j in range(1, len(nums)):
        for i in range(len(nums)-j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

def bubbleSort2(nums):
    for j in range(len(nums)-1, 0, -1):
        for i in range(j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort2(nums)
    print(nums)
