class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(0, len(nums)):
        #     if i not in nums:
        #         return i
        
        num_set = set(nums)
        n = len(nums)

        for i in range(n + 1):
            if i not in num_set:
                return i
                