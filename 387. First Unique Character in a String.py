class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = []
        for i,j in enumerate(s):
            if not j in s[i+1:] and not j in res:
                return i
            else:
                res.append(j)
        return -1
                
