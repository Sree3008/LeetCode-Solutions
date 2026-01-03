class Solution:
    def categorizeBox(self, leng: int, wid: int, hei: int, mass: int) -> str:
        list1=[]
        if leng>=10**4 or wid>=10**4 or hei>=10**4 or leng*wid*hei>=10**9:
            list1.append("Bulky")
        if mass>=100:
            list1.append("Heavy")
        if len(list1)==2:
            return "Both"
        if len(list1)==1:
            return list1[0]
        return "Neither"


        
