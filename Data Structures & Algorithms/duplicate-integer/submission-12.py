class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDuplicate = set()
        for num in nums:
            if num in checkDuplicate:
                return True
            else:
                checkDuplicate.add(num)
        return False