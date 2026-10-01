class Solution:
    def maxArea(self, heights: List[int]) -> int:
        temp_area = 0
        l = 0
        r = len(heights) - 1
        max_a = 0
        for i in range(len(heights)):
            temp_area = abs((r-l) * min(heights[r],heights[l]))
            if min(heights[r],heights[l]) == heights[r]:
                r-=1
            else:
                l+=1
            max_a = max(max_a,temp_area)
        return max_a
        