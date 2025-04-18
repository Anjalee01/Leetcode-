class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        # print(words)

        reversed_word = []
        for word in words:
            reversed_word.append(word[::-1])

        return " ".join(reversed_word)
        