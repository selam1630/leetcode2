class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fre={}
        for i in nums:
            fre[i] = fre.get(i, 0) + 1
        for key,val in fre.items():
            if val==1:
                return key