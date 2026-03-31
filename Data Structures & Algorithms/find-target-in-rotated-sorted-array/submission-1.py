class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (r+l)//2
            if nums[m]==target:
                return m
            if nums[l] <= nums[m]:#Left part are ordered
                if nums[l] <= target < nums[m]:#Target are in left ordered part
                    r=m-1
                else:
                    l = m+1
            else:#Right part are ordered
                if nums[m] < target <=nums[r]:#Target are in right ordered part
                    l=m+1
                else:
                    r=m-1
        return -1





        
        