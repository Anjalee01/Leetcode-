class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        pos = 0
        neg = 0

        for num in nums:
            if num == 0:
                continue
            elif num<0:
                pos += 1
            else:
                neg +=1
        return max(pos,neg)



        