class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = {}

        for i in range(len(strs)):
            s = strs[i]
            key = ''.join(sorted(s))

            if key not in mp:
                mp[key] = len(res)
                res.append([s])
            else:
                res[mp[key]].append(s)
        return res

