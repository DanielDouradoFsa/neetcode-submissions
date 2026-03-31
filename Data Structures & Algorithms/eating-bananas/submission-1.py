class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas_in_pile = max(piles)
        l, r = 1, max_bananas_in_pile 
        res = r
        def canEatInTime(currRate):
            total_hours_spent=0
            for bananas in piles:
                total_hours_spent += math.ceil(float(bananas)/currRate)
            return total_hours_spent<=h

        while l<=r:
            m = (r+l)//2
            if canEatInTime(m):
                res = min(res,m)
                r = m -1
            else:
                l=m+1
        return res