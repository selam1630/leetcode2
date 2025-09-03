class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=sum(nums[:k])
        a=w/k
        for i in range(k,len(nums)):
            w+=nums[i]-nums[i-k]
            a=max(a,w/k)
        return a
        