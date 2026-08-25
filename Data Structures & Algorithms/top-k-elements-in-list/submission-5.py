class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        arr = []
        for num, count in frequency.items():
            arr.append([count, num])
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        return result