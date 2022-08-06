def mergeSort(aList):
    if len(aList) <= 1:
        return aList

    mid = len(aList) // 2
    left_half = aList[:mid]
    right_half = aList[mid:]

    left = mergeSort(left_half)
    right = mergeSort(right_half)

    return merge(left, right)


def merge(left, right):
    mergeList = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mergeList.append(left[i])
            i += 1
        else:
            mergeList.append(right[j])
            j += 1

    # mergeList += left[i:]
    # mergeList += right[j:]

    while i < len(left):
        mergeList.append(left[i])
        i += 1
    while j < len(right):
        mergeList.append(right[j])
        j += 1

    return mergeList

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_alist = mergeSort(alist)
    print(sorted_alist)