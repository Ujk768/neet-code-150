from typing import List


# Given an array of integers nums and an integer target, return the indices i and j 
# such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

# Input: nums = [4,5,6], target = 10

# Output: [0,2]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store the indices of the numbers we have seen so far
        hm ={}
        # use enumerate to get both the index and the value of each number in the list
        for i , val in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - nums[i]
            if diff in hm:
            # If the difference is already in the hash map, we have found the two numbers that add up to the target
                return [hm[diff],i]
            else:
            # If the difference is not in the hash map, add the current number and its index to the hash map
                hm[val] = i
        # If we have gone through the entire list and have not found two numbers that add up to the target, return an empty list        
        return []
    
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4], 6))
    print(s.twoSum([3,3], 6))