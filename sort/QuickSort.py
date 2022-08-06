def quickSort(aList):
    if len(aList) <= 1:
        return aList

    point = aList[0]
    left = [i for i in aList[1:] if i < point]
    right = [j for j in aList[1:] if j > point]

    return quickSort(left) + [point] + quickSort(right)

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    alist = quickSort(alist)
    print(alist)