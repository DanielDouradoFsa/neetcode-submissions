class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_off_all = 1
        number_of_zeros = 0
        for number in nums:
            if number_of_zeros>1:
                break
            if number==0:
                number_of_zeros+=1
            else:
                product_off_all = number*product_off_all
        if number_of_zeros>1:
            return [0 for _ in range(len(nums))]
        output = []
        print(number_of_zeros)
        print(product_off_all)
        for i in range(len(nums)):
            if number_of_zeros:
                if nums[i]!=0:
                    output.append(0)
                else:
                    output.append(product_off_all)
            else:
                output.append(product_off_all//nums[i])
        return output

            

        