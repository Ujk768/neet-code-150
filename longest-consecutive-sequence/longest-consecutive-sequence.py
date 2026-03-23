from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if(len(nums)==0):
            return 0
        # set to keep track of numebrs already seen
        seen = set(nums)
        max_len = 0
        for num in seen :
            # if num -1 doesnt exist in set it means it could be start of sequence
            if num -1 not in seen:
                curr = num
                currlen =1
                # check all sequences that can be formed going forward
                while(curr +1 in seen):
                    curr+=1
                    currlen +=1
                max_len = max(max_len , currlen)
        return max_len
        
if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([2,20,4,10,3,4,5]))
    print(s.longestConsecutive([0,3,2,5,4,6,1,1]))
    