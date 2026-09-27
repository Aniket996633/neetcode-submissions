class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_1 = dict()
        hash_2 = dict()
        for i in s:
            if i in hash_1:
                hash_1[i] += 1
            else:
                hash_1[i] = 1
        for i in t:
            if i in hash_2:
                hash_2[i] += 1
            else:
                hash_2[i] = 1
        if hash_1 == hash_2:
            return True
        else:
            return False