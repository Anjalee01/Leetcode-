class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        seen = defaultdict(int) 
        
        for item in nums:
            if item % 2 == 0:
                seen[item] +=1
        
        max = 0
        output = -1

        for element, count in seen.items():
            if count > max:
                max, output = count, element
            elif count == max:
                output = min(element, output)
        return output



     

       

  




        