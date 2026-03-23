from typing import List


class Solution:
    def hasDuplicates(self, nums:List[int]) -> bool:
        hm ={}
        for n in nums:
            if n in hm:
                return True
            else:
                hm[n] = 1
        return False
    
    def hasDuplicates2(self, nums:List[int]) -> bool:
        # Add each number to a set and check if it already exists in the set
        seen = set()
        for n in nums:
         # If the number is already in the set, we have a duplicate
         if n in seen:
             return True
         # Otherwise, add the number to the set
         else:
             seen.add(n)
         # No duplicates found, return False
        return False


if __name__ == "__main__":
        s = Solution()
        print(s.hasDuplicates([1,2,3,4]))
        print(s.hasDuplicates2([1,2,3,3]))
    