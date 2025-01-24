class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        temp= 0
        for i in range(len(nums)):
            temp = temp + nums[i]
            arr.append(temp)
        return arr
        