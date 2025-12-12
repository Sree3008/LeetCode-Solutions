class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x=word.find(ch)
        list1=list(word[:x+1])
        list1.reverse()
        return ''.join(list1)+word[x+1:]
        
