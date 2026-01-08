class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        list1=[words[0]]
        for i in range(1,len(words)):
            x=Counter(words[i])
            y=Counter(list1[-1])
            if  x!=y:
                list1.append(words[i])
        return list1
            
