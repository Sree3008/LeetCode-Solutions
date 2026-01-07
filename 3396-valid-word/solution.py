class Solution:
    def isValid(self, word: str) -> bool:
        x='AEIOUaeiou'
        y='qwrtyoplkjhgfdszxcvbnmQWRTYPLKJHGFDSZXXCVBNM'
        c=0
        c1=0
        if len(word)>=3 and word.isalnum():
            for i in word:
                if i in x:
                    c+=1
                if i in y:
                    c1+=1
        if c>=1 and c1>=1:
            return True
        return False

