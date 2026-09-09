class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = sorted(strs)
        ad = 0
        idx = 0
        while idx < len(st[0]) and idx < len(st[-1]) and st[0][idx] == st[-1][idx]:
            ad += 1
            idx += 1
        if ad == 0:
            return ""
        else:
            return st[0][:ad]