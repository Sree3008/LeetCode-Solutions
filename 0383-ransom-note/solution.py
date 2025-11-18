class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list1=[]
        for i in magazine:
            list1.append(i)
        
        for i in ransomNote:
            if i in list1:
                list1.remove(i)
            else:
                return False
        return True
                
