class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int];
        counterP, pLen = [0] * 26, len(p)
        for c in p:
            counterP[ord(c)-97] += 1
        
        counterS, sLen, j = [0] * 26, 0, 0
        res = []
        for i, c in enumerate(s):
            counterS[ord(c)-97] += 1
            sLen += 1
            while j < i and sLen > pLen:
                counterS[ord(s[j])-97] -= 1
                sLen -= 1
                j += 1
            if sLen == pLen and counterP == counterS:
                res.append(i - (pLen - 1))
        return res
