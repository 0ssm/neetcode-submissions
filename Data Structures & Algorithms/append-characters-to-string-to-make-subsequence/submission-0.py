class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        ns = len(s)
        nt = len(t)
        while i < ns and j < nt:
            if s[i] == t[j]:
                j += 1
            i += 1
        return nt - j

        