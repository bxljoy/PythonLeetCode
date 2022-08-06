class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array = s.split(' ')
        for i in range(len(array)-1, -1, -1):
            if array[i] != '':
                return len(array[i])

if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    print(s.split(' '))
