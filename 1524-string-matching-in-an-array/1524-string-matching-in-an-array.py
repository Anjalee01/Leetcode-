class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        result = []
    
        # Sort words based on length to optimize substring checks
        words.sort(key=len)
    
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:  
                    result.append(words[i])
                    break  
        
        return result
            
        