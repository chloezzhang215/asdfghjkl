# Median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer_array = []
        if nums1 or nums2 != None:
            mer_array = sorted(nums1+nums2)
        return median(mer_array)
