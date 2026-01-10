class Solution:
    def minMaxDifference(self, num: int) -> int:
        # maxi=0
        # s=str(num)
        # for i in s:
        #     if maxi<int(i):
        #         maxi=int(i)
        # x=''
        # for i in range(len(s)):
        #     if str(maxi)!=s[i]:
        #         x=s[i]
        #         break
        # s1=list(s)
        # for i in range(len(s1)):
        #     if s1[i]==x:
        #         s1[i]=str(maxi)
        # z=int(''.join(s1))
        # y = ''
        # for i in range(len(s)):
        #     if s[i] != '0':
        #         y = s[i]
        #         break

        # s2 = list(s)
        # for i in range(len(s2)):
        #     if s2[i] == y:
        #         s2[i] = '0'
        # a = int(''.join(s2))
        # return z-a      
        s = str(num)
        x = ''
        for i in range(len(s)):
            if s[i] != '9':
                x = s[i]
                break

        s1 = list(s)
        for i in range(len(s1)):
            if s1[i] == x:
                s1[i] = '9'
        z = int(''.join(s1))
        y = ''
        for i in range(len(s)):
            if s[i] != '0':
                y = s[i]
                break

        s2 = list(s)
        for i in range(len(s2)):
            if s2[i] == y:
                s2[i] = '0'
        a = int(''.join(s2))

        return z - a 

        
