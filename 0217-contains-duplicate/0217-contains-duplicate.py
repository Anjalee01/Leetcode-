class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h_set = set()

        for i in nums:
            if i in h_set:
                return True
            h_set.add(i)
        return False



# Brute force approach
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        

