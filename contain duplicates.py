class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        f={}
        for num in nums:
            f[num]=f.get(num,0)+1
        y=list(f.values())
        for i in y:
            if i>=2:
                return True
                break
        else:
            return False