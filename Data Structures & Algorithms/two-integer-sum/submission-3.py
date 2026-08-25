class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        findMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in findMap:
                return [findMap[diff], i]
            findMap[nums[i]] = i
        return []