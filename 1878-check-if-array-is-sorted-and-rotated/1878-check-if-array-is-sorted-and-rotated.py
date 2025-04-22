class Solution:
    def check(self, nums: List[int]) -> bool:

        counter = 0

        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % len(nums)]:
                counter += 1
        return counter <= 1
        