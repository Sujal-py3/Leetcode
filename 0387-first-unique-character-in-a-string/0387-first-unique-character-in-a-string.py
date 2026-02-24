from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map1=Counter(s)
        for i, char in enumerate(s):
            if map1[char]==1:
                return i 
        return -1



        