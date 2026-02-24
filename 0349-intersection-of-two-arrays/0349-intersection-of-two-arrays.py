class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #convert both arrays to sets
        se1= set(nums1)
        se2=set(nums2)
        result_set= se1 & se2
        return list(result_set)       