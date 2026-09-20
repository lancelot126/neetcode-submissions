class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[-1]
        for num in nums:
            minimum = min(minimum, num)
        return minimum