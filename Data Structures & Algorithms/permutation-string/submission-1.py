class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        countS1 = defaultdict(int)
        for c in s1:
            countS1[c] += 1
        
        for i in range(len(s2)):
            countS2 = defaultdict(int)
            substring = s2[i:i + len(s1)]
            for c in substring:
                countS2[c] += 1
            if countS1 == countS2:
                return True
        return False
            