class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = set(nums)
        if len(newList) < len(nums):
            return True
        return False
        # for num in nums:
        #     if num in newList:
        #         return True
        #     else:
        #         newList.add(num)
        #     return False
    