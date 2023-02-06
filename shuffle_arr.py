class Solution:
    def shuffle(self, a: List[int], n: int) -> List[int]:
        return chain(*zip(a[:n], a[n:]))
