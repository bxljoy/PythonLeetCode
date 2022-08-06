
def binarySearchRecursion(nums, target):
    if len(nums) == 0:
        return False
    if len(nums) == 1:
        if nums[0] == target:
            return True
        else:
            return False
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return binarySearchRecursion(nums[:mid], target)
        else:
            return binarySearchRecursion(nums[(mid+1):], target)

def sumRecursion(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sumRecursion(nums[1:])

def maxRecursion(nums):
    if len(nums) == 2:
        if nums[0] >= nums[1]:
            return nums[0]
        else:
            return nums[1]
    submax = maxRecursion(nums[1:])
    if nums[0] > submax:
        return nums[0]
    else:
        return submax

if __name__ == '__main__':
    nums = [1, 3, 5, 7, 9]
    print(sumRecursion(nums))
    print(binarySearchRecursion(nums, 5))
