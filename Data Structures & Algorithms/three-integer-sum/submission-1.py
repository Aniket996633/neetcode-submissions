class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        so = sorted(nums)
        for i in range(len(so)):
            if so[i] > 0:
                break
            if i>0 and so[i] == so[i-1]:
                continue
            left = i+1
            right = len(so) - 1
            while left < right:
                sum = so[i] + so[left] + so[right]
                if sum==0 and i!=left and i!=right:
                    out.append([so[i],so[left],so[right]])

                    while left < right and so[left] == so[left+1]:
                        left+=1
                    while left<right and so[right] == so[right-1]:
                        right-=1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left+=1
                else :
                    right -= 1
        return out
        
            

        