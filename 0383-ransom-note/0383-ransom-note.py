class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # charDict = defaultdict(int)


        # for letter in magazine:
        #     charDict[letter] +=1

        # for alpha in ransomNote:
        #     if charDict[alpha] > 0:
        #         charDict[alpha] -=1
        #     else:
        #         return False
        # return True

        count_ransomNote = Counter(ransomNote)
        count_magazine   = Counter(magazine)

        for char, count in count_ransomNote.items():
            if  count_magazine[char] < count:
                return False 

        return True