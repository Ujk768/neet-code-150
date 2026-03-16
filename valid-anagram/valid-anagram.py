# Given two strings s and t, 
# return true if the two strings are anagrams of each other,
#  otherwise return false.

# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.

# Input: s = "racecar", t = "carrace"

# Output: true


# Input: s = "jar", t = "jam"

# Output: false



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # If the lengths of the strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False;
        
        hm_s = {}
        hm_t = {}

        # Count the frequency of each character in both strings
        for i in range(len(s)):
            hm_s[s[i]] = hm_s.get(s[i],0) +1;
            hm_t[t[i]] = hm_t.get(t[i],0) +1;

        # Compare the frequency dictionaries. If they are the same, the strings are anagrams
        return hm_s == hm_t 
        

if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))