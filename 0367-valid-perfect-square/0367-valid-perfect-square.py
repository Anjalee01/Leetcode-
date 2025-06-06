class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l = 1
        r = num

        while (l<=r):
            mid = (r+l)//2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                r = mid - 1
            elif mid*mid < num:
                l = mid + 1
        return False

        
        