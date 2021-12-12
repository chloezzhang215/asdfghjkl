class Solution:
    def isUnique(self, astr: str) -> bool:
        if len(astr) == len(set(astr)):
            return True
        else:
            return False
