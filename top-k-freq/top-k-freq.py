from typing import List


# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.


# Input: nums = [1,2,2,3,3,3], k = 2

# # Output: [2,3]

# Input: nums = [7,7], k = 1

# Output: [7]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        sorted_vals=[]
        ans=[]
        # Count the frequency of each number in the input list and store it in a hash map
        for num in nums:
            hm[num] = hm.get(num,0) +1
        # Sort the hash map by frequency in descending order and store the sorted keys in a list
        sorted_dict = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        
        # Iterate through the sorted hash map and add the keys to the sorted_vals list
        for key in sorted_dict:
            sorted_vals.append(key)
        
        # Add the first k elements from the sorted_vals list to the ans list and return it
        for i in range(k):
            ans.append(sorted_vals[i])
        
        return ans
        
if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))
    print(s.topKFrequent([1], 1))