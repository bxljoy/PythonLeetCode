class Solution:
    def findWords(self, words: [str]) -> [str]:
        res = []
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        for word in words:
            realRow = ''
            flag = True
            wordL = word.lower()
            for i in range(len(wordL)):
                if i == 0:
                    if wordL[i] in row1:
                        realRow = row1
                    elif wordL[i] in row2:
                        realRow = row2
                    elif wordL[i] in row3:
                        realRow = row3
                else:
                    if wordL[i] not in realRow:
                        flag = False
                        break
            if flag:
                res.append(word)
        return res

