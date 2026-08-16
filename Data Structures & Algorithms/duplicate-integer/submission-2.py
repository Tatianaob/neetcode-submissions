class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = set()
        # if len(newList) < len(nums):
        #     return True
        # return False
        for num in nums:
            if num in newList:
                return True
            newList.add(num)
        return False
    