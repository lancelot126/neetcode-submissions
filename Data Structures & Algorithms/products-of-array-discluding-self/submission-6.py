class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1
        if zero_count >= 2:
            return [0] * n

        result = []
        if zero_count == 1:
            for i in range(n):
                if nums[i] != 0:
                    result.append(0)
                else:
                    result.append(total_product)
        else:
            for i in range(n):
                val = total_product // nums[i]
                result.append(val)
        return result

                
