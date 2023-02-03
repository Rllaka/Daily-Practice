class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        m = numRows
        grid = [[] for _ in range(m)]
        r, c, pos = 0, 0, 0
        while pos < len(s):
            if r == 0:
                for r in range(m):
                    if pos >= len(s):
                        break
                    grid[r].append(s[pos])
                    pos += 1
            else:
                grid[r].append(s[pos])
                pos += 1
            r -= 1
        
        res = ""
        for row in grid:
            res += "".join(row)
        return res
