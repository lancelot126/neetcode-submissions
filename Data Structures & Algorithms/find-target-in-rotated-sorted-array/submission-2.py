class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minimum = 0
        l = 0
        r = len(nums) - 1
        # while l <= r:
        #     if nums[l] < nums[r]:
        #         minimum = min(nums[minimum], nums[l])
        #         break
        #     mid = (l + r) // 2
        #     minimum = min(nums[minimum], nums[mid])
        #     if nums[mid] >= nums[l]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        pivot = nums.index(min(nums))

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
            
        res = binary_search(0, pivot - 1)
        if res != -1:
            return res
        return binary_search(pivot, len(nums) - 1)
