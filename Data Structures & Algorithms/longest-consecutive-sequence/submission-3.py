class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        count = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            length = 1
            while num + length in numSet:
                length += 1
            count = max(count, length)
        return count