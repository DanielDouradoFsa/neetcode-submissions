class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = set()
        max_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in max_substring:
                max_substring.remove(s[left])
                left+=1 
            max_substring.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len


        