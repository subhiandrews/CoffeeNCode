class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = 0, 0
        l = len(haystack)
        m = len(needle)
        start = -1
        found = False

        if m > l:
            return start
        elif haystack == needle:
            return 0
    
        while h < l and n < m:
            if haystack[h] == needle[n]:
                if start < 0:
                    start = h
                h += 1
                n += 1
                if n >= m:
                    found = True
                    break
            else:
                if start >= 0:
                    h = start + 1
                    start = - 1
                    n = 0
                else:
                    h += 1
        if not found:
            start = -1
        return start
