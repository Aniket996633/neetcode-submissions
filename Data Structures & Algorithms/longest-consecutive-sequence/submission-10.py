class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        long_streak = 0
        cnt = 0
        for i in unique:
            if i-1 not in unique:
                cnt = 1
                curr_i = i
                while curr_i + 1 in unique:
                    cnt +=1
                    curr_i += 1
                long_streak = max(long_streak, cnt)
        return long_streak    

        