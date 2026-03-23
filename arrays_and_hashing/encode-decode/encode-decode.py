from typing import List


class Solution:

    # Encodes a list of strings to a single string.
    # We encode in such a way that we store the lenght and then a delemiter # followed by the string itself.
    #  This way we can easily decode the string later by looking for the delemiter 
    # and then using the length to extract the original string.
    def encode(self, strs: List[str]) -> str:
        ans=""
        for s in strs:
            ans+= str(len(s)) + '#' + s    
          
        return ans

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # Look for the delemiter # to find the length of the next string 
            j = i
            while s[j] != '#':
                j += 1
            # From the start to before the delemiter is the length of the string, so we convert it to an integer
            length = int(s[i:j])
            # After the delemiter, we can extract the original string using the length we just found and add it to the result list
            res.append(s[j + 1 : j + 1 + length])
            # Move the index i to the start of the next encoded string, which is after the current string we just extracted
            i = j + 1 + length
        return res
    
if __name__ == "__main__":
    s = Solution()
    encoded_str = s.encode(["Hello", "World"])
    print(encoded_str)
    decoded_str = s.decode(encoded_str)
    print(decoded_str)
