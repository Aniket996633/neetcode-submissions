class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = dict()
        res = []
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        sort = sorted(hash.values(),reverse=True)
        sort = sort[:k]
        for k,v in hash.items():
            if v in sort:
                res.append(k)
        return res
        
            
        