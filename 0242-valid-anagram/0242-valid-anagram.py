class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Not an optimal approach

        s1 = sorted(s)
        s2 = sorted(t)

        # compare sorted strings
        return s1 == s2
        