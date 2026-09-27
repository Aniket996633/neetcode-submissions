class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        from collections import defaultdict
        out = defaultdict(list)
        res = []
        for i in strs:
            s = sorted(i)
            # print(s)
            back = "".join(s)
            # print(back)
            out[back].append(i)
            # print(out)
        for key, val in out.items():
            # print(val)
            res.append(val)
            # print(res)
        return res

        