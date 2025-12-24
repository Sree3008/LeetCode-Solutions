class Solution:
    def isPrefixOfWord(self, s: str, se: str) -> int:
        list1=s.split(' ')
        for i in range(len(list1)):
            if list1[i].startswith(se):
                return i+1
        return -1
