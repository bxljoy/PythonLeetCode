class Solution:
    def twoSum1(self, numbers: [int], target: int) -> [int]:
        array = []
        for i in range(len(numbers)):
            if numbers[i] in array:
                continue
            res = target - numbers[i]
            if numbers.count(res) > 0:
                resNum = numbers.index(res)
                if i == resNum:
                    numbers[resNum] += 1
                    resNum = numbers.index(res)
                break
            else:
                array.append(numbers[i])
        return [i+1, resNum+1]

    def twoSum(self, numbers: [int], target: int) -> [int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum == target:
                return [left+1, right+1]
            else:
                left += 1


