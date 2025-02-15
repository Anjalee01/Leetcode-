class Solution:
    def romanToInt(self, s: str) -> int:

        my_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        last_index = len(s) - 1
        result = 0
        last_digit = 0
        
        for a in range(last_index, -1, -1):
            if my_map[s[a]] >= last_digit:
                result += my_map[s[a]]
            else:
                result -= my_map[s[a]]
            last_digit = my_map[s[a]]
        
        return result

        