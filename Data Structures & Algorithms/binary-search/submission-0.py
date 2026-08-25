class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while (first <= last):
            middle = int((first + last) / 2)
            if target > nums[middle]:
                first = middle + 1
            elif target < nums[middle]:
                last = middle - 1
            else:
                return middle
        return -1