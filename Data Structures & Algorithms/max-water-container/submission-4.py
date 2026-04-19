class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0
        while l<=r:
            cur_area = (r-l)*min(height[r], height[l])
            max_area = max(max_area, cur_area)
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return max_area
        