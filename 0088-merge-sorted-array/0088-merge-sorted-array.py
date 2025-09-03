class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s=n-1
        l=m-1
        h=m+n-1
        while s>=0:
            if l>=0 and nums1[l]>nums2[s]:
                nums1[h]=nums1[l]
                l-=1
            else:
                nums1[h]=nums2[s]
                s-=1
            h-=1
        