class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        arr1 = [0] * 26
        arr2 = [0] * 26
        for ch in s1:
            arr1[ord(ch) - ord('a')] += 1
        for i in range(n2):
            arr2[ord(s2[i]) - ord('a')] += 1
            if i >= n1:
                arr2[ord(s2[i - n1]) - ord('a')] -= 1
            if arr1 == arr2:
                return True
        return False
