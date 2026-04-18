class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums) #O(n)
        num_freq_tuple = [(-count,num) for num,count in nums_count.items()] #O(n)
        heapq.heapify(num_freq_tuple)#O(n)
        res = []
        while k>0:#O(k)
            k-=1
            count,num = heapq.heappop(num_freq_tuple)#O(log(n))
            res.append(num)
        return res
        