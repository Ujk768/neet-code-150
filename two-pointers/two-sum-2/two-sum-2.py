from typing import List

class Solution:
    # Normal Approach
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     hm = {}

    #     for i in range(len(numbers)) :
    #         if target - numbers[i] in hm:
    #             return [hm[target - numbers[i]]+1,i+1]
    #         hm[numbers[i]] = i

    #     return []

    # since the array is sorted we can use binary search to solve this
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers) -1

        while(start <end):
            # currSum
            target_sum = numbers[start] + numbers[end]
            # if current sum = target return the indexes
            if target_sum == target :
                return [start+1,end+1]
            # if sum is more than target reduce end pointer to get a smaller sum
            if target_sum > target :
                end-=1
            # if sum is smaller than target increase start to get bigger sum
            if target_sum < target :
                start +=1
        
        return []
        

if __name__ == "__main__" :
    s = Solution()
    print(s.twoSum([1,2,3,4]))
    print(s.twoSum([1,2,3,4]))
