class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        res = []

        set_spaces = set(spaces)

        for i, char in enumerate(s):
            if i in set_spaces:
                res.append(" ")
            res.append(char)
        return "".join(res)
        