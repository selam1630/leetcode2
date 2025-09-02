class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq={}
        y=[]
        for i in nums1:
            freq[i]=freq.get(i,0)+1
            if i in nums2 and freq[i] <= nums2.count(i):
                y.append(i)
        return y
        