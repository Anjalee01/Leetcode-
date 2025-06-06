class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (r+l)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1
        return l


        