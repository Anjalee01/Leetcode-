class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_value = max(candies)
        res = []

        for currentValue in candies:
            if currentValue + extraCandies >= max_value:
                res.append(True)
            else: 
                res.append(False)
        return res
      