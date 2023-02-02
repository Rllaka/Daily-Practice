class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = {}
        for i in range(len(order)):
            map[order[i]] = i
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]
            n = min(len(first), len(second))
            flag = False
            for j in range(n):
                if map[first[j]] < map[second[j]]:
                    flag = True
                    break
                elif map[first[j]] > map[second[j]]:
                    return False
            if not flag and len(first) > len(second):
                return False
        return True
