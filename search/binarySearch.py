
def binarySearch(alist, num):
    low = 0
    high = len(alist) - 1
    found = False

    while low <= high and not found:
        mid = (low + high) // 2
        if alist[mid] == num:
            found = True
        elif alist[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return found

def binarySearchRecursion(alist, num):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == num:
            return True
        else:
            if alist[mid] > num:
                return binarySearchRecursion(alist[:mid-1], num)
            else:
                return binarySearchRecursion(alist[mid+1:], num)

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(binarySearch(nums, 10))
    print(binarySearchRecursion(nums, 5))
