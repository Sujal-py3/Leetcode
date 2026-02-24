class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,num in enumerate(nums) :
            a=target-num
            if a in s:
                return [s[a], i]
            s[num]=i
        
                    
        