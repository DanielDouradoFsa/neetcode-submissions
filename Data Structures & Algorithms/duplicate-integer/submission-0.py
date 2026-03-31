class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #store if all vale that appears
        #if value has in store, returne true
        #default false
        values = set()
        for num in nums:
            if num in values:
                return True
            else:
                values.add(num)
        return False