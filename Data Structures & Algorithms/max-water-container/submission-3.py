class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            left_val = heights[l]
            right_val = heights[r]
            current_area = (r-l)*min(left_val, right_val)
            if current_area > max_area:
                max_area = current_area
            if right_val > left_val:
                l+=1
            elif left_val > right_val:
                r-=1
            else:#equal
                r-=1
        return max_area
"""
7
36
10
20
12
12
3
"""
        #I=0=>1
        #J=7=>7
        #current_amount = (7-0)*min(1,7) => 7
        #max_area = 7

        #if left+1 is bigger than left_value + 1:
            #left+=1
        #elif right-1 is bigger than left_value + 1:
            #right-=1
        #I=0=>1
        #J=7=>6
        #current_amount = (7-0)*min(1,6) => 7
