class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = iter(t)
        is_true = all(char in i for char in s)
        return is_true
        