
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n

def reserveList(nums):
    if len(nums) > 1:
        return reserveList(nums[1:]) + [nums[0]]
    else:
        return nums

def fab(n):
   if n >= 2:
       return fab(n-1) + fab(n-2)
   else:
       return n

def sum(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    return nums[0] + sum(nums[1:])

def count(nums):
    if nums == []:
        return 0
    else:
        return 1 + count(nums[1:])

if __name__ == '__main__':
    # print(factorial(4))
    print(reserveList([1, 2, 3, 4]))
    fabArray = []
    for i in range(1, 10):
        fabArray.append(fab(i))
    print(fabArray)

    print(sum([1, 2, 3, 4, 5]))
    print(count([1, 2, 3, 4, 5]))
