class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = set(nums)
        if len(nums)-len(val) == 0:
            return False
        else:
            return True


        