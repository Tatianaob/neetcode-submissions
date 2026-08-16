class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [3,4,5,6] target = 7
        # [0, 1] 
        # difference = target - num
        # seen {num: index}
        # return current index, plus index


        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[nums[i]] = i