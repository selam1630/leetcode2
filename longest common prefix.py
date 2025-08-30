class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        r = 1
        prefix = ""
        first = strs[0]

        for i in range(1, len(first) + 1):  
            candidate = first[:i]
            if all(s.startswith(candidate) for s in strs):
                prefix = candidate
            else:
                break
        return prefix
