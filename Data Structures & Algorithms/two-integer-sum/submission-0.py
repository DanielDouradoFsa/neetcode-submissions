class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_prev_index = {}
        for index in range(len(nums)):
            num = nums[index]
            diff_value = target - num
            if diff_prev_index.get(num,None) != None:
                prev_index = diff_prev_index[num]
                return [prev_index, index]
            else:
                diff_prev_index[diff_value] = index
        return []