class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        arr = []
        for num, count in frequency.items():
            arr.append([count, num])
        arr.sort()

        res = []
        i = 0
        while i < k:
            res.append(arr.pop()[1])
            i += 1
        return res