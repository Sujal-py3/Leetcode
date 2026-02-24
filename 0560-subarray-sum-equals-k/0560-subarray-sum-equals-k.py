class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s={}
        validsubarray=0
        currsum=0
        for i in nums:
            currsum+= i
            if currsum==k:
                validsubarray += 1
            if currsum-k in s:
                validsubarray += s[currsum-k]
            s[currsum]=s.get(currsum,0)+1
        return validsubarray
        