class Solution:
    def countVowels(self, word: str) -> int:
        vowels = 'aeiouAEIOU'
        n = len(word)
        c = 0
        for i in range(n):
            if word[i] in vowels:
                c += (i + 1) * (n - i)

        return c

