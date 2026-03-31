class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                longer = 1
                while num+longer in nums:
                    longer+=1
                longest = max(longest, longer)
        return longest
        