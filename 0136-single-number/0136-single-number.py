class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # if len(nums) == 1:
        #     return nums[0]

        # newset = set(nums)  #[2,1]

        # for i in newset:
        #     if nums.count(i) == 1:
        #         return i


        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for i in dic:
            if dic[i] == 1:
                return i






        












        # if len(nums)==1:
        #     return nums[0]
        
        # newset = set(nums)

        # for i in newset:
        #     if nums.count(i) == 1:
        #         return i
        