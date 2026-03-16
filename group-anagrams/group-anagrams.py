from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm ={}
        ans = []
        for i in range(len(strs)):
            key = strs[i]
            sorted_key = sorted(key)
            join_sorted_key = "".join(sorted_key)
            hm.setdefault(join_sorted_key, []).append(strs[i])

        for key , val in hm.items():
            ans.append(val)
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))