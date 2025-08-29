class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if needle in haystack:
                 return haystack.index(needle)
            else:
                return -1
        
    
       
    