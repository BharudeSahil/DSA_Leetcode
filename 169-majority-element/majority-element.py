class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        n = len(nums)

        for i in nums:
            count[i] = count.get(i, 0) + 1
            if count[i] > n // 2:
                return i