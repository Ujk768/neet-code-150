from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1] * len(nums)
        suffix=[1] * len(nums)
        for ind , val in enumerate(nums):
            if ind == 0:
                prefix[ind] = val
            else:
                prefix[ind] = prefix[ind-1] * val


        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) -1 :
                suffix[i] = nums[i]
            else:   
                suffix[i] = suffix[i+1] * nums[i]
        ans =[1] * len(nums)
        for i in range(len(nums)):
            if i==0:
                ans[i] = suffix[i+1]
            elif i==len(nums)-1:
                ans[i]=prefix[i-1]
            else:
                ans[i] = prefix[i-1] * suffix[i+1]

        return ans   

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,4,6]))
    print(s.productExceptSelf([-1,0,1,2,3]))     

