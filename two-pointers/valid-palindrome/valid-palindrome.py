from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start =0
        end = len(s) -1

        while start<end:
            if not s[start].isalnum() :
                start+=1
                continue
            if not s[end].isalnum() :
                end-=1
                continue
            if s[start].lower() != s[end].lower() :
                return False
            start+=1
            end-=1
            
        
        
        return True
             

        

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("Was it a car or a cat I saw?"))
    print(s.isPalindrome("tab a cat"))